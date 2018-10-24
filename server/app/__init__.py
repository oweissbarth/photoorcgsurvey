from flask import Flask, make_response, send_file, jsonify, request
import os
import random
import hashlib

from flask_pymongo import PyMongo

app = Flask(__name__)

app.config.from_pyfile('config.py')

mongo = PyMongo(app)

cg_imgs = list(map(lambda e: os.path.join(os.path.abspath(
    "./data/cg/"), e), os.listdir("./data/cg")))
photo_imgs = list(map(lambda e: os.path.join(os.path.abspath(
    "./data/photo/"), e), os.listdir("./data/photo")))

img_dict = dict(map(lambda e: (hashlib.md5(
    e.encode("utf-8")).hexdigest(), e), cg_imgs+photo_imgs))


@app.route("/", methods=["GET"])
def get_survey():
    imgs = list(img_dict.keys())
    random.shuffle(imgs)

    response = make_response(jsonify(imgs))

    return response


@app.route("/submit", methods=["POST"])
def submit_survey():
    json = request.get_json(force=True)
    answers = {}
    results = {}
    correct = 0
    for (k, v) in json.items():
        path = img_dict.get(k)

        if path is not None:
            name = os.path.splitext(os.path.basename(path))[0]
            answers[name] = v

            if ("/cg/" in path and v == "cg") or ("/photo/" in path and v == "photo"):
                correct += 1
                results[name] = True
            else:
                results[name] = False
        else:
            answers[k] = v

    mongo.db.responses.insert_one(answers)
    response = make_response(
        jsonify({"correct": correct, "total": len(img_dict), "results": results}))
    return response


@app.route("/images/<string:hash>", methods=["GET"])
def get_image(hash):
    img = img_dict.get(hash)
    if img is None:
        r = make_response()
        r.status_code = 404
        return r
    return send_file(img_dict.get(hash), mimetype="image/jpg")


@app.route("/images", methods=["GET"])
def get_all_images():
    pass
