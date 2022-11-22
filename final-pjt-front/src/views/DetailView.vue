<template>
  <div>
    <!-- <img class="bakcimage" :src="`https://mage.tmdb.org/t/p/w1280/rl7Jw8PjhSIjArOlDNv0JQPL1ZV.jpg`" alt="hotel" style="width:100%"> -->
    
    <div id='show1' >
      <br>
      <div class="mt-5 " style="width:40%">
        <h1>{{movieDetail?.title}}</h1>
        <p>{{movieDetail?.overview}}</p>
        <p class="genre_red">
          GENRES</p>
        <div class="d-flex flex-row justify-content-center">
          <p class="ms-2" v-for="(genre,index) in movieDetail.genre" :key="index">{{genre.name}} /</p>
        </div>
      </div>
      <div style="width:40%">
        <button class="pinkBtn" @click="youtubeFullScreen(`https://www.youtube.com/embed/${youtubeSrc}`,$event)" value=" 창 열기 ">WATCH</button>
        <button class="grayBtn">MY LIST</button>
      </div>
    </div>
    
    <div class="actor_box">
      <p class="popular_text">배우 목록</p>
      
      <div class="d-flex flex-row">
        <MovieActorItem 
          v-for="actor in actor_list" :key="actor.id" :actor="actor"
        />
      </div>
      
    </div>
    <p>{{movieDetail}}</p>
    
  <div  class="review-box">
    <div>
      <MovieReviewListItem v-for="(review,index) in movieReviewListc" :key="index" :review="review" 
      />
      <h1>작성된 리뷰가 없어요!!</h1>
    </div>
    <div>
      <input v-model.trim="reviewContent" placeholder="내용">
      <input v-model.trim="reviewScore" placeholder="평점">
      <button @click="reviewCreate">생성</button>
    </div>
  </div>

    <div>
      <p class="popular_text">비슷한 영화</p>
      
      <div class="d-flex flex-row">
        <MovieSimilarListItem 
          v-for="similar in movieSimilar" :key="similar.id" :similar="similar"
        />
      </div>
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'
import MovieSimilarListItem from '@/components/MovieSimilarListItem.vue'
import MovieActorItem from '@/components/MovieActorItem.vue'
import MovieReviewListItem from '@/components/MovieReviewListItem.vue'


export default {
  name:'DetailView',
  components: {
    MovieSimilarListItem,
    MovieActorItem,
    MovieReviewListItem
},
  data(){
    return {
      movieId: this.$route.params.id,
      movieDetail: {"genre": [{"name": "모험"},]}, //비동기 에러 방지용
      movieSimilar: null,
      youtubeSrc:'jD5Yc2qMzBw', //임시로 넣어둠 if 로 방지할수있을듯 (console에러)
      actor_list:null,
      movieReviewList:null,
      reviewContent:null,
      reviewScore:null,
    }
  },
methods:{
    youtubeFullScreen(url){
    window.open(url,"","fullscreen,scrollbars")
  },
  getReviewList(){
    axios({
      method:'get',
      url:`http://127.0.0.1:8000/movies/detail/${this.movieId}`,
    })
    .then((res)=>{
      this.movieReviewList=res.data.reviews
    })
  },
  reviewCreate(){
    // const array1=["1","2","3","4","5"]
    // console.log(this.reviewScore)
    if (5>=Number(this.reviewScore) && Number(this.reviewScore)>=1){
      console.log(Number(this.reviewScore))
      console.log('참')
      axios({
        method:'post',
        url:`http://127.0.0.1:8000/movies/detail/${this.movieId}/review/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data:{
          content:this.reviewContent,
          score:this.reviewScore,
        },
      })
      .then(()=>{
        this.getReviewList()
      })
      this.reviewContent=null
      this.reviewScore=null
    }else{
      // console.log(22)
      alert('평점은 1~5사이숫자만가능^^')
      this.reviewContent=null
      this.reviewScore=null
    }
  } 
    ,
  },
  computed:{
    movieReviewListc() {
      this.movieReviewList
      return this.movieReviewList
    },
  },
  created(){
    axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/detail/${this.movieId}`,
        })
          .then((res) => {
          this.movieDetail = res.data
          this.movieReviewList = this.movieDetail.reviews
          // console.log(this.movieReviewList)
          // // console.log(this.movieDetail.actor)
          //   console.log(typeof(this.movieDetail.actor))
          //   const json = `[1083010,LetitiaWright,/i6fbYNn5jWA6swWtaqgzaj02RMc.jpg]`
          //   // const json = this.movieDetail.actor
          //   const obj = JSON.parse((json));
            // console.log(obj);
            let movies = this.movieDetail.actor
            let cnt = 0
            movies=movies.split(",")
            var actor_list=new Array()
            var actor_index=new Array()
            for (let ac of movies){
              // console.log(ac);
              ac=ac.trim()              
              ac=ac.replace(/\[/,"")
              ac=ac.replace(/"/g,"")
              ac=ac.replace(/'/g,"")
              ac=ac.replace(/\[/,"")
              ac=ac.replace(/\//,"")
              ac=ac.replace(/\]/,"")
              ac=ac.replace(/\]/,"")
              cnt =cnt + 1
              if (cnt===3){
                actor_index.push(ac)
                actor_list.push(actor_index)
                actor_index=new Array()
                cnt=0
              } else {
                actor_index.push(ac)
              }
            }
            // console.log(actor_list)
            this.actor_list=actor_list
            // console.log(movies);
          })
          .then(()=>{
          document.getElementById("show1").style.backgroundImage = 
          `linear-gradient(to left, rgba(255, 255, 255, 0), rgba(24, 23, 23, 0.73)), 
          url('https://image.tmdb.org/t/p/original${this.movieDetail.backdrop_path}')`;
          })
          .catch((err) => {
            console.log(err)
          })

    //비슷한 취향의 영화 추천
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
          
    //유튜브 영상 아이디 값 가져오기
    axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.movieId}/videos?api_key=6aff6c96fa8121c83d1a49c01d1407b3&language=ko-KR`,
        })
          .then((res) => { 
            if (res.data.results[0]){
              this.youtubeSrc = res.data.results[0].key
            } else {
              this.youtubeSrc = ''
            
          }})
          .catch((err) => {
            console.log(err)
          })
        },

      
}
</script>

<style>
#show1 {
    /* background-image:
    linear-gradient(to left, rgba(255, 255, 255, 0), rgba(24, 23, 23, 0.73)),
    url('https://image.tmdb.org/t/p/original/rl7Jw8PjhSIjArOlDNv0JQPL1ZV.jpg'); */
    width: 100%;
    height: 500px;
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
h2{
  font-family: 'Montserrat';
font-style: normal;
font-weight: 600;
font-size: 16px;
line-height: 20px;
color: #FFFFFF;
}
h3{
  
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
.genre_red{
  font-family:'Montserrat';   
        font-style:normal;
        font-weight:600;
        font-size: 18px;
        line-height: 22px;color: #FF2E00;
}
.review-box{
    width: 90%;
    right: 0px;
    bottom: 0px;
  
    background: rgba(11, 15, 22, 0.47);
    box-shadow: 8px -8px 10px rgba(0, 0, 0, 0.25);
    backdrop-filter: blur(12.5px);
    /* Note: backdrop-filter has minimal browser support */
  
    border-radius: 24px 0px 0px 24px;
    }  

</style>