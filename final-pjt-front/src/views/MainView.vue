<template>

  <div>
    <!-- <img style="position:relative; width:100%; height:80%;" alt="Hotel" src="../assets/hotel.jpg"> -->
    <div class="main-image">
      <div class="background-gradation"></div>
    </div>
    <div style="height:1300px"></div>


    <div class="popular_box">
          <MovieList/>
    </div>

    <div class="genre_box">
      <MovieGenreList/>
    </div>

    <FollowingLikeMovieList v-if="this.$store.state.user.following.length>0"/>
    
  </div>

</template>

<script>
// import axios from 'axios'
import MovieList from '@/components/MovieList'
import MovieGenreList from '@/components/MovieGenreList'
import FollowingLikeMovieList from '@/components/FollowingLikeMovieList.vue'

export default {
  name: 'MainView',
  components: {
    MovieList,
    MovieGenreList,
    FollowingLikeMovieList,
  },
  data() {
    return {
      movieList:null,
    }
  },
  methods: {
  }
}
</script>
<style>
.box {
  position: absolute;
  width: 100%;
  height: 80%;
  left: 0px;
  top: 0px;

  background: linear-gradient(90deg, #000000 0%, rgba(0, 0, 0, 0.720349) 0.01%, rgba(1, 1, 1, 0.682696) 0.02%, rgba(5, 5, 5, 0.668436) 0.03%, rgba(0, 0, 0, 0.687449) 0.04%, rgba(183, 183, 183, 0.0458299) 99.99%, rgba(196, 196, 196, 0) 100%);
  }
.popular_box{
  position: absolute;
  width: 92%;
  height: 375px;
  right: 0px;
  bottom: -150px;

  background: rgba(11, 15, 22, 0.47);
  box-shadow: 8px -8px 10px rgba(0, 0, 0, 0.25);
  backdrop-filter: blur(12.5px);
  /* Note: backdrop-filter has minimal browser support */

  border-radius: 24px 0px 0px 24px;
  } 
.popular_text{
  height: 22px;
  text-align: left;
  margin-top: 20px;
  margin-left: 20px;
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 700;
  font-size: 18px;
  line-height: 22px;
  /* identical to box height */
  color: #FFFFFF;
  }
  .genre_box{
    position: absolute;
    width: 92%;
    height: 428px;
    right: 0px;
    bottom: -600px;
  
    background: rgba(11, 15, 22, 0.47);
    box-shadow: 8px -8px 10px rgba(0, 0, 0, 0.25);
    backdrop-filter: blur(12.5px);
    /* Note: backdrop-filter has minimal browser support */
  
    border-radius: 24px 0px 0px 24px;
    }
  .actor_box{
    position: absolute;
    width: 55%;
    height: 320px;
    right: 0px;
    top: 730px;
  
    background: rgba(11, 15, 22, 0.47);
    box-shadow: 8px -8px 10px rgba(0, 0, 0, 0.25);
    backdrop-filter: blur(12.5px);
    /* Note: backdrop-filter has minimal browser support */
  
    border-radius: 24px 0px 0px 24px;
    }  
  .similar_box {
    position: absolute;
    width: 55%;
    height: 320px;
    right: 0px;
    top: 1040px;
  
    background: rgba(11, 15, 22, 0.47);
    box-shadow: 8px -8px 10px rgba(0, 0, 0, 0.25);
    backdrop-filter: blur(12.5px);
    /* Note: backdrop-filter has minimal browser support */
  
    border-radius: 24px 0px 0px 24px;
    } 
  .following-like-movie-box{
  position: absolute;
  width: 92%;
  height: 430px;
  right: 0px;
  bottom: -1040px;

  background: rgba(11, 15, 22, 0.47);
  box-shadow: 8px -8px 10px rgba(0, 0, 0, 0.25);
  backdrop-filter: blur(12.5px);
  /* Note: backdrop-filter has minimal browser support */

  border-radius: 24px 0px 0px 24px;
  }
  .following-like-movie-text{
    height: 22px;
    text-align: left;
    margin-top: 20px;
    margin-left: 0px;
    font-family: 'Montserrat';
    font-style: normal;
    font-weight: 700;
    font-size: 18px;
    line-height: 22px;
    /* identical to box height */
    color: #FFFFFF;
    
    }
  
    .following-like-movie-text span {
      color:#FF9999;
      font-size: 30px;
      cursor: pointer;
    }
.genre_text{
  height: 22px;
  text-align: left;
  margin-top: 20px;
  margin-left: 20px;
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 700;
  font-size: 18px;
  line-height: 22px;
  /* identical to box height */

  color: #FFFFFF;
  }

.main-image {
        position: relative;
        top: 0px;
        margin: 0;
        width: 100%;
        height: 100vh;
        background: linear-gradient(
            to left,
            rgb(0, 0, 0, 0.9) 0%,
            rgb(0, 0, 0, 0.7) 5%,
            rgba(20, 20, 20, 0.4) 30%,
            rgba(20, 20, 20, 0.3) 50%,
            rgba(20, 20, 20, 0.4) 70%,
            rgba(20, 20, 20, 0.7) 95%,
            rgba(0, 0, 0, 0.9) 100%
          ), url(../assets/hotel5.jfif);
        background-size: cover;
      }
.main-image-dark{
        position: relative;
        /* position: absolute; */
        top: 0px;
        margin: 0;
        width: 100%;
        height: 100vh;
        background: linear-gradient(
            to left,
            rgb(0, 0, 0, 0.9) 0%,
            rgb(0, 0, 0, 0.7) 5%,
            rgba(20, 20, 20, 0.4) 30%,
            rgba(20, 20, 20, 0.3) 50%,
            rgba(20, 20, 20, 0.4) 70%,
            rgba(20, 20, 20, 0.7) 95%,
            rgba(0, 0, 0, 0.9) 100%
          ), url(../assets/hotel5.jfif);
        background-size: cover;
      }
.background-gradation {
  position: absolute;
  width: 100%;
  height: 951px;
  left: 0px;
  bottom: 0px;

  background: linear-gradient(
            to bottom,
            rgb(0, 0, 0, 0) 0%,
            rgba(20, 20, 20, 0.0) 5%,
            rgba(20, 20, 20, 0) 50%,
            rgba(20, 20, 20, 0.4) 90%,
            rgba(0, 0, 0, 1) 100%
          );  
  background-size: inherit;
  }

select {
  -moz-appearance: none;
  -webkit-appearance: none;
  appearance: none;

  position: absolute;
  right:40px;
  top: -45px;
  width: 120px;
  height: 35px;

  background: #5C5C5C;
  border-radius: 10px;
  outline: none;
  border: none;
  
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 600;
  font-size: 13px;
  line-height: 20px;
  text-align: center;

  color: #FFFFFF;
  letter-spacing:1.5px
}
option {
  background-color: black;
  font-size: 14px;
}

li{
  list-style-type: none;
}

/* ????????? ????????? ????????? ?????? ?????? */
#slideShow{
  width: 100%;
  height: 100%;
  position: relative;
  overflow: hidden;
  display: flex;
  /*????????? ???????????? ???????????? ????????? 
  ????????? ????????? ?????????, 500px ????????? ?????? ?????? ???????????????
  hidden?????? ???????????????*/
}


