<template>
    <div v-if="actor[2]!=`None`" class="ms-4 me-3" @click="goimagelink()" style="cursor:pointer;">
        <img class="actor-poster" :src="`https://image.tmdb.org/t/p/w400/${actor[2]}`" alt="">
        <p class="actor-name mt-2">{{actor[1]}}</p>

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
.actor-poster {
  width: 130px;
  height: 173px;

  border: 1px solid #FFFFFF;
  border-radius: 9px;
}

.actor-name {
  width: 130px;
  height: 18px;

  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 700;
  font-size: 14px;
  line-height: 17px;
  overflow: hidden;
  white-space: nowrap;
  text-align: center;
  text-overflow: ellipsis;

  color: #FFFFFF;
}
</style>