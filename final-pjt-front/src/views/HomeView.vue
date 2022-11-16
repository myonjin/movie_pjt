<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <h1 v-for="movie in this.movieList" :key="movie.id" >{{movie.title}}</h1>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import axios from 'axios'
export default {
  name: 'HomeView',
  components: {
    HelloWorld
  },
  data() {
    return {
      movieList:null,
    }
  },
  methods: {
  },
  created(){
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/totalmovielist',
    })
    .then((res)=>{
      this.movieList= res.data
      console.log(this.movieList)
    })
    .catch((err)=>{
      console.log(err)
    })
  }
}
</script>
