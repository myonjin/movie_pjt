
<template>
  <div class=" " style="margin-top:60px; height: 100vh;">
    <!-- <h1>영화 정보 검색 </h1>
    <b-form @submit.prevent="onSearch">
        <b-form-input class="border-black" v-model="keyword" placeholder="영화 제목을 입력하세요."></b-form-input>
    </b-form> -->
    <h1 id="no-result" style="visibility:hidden; position:absolute; top:350px;left:50%; transform:translateX(-50%); color:#E8E8E8;">검색 결과가 없어요 :(</h1>
    <div v-if="this.movieList" class="d-flex flex-wrap align-content-around" style="width:80%; height:80vh; margin:auto;">
      <MovieListItem
        v-for="movie in movieList" :key="movie.id" :movie="movie"
      />      
    </div>
  </div>
</template>

<script>
import MovieListItem from '../components/MovieListItem.vue'
import axios from 'axios'



export default {
  name:'AboutView',
  components:{
    MovieListItem,
  },
  data () {
  return {
    movieList: null,
    }
  },
  methods:{

  },
  computed: {
  },
  created() {
    axios({
          method:'get',
          url:`https://api.themoviedb.org/3/search/movie?api_key=6aff6c96fa8121c83d1a49c01d1407b3&language=ko-KR&query=${this.$route.params.keyword}&page=1&include_adult=false`
        })
        .then((res)=>{
          this.movieList=res.data.results
          if (res.data.results.length<1) {
            const noResult = document.querySelector('#no-result')
            noResult.style.visibility = 'visible'
            noResult.style.height = '0px'
          }
        })
        .catch((err)=>{
          console.log(err)
        })
  }
}
</script>
<style>

</style>