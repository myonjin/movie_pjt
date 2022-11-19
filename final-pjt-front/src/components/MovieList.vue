<template>
  <div class="d-flex flex-column" style="height:100%; position:relative;">
    <p class="popular_text">전체 영화</p>
    
    <!-- <div class="d-flex flex-row" style="position: relative;"> -->
    <select v-model="filterList" style="top:10px;">
      <option value="default" selected disabled hidden>FILTERS</option>
      <option value="random">랜덤</option>
      <!-- <option value="default">default</option> -->
      <option value="vote">평점순</option>
      <option value="popularity">인기순</option>
      <option value="new">신작순</option>
      <option value="old">구작순</option>
    </select>
    <div id="slideShow">
      <ul class="slides">
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
    <!-- </div> -->
  </div>


</template>

<script>
import axios from 'axios'
import MovieListItem from '@/components/MovieListItem'
export default {
  name: 'MovieList',
  components: {
    MovieListItem
  },
  data() {
    return {
      movieList : null,
      filterList: null,
      currentIdx: 0,
    }
  },
  methods: {
    getTotalMovieList(filter) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/totalmovielist/${filter}`,
        // 권한이 필요한 요청은 token 붙여서 보내자
        // headers: {
        //   Authorization: `Token ${context.state.token}`
        // }
        })
          .then((res) => {
            
            this.movieList = res.data
          })
          .catch((err) => {
            console.log(err)
          })
    },
    prevBtn() {
      if (this.currentIdx !== 0) {
        this.moveSlide(this.currentIdx - 1)
      }
    },
    nextBtn() {
      const slideImg = document.querySelectorAll('.slides li')
      const slideCount = slideImg.length
      if (this.currentIdx !== slideCount - 1) {
        this.moveSlide(this.currentIdx + 1);
      }
    },
    moveSlide(num) {
      const slides = document.querySelector('.slides')
      slides.style.left = -num * 800 + 'px';
      this.currentIdx = num;
    }

  },
  watch: {
    filterList: function (val) {
      this.getTotalMovieList(val)
    }
  }
  ,
  // computed:{
  //   totalMovieList() {
  //     const filter = this.filterList
  //     // console.log(filter)
  //     this.getTotalMovieList(filter)
  //     // this.getTotalMovieList(filter)
  //     return 0
  //   }
  // },
  created() {
    this.filterList = 'default'
  }

}
</script>

<style>

</style>