.slides{
  position: absolute;
  display: inline-block;
  left: 0;
  top: 0;
  width: 15000px; /* ??????????????? ????????? ?????? ??? ?????? */
  height: 100%;
  transition: left 0.5s ease-out; 
  /*ease-out: ???????????? ???????????? ?????? ?????????*/
}

/* ??? ?????? ???????????? ???????????? ??????????????????
????????? ??????????????? margin-left?????? */
.slides li:first-child{
  margin-left: 30px;
}

/* ??????????????? ????????? ?????? */
.slides li:not(:last-child){
  float: left;
  margin-right: 10px;
}

.slides li{
  float: left;
}

.controller span{
  position:absolute;
  background-color: transparent;
  color: rgb(226, 226, 226);
  text-align: center;
  border-radius: 50%;
  padding: 10px 20px;
  top: 50%;
  font-size: 1.3em;
  cursor: pointer;
}

/* ??????, ?????? ???????????? ????????? ????????? ????????? ????????? */
.controller span:hover{
  background-color: rgba(188, 188, 188, 0.11);
}

.prev{
  left: 10px;
  color: white;
}

/* ?????? ???????????? ????????? ????????? ????????? ????????? 
?????? ???????????? ?????? ???????????? ???????????? ??????*/
.prev:hover{
  transform: translateX(-10px);
}

.next{
  right: 10px;
}

/* ?????? ???????????? ????????? ????????? ????????? ????????? 
?????? ???????????? ?????? ??????????????? ???????????? ??????*/
.next:hover{
  transform: translateX(10px);
}
</style>
