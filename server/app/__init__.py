from flask import Flask, make_response, send_file, jsonify, request
import os
import random
import hashlib

import json
from bson.objectid import ObjectId
import datetime

from flask_pymongo import PyMongo

app = Flask(__name__)

app.config.from_pyfile('config.py')

mongo = PyMongo(app)


class JSONEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, (datetime.datetime, datetime.date)):
            return o.isoformat()
        return super(JSONEncoder, self).default(o)


@app.route("/", methods=["GET"])
def get_survey():
    cg_imgs = mongo.db.images.find({}, {})
    imgs = list(cg_imgs)
    random.shuffle(imgs)

    response = make_response(JSONEncoder().encode(imgs))

    return response


@app.route("/submit", methods=["POST"])
def submit_survey():
    json = request.get_json(force=True)
    answers = {}
    results = []
    correct = 0
    total = mongo.db.images.count()
    for (k, v) in json.items():
        ObjectId.is_valid(k)

        if ObjectId.is_valid(k):
            img = mongo.db.images.find_one({"_id": ObjectId(k)})

            id = str(img["_id"])
            answers[id] = v

            if v == "seen":
                total -= 1
                img["correct"] = "seen"
                results.append(img)
                continue

            if (img["type"] == "cg" and v == "cg") or (img["type"] == "photo" and v == "photo"):
                correct += 1
                cur_correct = "correct"
            else:
                cur_correct = "wrong"

            img["correct"] = cur_correct
            results.append(img)

        else:
            answers[k] = v

    mongo.db.responses.insert_one(answers)
    response = make_response(
        JSONEncoder().encode({"correct": correct, "total": total, "results": results}))
    return response


@app.route("/images/<string:id>", methods=["GET"])
def get_image(id):
    img = mongo.db.images.find_one({"_id": ObjectId(id)})
    if img is None:
        r = make_response()
        r.status_code = 404
        return r
    return send_file("../"+img["path"], mimetype="image/jpg")
