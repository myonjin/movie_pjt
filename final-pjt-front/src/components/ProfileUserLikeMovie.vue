<template>
  <div style="height:450px; position:relative;">
    <div class="profile-user-like-movie-box">
      <div class="d-flex flex-column" style="height:100%; position:relative;">
        <p class="profile-user-like-movie-text">{{ username }}님이 좋아하는 영화</p>
        <div id="slideShow">
        <ul class="slides" id="slides-profile-like-movie">
          <li v-for="movie in movieList" :key="movie.id">
            <MovieListItem 
              :movie="movie"
              />
          </li>  
        </ul>
      </div>
      <p class="controller">
        <!-- &lang: 왼쪽 방향 화살표
        &rang: 오른쪽 방향 화살표 -->
        <span class="prev" @click="prevBtn">&lang;</span>  
        <span class="next" @click="nextBtn">&rang;</span>
      </p>
      </div>
  
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieListItem from "@/components/MovieListItem"

export default {
  name: 'ProfileUserLikeMovie',
  components: {
    MovieListItem,
  },
  props: {
    userId: Number,
  },
  data() {
    return {
      username: null,
      movieList: null,
      currentIdx: 0,
    }
  },
  methods: {
    prevBtn() {
      if (this.currentIdx !== 0) {
        this.moveSlide(this.currentIdx - 1)
      }
    },
    nextBtn() {
      const slideImg = document.querySelectorAll('#slides-profile-like-movie li')
      const slideCount = slideImg.length
      if (this.currentIdx !== slideCount - 1) {
        this.moveSlide(this.currentIdx + 1);
      }
    },
    moveSlide(num) {
      const slides = document.querySelector('#slides-profile-like-movie')
      slides.style.left = -num * 800 + 'px';
      this.currentIdx = num;
    }
  },
  created() {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/accounts/api/userlikemovie/${this.userId}/`,
    })
    .then((res) => {
      this.username = res.data.username
      this.movieList = res.data.movie_set
    })
  }

}
</script>

<style>
  .profile-user-like-movie-box{
    position: absolute;
    width: 92%;
    height: 428px;
    right: 0px;
    bottom: 0px;
  
    background: rgba(11, 15, 22, 0.47);
    box-shadow: 8px -8px 10px rgba(0, 0, 0, 0.25);
    backdrop-filter: blur(12.5px);
  
    border-radius: 24px 0px 0px 24px;
    }

  .profile-user-like-movie-text{
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
</style>