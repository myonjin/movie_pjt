<template>
  
  <div class="ms-4">
    <img :src="`https://image.tmdb.org/t/p/w400/${similar?.poster_path}`" alt="" style="width:150px; height:225px;">
  </div>
</template>

<script>
export default {
    name:'MovieSimilarListItem',
    props: {
    similar: Object,
  },
}
</script>

<style>

</style>