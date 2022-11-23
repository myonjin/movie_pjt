<template>
  <div class="pb-5" style="height:450px; position:relative; background-color: black;">
    <div class="profile-user-review-movie-box">
      <div class="d-flex flex-column" style="height:100%; position:relative;">
        <!-- 제목 -->
        <div class="d-flex mb-4">
          <p class="profile-user-review-movie-text">{{ username }}님이</p>
          <span class="star-profile">
            ★★★★★
            <span>★★★★★</span>
            <input type="range" @change ="drawStar($event)" v-model="reviewScore" value="8" step="1" min="0" max="10">
          </span>
          <p class="profile-user-review-movie-text" style="margin-left:3px;">점 준 영화</p>
        </div>
        <div id="slideShow">
        <ul class="slides" id="slides-profile-review">
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
  name: 'ProfileUserReviewMovie',
  components: {
    MovieListItem,
  },
  props: {
    userId: Number,
    username: String,
  },
  data() {
    return {
      reviewScore: 8,
      movieList: null,
      currentIdx: 0,
    }
  },
  methods: {
    drawStar(e) {
    const starTag = document.querySelector(`.star-profile span`)
    starTag.style.width = `${e.target.value * 10}%`;
    this.getUserReviewMovie()
    },
    getUserReviewMovie() {
      axios({
        method: 'get',
        url:`http://127.0.0.1:8000/movies/userreviewmovielist/${this.userId}/${this.reviewScore}/`,
      })
      .then((res) => {
        this.movieList = res.data
      })
    },
    prevBtn() {
      if (this.currentIdx !== 0) {
        this.moveSlide(this.currentIdx - 1)
      }
    },
    nextBtn() {
      const slideImg = document.querySelectorAll('#slides-profile-review li')
      const slideCount = slideImg.length
      if (this.currentIdx !== slideCount - 1) {
        this.moveSlide(this.currentIdx + 1);
      }
    },
    moveSlide(num) {
      const slides = document.querySelector('#slides-profile-review')
      slides.style.left = -num * 800 + 'px';
      this.currentIdx = num;
   },
  },
  created() {
    this.getUserReviewMovie()
  }
}
</script>

<style>
  .profile-user-review-movie-box{
    position: absolute;
    width: 92%;
    height: 430px;
    right: 0px;
    bottom: 0px;
  
    background: rgba(11, 15, 22, 0.47);
    box-shadow: 8px -8px 10px rgba(0, 0, 0, 0.25);
    backdrop-filter: blur(12.5px);
  
    border-radius: 24px 0px 0px 24px;
    }

  .profile-user-review-movie-text{
    height: 22px;
    text-align: left;
    margin-top: 20px;
    margin-left: 20px;
    margin-right: 5px;
    font-family: 'Montserrat';
    font-style: normal;
    font-weight: 700;
    font-size: 18px;
    line-height: 22px;
    /* identical to box height */
    color: #FFFFFF;
    }

  .star-profile {
    position: relative;
    font-size: 2rem;
    color: #ddd;
    /* margin-left: 20px; */
  }
  
  .star-profile input {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0;
    opacity: 0;
    cursor: pointer;
  }
  
  .star-profile span {
    width: 80%;
    position: absolute; 
    left: 0;
    color: #FFC907;
    overflow: hidden;
    pointer-events: none;
  }
</style>