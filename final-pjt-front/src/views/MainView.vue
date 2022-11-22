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
    top: 610px;
  
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
          ), url(../assets/hotel.jpg);
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
  position: absolute;
  right:40px;
  top: -45px;
  width: 120px;
  height: 35px;

  background: #5C5C5C;
  border-radius: 30px;

  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 600;
  font-size: 13px;
  line-height: 20px;
  text-align: center;

  color: #FFFFFF;
  letter-spacing:1.5px
}

li{
  list-style-type: none;
}

/* 보여줄 구간의 높이와 넓이 설정 */
#slideShow{
  width: 100%;
  height: 100%;
  position: relative;
  overflow: hidden;
  display: flex;
  /*리스트 형식으로 이미지를 일렬로 
  정렬할 것이기 때문에, 500px 밖으로 튀어 나간 이미지들은
  hidden으로 숨겨줘야됨*/
}


.slides{
  position: absolute;
  display: inline-block;
  left: 0;
  top: 0;
  width: 15000px; /* 슬라이드할 사진과 마진 총 넓이 */
  height: 100%;
  transition: left 0.5s ease-out; 
  /*ease-out: 처음에는 느렸다가 점점 빨라짐*/
}

/* 첫 번째 슬라이드 가운데에 정렬하기위해
첫번째 슬라이드만 margin-left조정 */
.slides li:first-child{
  margin-left: 30px;
}

/* 슬라이드들 옆으로 정렬 */
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

/* 이전, 다음 화살표에 마우스 커서가 올라가 있을때 */
.controller span:hover{
  background-color: rgba(188, 188, 188, 0.11);
}

.prev{
  left: 10px;
  color: white;
}

/* 이전 화살표에 마우스 커서가 올라가 있을때 
이전 화살표가 살짝 왼쪽으로 이동하는 효과*/
.prev:hover{
  transform: translateX(-10px);
}

.next{
  right: 10px;
}

/* 다음 화살표에 마우스 커서가 올라가 있을때 
이전 화살표가 살짝 오른쪽으로 이동하는 효과*/
.next:hover{
  transform: translateX(10px);
}
</style>
