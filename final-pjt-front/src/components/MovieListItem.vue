<template>
  <div class="ms-4" @click="goDetail()">
    <img class="poster" :src="`https://image.tmdb.org/t/p/w400/${movie.poster_path}`" alt="">
    <p class="title">{{movie.title}}</p>
    <p class="release">{{movie.release_date.slice(0, 4)}}</p>
    <div class="d-flex justify-content-between">
      <div class="d-flex">
        <img src="../assets/imdb_logo.png" alt="" style="width: 28px; height: 14px;">
        <p class="vote">{{ movie.vote_average }}</p>
      </div>
      <!-- 임시!! 좋아요기능 구현 후 버튼넣을거임 -->
      <p>❤</p>
    </div>
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
.poster {
  width:150px;
  height:225px;
  border-radius: 7px;
}
.title {
  width: 150px;
  margin-top: 8px;
  margin-bottom: 8px;
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  line-height: 20px;
  /* identical to box height */
  overflow: hidden;
  white-space: nowrap;
  text-align: left;
  text-overflow: ellipsis;

  color: #FFFFFF;
  }
.release {
  margin-bottom: 5px;
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 700;
  font-size: 11px;
  line-height: 13px;
  text-align: left;

  color: #AFAFAF;
}
.vote {
  margin-left: 4px;
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 700;
  font-size: 14px;
  line-height: 13px;

  color: #FFC907;
  }
</style>