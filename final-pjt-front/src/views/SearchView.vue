
<template>
  <div class=" " style="margin-top:60px">
    <h1>영화 정보 검색 </h1>
    <b-form @submit.prevent="onSearch">
        <b-form-input class="border-black" v-model="keyword" placeholder="영화 제목을 입력하세요."></b-form-input>
    </b-form>
    <div v-if="this.movieList" class="d-flex flex-wrap">
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
    keyword :"",
    movieList:"",
  }
  },

  methods:{
   
    onSearch(){
        if(!this.keyword){
            alert("영화 제목을 입력하세요!");
            this.keyword = ""
            return;
        }
        axios({
          method:'get',
          url:`https://api.themoviedb.org/3/search/movie?api_key=6aff6c96fa8121c83d1a49c01d1407b3&language=ko-KR&query=${this.keyword}}&page=1&include_adult=false`
        })
        .then((res)=>{
          this.movieList=res.data.results
          console.log(this.movieList)
       
          this.keyword = ""
        })
        .catch((err)=>{
          console.log(err)
        })

    }    
  }
}
</script>
<style>

</style>