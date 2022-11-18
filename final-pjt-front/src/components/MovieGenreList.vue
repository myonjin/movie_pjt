<template>
  <div class="d-flex flex-column">
    <div>
      <p class="genre_text">어떤 장르를 좋아하세요?</p>
    </div>
    <div>
      <button
        v-for="genre in genreList"
        :key="genre.id"
        @click="addGenreFilter(genre.id)"
      >
      {{genre.name}}</button>
    </div>
    <select v-model="filterList" style="position: absolute;width: 139px;height: 40px;right:0px;top: 0px;">
      <option value="default" selected>랜덤</option>
      <!-- <option value="default">default</option> -->
      <option value="vote">평점순</option>
      <option value="popularity">인기순</option>
      <option value="new">신작순</option>
      <option value="old">구작순</option>
    </select>
    <div class="d-flex">
      <MovieListItem 
        v-for="movie in genreMovieList" :key="movie.id" :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieListItem from '@/components/MovieListItem'

export default {
  name: 'MovieGenreList',
  components: {
    MovieListItem,
  },
  data() {
    return {
      genreMovieList : null,
      filterList: null,
      genreFilter: [],
      genreList: [
        {
          id: '12',
          name: '모험',
        },
        {
          id: '14',
          name: '판타지',
        },
        {
          id: '16',
          name: '애니메이션',
        },
      ],
    }
  },
  methods: {
    getGenreMovieList() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/genremovielist/${this.filterList}`,
        params: {
          id: this.genreFilter.join(',')
        }
        })
          .then((res) => {
            this.genreMovieList = res.data
          })
          .catch((err) => {
            console.log(err)
          })
    },
    addGenreFilter(add) {
      if (!this.genreFilter.includes(add)) {
        this.genreFilter.push(add)
      } else {
        this.genreFilter = this.genreFilter.filter((exist) => exist!==add )
      }
      console.log(this.genreFilter);
    }

  },
  watch: {
    filterList: function () {
      this.getGenreMovieList()
    },
    genreFilter: function () {
      this.getGenreMovieList()
    },
  },
  created() {
    this.filterList = 'default'
    this.genreFilter.push(12)
  }
}
</script>

<style>

</style>