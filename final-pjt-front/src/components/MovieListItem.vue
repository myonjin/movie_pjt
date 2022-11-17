<template>
  <div>
    <img :src="`https://image.tmdb.org/t/p/w400/${movie.poster_path}`" alt="hotel">
    {{movie.title}}
  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  }
}
</script>

<style>

</style>