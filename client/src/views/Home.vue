<template>
  <div class="home">
    <h1>Welcome</h1>
    <p>This is a survey to learn about people's ability to distinguish between photo-realistic computer graphics and photos.</p>
    <p>After answering 2 questions about your background the main part of the survey will start. You will see image and two buttons. Please decide wheter you think the image is a photo or computer graphics. Based on your decision click on the corresponding button.</p>
    <strong>IMPORTANT: IF YOU SAW THE IMAGE BEFORE SEEING IT IN THE SURVEY PLEASE SELECT "I have already seen this" IN THE UPPER RIGHT HAND CORNER.</strong>
    <p>Notice: Addtionally to your answers timing informataion is collected. No other information is collected. By starting the survey you agree that all collected data can be stored, processed and published. The study is conducted by Oliver Weissbarth. All images are used with permission. Copyright remains with the respective creators.</p>

    <br/>
    <router-link to="survey"><button class="startButton" type="button">Start the survey</button></router-link>
    <br/>
  </div>
</template>

<script>

export default {
  name: 'home'
}
</script>
<style>
  .home{
    width: 95%;
    margin: auto;
    max-width: 700px;
  }

  .startButton{
    margin: 2em;
  }
</style>
