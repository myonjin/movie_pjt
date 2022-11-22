<template>
  
  <div class="ms-4">
    <img @click="goDetail()" class="poster" :src="`https://image.tmdb.org/t/p/w400/${similar?.poster_path}`" alt="" style="width:150px; height:225px;">
    <p @click="goDetail()" class="title mt-3">{{similar.title}}</p>
    <div @click="goDetail()" class="d-flex">
      <img src="../assets/imdb_logo.png" alt="" style="width: 28px; height: 14px;">
      <p class="vote">{{ similar.vote_average.toFixed(1) }}</p>
    </div>
  </div>
</template>

<script>
export default {
    name:'MovieSimilarListItem',
    props: {
    similar: Object,
    },
    methods:{
    goDetail(){
      this.$router.push({name:'detail', params:{id : this.similar.id}})
    },
    }
}
</script>

<style>

</style>