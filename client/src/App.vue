<template>
  <div id="app">
    <router-view/>
  </div>
</template>
<script>
export default{
  mounted () {
    this.$router.push('/')
  }
}

</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
body{
  margin: 0;
}

button{
  padding: 15px;
  background-color: firebrick;
  border: none;
  box-shadow: 0px 0px 11px 0px black;
  color: whitesmoke;
  border-radius: 2px;
  min-width: 120px;
  cursor: pointer;
}
</style>
