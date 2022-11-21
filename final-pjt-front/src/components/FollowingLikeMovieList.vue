<template>
  <div class="d-flex flex-column" style="height:100%; position:relative;">
    <div class="d-flex align-items-center" style="margin-bottom: 15px;">
      <img class="follow-user-image" :src="`http://127.0.0.1:8000${profileImg}`" alt="">
      <p class="following-like-movie-text"><span>{{ followUsername }} </span>님이 좋아하는 영화입니다.</p>
    </div>
    <div id="slideShow">
      <ul class="slides" id="slides-follow-like-movie">
        <li v-for="movie in movieList" :key="movie.id">
          <MovieListItem 
            :movie="movie"
          />
        </li>  
      </ul>
    <!-- </div> -->
    </div>
    <p class="controller">
      <!-- &lang: 왼쪽 방향 화살표
      &rang: 오른쪽 방향 화살표 -->
      <span class="prev" @click="prevBtn">&lang;</span>  
      <span class="next" @click="nextBtn">&rang;</span>
    </p>
  
  </div>
  
</template>

<script>
import axios from 'axios'
import _ from 'lodash'
import MovieListItem from './MovieListItem.vue'

export default {
  name: 'FollowingLikeMovieList',
  components: {
    MovieListItem,
  },
  data() {
    return {
      followUsername: null,
      movieList: null,
      profileImg: '/media/users/default.png',
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
      const slideImg = document.querySelectorAll('#slides-follow-like-movie li')
      const slideCount = slideImg.length
      if (this.currentIdx !== slideCount - 1) {
        this.moveSlide(this.currentIdx + 1);
      }
    },
    moveSlide(num) {
      const slides = document.querySelector('#slides-follow-like-movie')
      slides.style.left = -num * 800 + 'px';
      this.currentIdx = num;
    }
  },
  created() {
    const userId = _.sample(this.$store.state.user.following);
    console.log(userId);
    axios({
      methods: 'get',
      url: `http://127.0.0.1:8000/accounts/api/userlikemovie/${userId}/`
    })
    .then((res) => {
      this.followUsername = res.data.username
      this.movieList = res.data.movie_set
      console.log(res.data.profile_img_src);
      if (res.data.profile_img_src !== null) {
        this.profileImg = res.data.profile_img_src
      }
    })
  }
}
</script>

<style>
.follow-user-image {
  width: 60px;
  height: 60px;
  margin: 20px;
  border: 1px solid #FFFFFF;
  border-radius: 5px;
}
</style>