<template>
  <div class="mt-5" @click="goDetail()">
    <img :src="`https://image.tmdb.org/t/p/w400/${movie.poster_path}`" alt="hotel" style="width:200px">
    {{movie.title}}
  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  },
  methods:{
    goDetail(){
      this.$router.push({name:'detail', params:{id : this.movie.id}})
    }
  }
}
</script>

<style>

</style>