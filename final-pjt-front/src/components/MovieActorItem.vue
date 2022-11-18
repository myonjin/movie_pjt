<template>
    <div v-if="actor[2]!=`None`" class="ms-4" @click="goimagelink()">
        <img class="poster" :src="`https://image.tmdb.org/t/p/w400/${actor[2]}`" alt="">
        <p class="title">{{actor[1]}}</p>

    </div>

</template>

<script>
export default {
  name: 'MovieActorItem',
  props: {
    actor: Array,
  },
  methods:{
    goimagelink(){
        window.location.href=`https://www.themoviedb.org/person/${this.actor[0]}`
    }
  }
}
</script>

<style>

</style>