<template>
  <div class="d-flex flex-column">
    <p class="popular_text">전체 영화</p>
    <select v-model="filterList" style="position: absolute;width: 139px;height: 40px;right:0px;top: 0px;">
      <option value="default" selected>랜덤</option>
      <!-- <option value="default">default</option> -->
      <option value="vote">평점순</option>
      <option value="popularity">인기순</option>
      <option value="new">신작순</option>
      <option value="old">구작순</option>
    </select>
    <div class="d-flex flex-row">
      <MovieListItem 
        v-for="movie in movieList" :key="movie.id" :movie="movie"
      />

    </div>

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
    }
  },
  methods: {
    getTotalMovieList(filter) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/totalmovielist/${filter}`,
        })
          .then((res) => {
            
            this.movieList = res.data
          })
          .catch((err) => {
            console.log(err)
          })
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