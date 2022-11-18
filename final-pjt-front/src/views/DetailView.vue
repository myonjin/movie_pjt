<template>
  <div style="margin-top:60px;">
    <!-- <img class="bakcimage" :src="`https://mage.tmdb.org/t/p/w1280/rl7Jw8PjhSIjArOlDNv0JQPL1ZV.jpg`" alt="hotel" style="width:100%"> -->
    <div id='show1'>
      <div style="width:40%">
        <h1>{{movieDetail?.title}}</h1>
        <p>{{movieDetail?.overview}}</p>
        <p style="font-family:'Montserrat';font-style: normal;font-weight: 600;font-size: 18px;line-height: 22px;color: #FF2E00;">GENRES</p>
        <p>{{movieDetail?.genre}}</p>
      </div>
      <div style="width:40%">
        <button class="pinkBtn">WATCH</button>
        <button class="grayBtn">MY LIST</button>
      </div>
    </div>
    <p>비슷한 영화</p>
    <div class="d-flex flex-row">
      <movieSimilarListItem 
        v-for="similar in movieSimilar" :key="similar.id" :similar="similar"
      />
    </div>
    
    <p>{{movieDetail}}</p>
  </div>
</template>

<script>
import axios from 'axios'
import MovieSimilarListItem from '@/components/MovieSimilarListItem.vue'
export default {
  name:'DetailView',
  components: {
    MovieSimilarListItem
  },
  data(){
    return {
      movieId: this.$route.params.id,
      movieDetail: null,
      movieSimilar: null,
    }
  },
  created(){
    axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/detail/${this.movieId}`,
        })
          .then((res) => {
          this.movieDetail = res.data
          })
          .catch((err) => {
            console.log(err)
          })
    axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.movieId}/similar?api_key=8513510776c862bf8d57bb36d072f05e&language=ko-KR&page=1`,
        })
          .then((res) => { 
            // console.log(res.data.results)
            this.movieSimilar = res.data.results
          })
          .catch((err) => {
            console.log(err)
          })
  },
}
</script>

<style>
#show1 {
    background-image:
    linear-gradient(to left, rgba(255, 255, 255, 0), rgba(24, 23, 23, 0.73)),
    url('https://image.tmdb.org/t/p/w1280/rl7Jw8PjhSIjArOlDNv0JQPL1ZV.jpg');
    width: 100%;
    height: 400px;
    background-size: cover;
    color: white;
    padding: 20px;
}
h1 {
font-family: 'Montserrat';
font-style: normal;
font-weight: 600;
font-size: 16px;
line-height: 20px;

color: #FFFFFF;
}
p {
  font-family: 'Montserrat';
font-style: normal;
font-weight: 600;
font-size: 16px;
line-height: 20px;

color: #FFFFFF;
}

</style>