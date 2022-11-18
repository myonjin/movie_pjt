<template>
  <div style="margin-top:60px;">
    <h1>detail</h1>
    <!-- <p>{{movie}}</p> -->
    <!-- <img :src="`https://image.tmdb.org/t/p/w400/${movie.poster_path}`" alt="hotel" style="width:200px"> -->

    <h3></h3>
  </div>
</template>

<script>
export default {
  name:'DetailView',
  data(){
    return {
      movie: this.$route.params.movie
    }
  },
  // created(){
  //   axios({
  //       method: 'get',
  //       url: `http://127.0.0.1:8000/movies/totalmovielist/${filter}`,
  //       })
  //         .then((res) => {
            
  //           this.movieList = res.data
  //         })
  //         .catch((err) => {
  //           console.log(err)
  //         })
  // }
}
</script>

<style>

</style>