<template>
  <div style="position:relative; top:0px; height:2000px;">
    <!-- <img class="bakcimage" :src="`https://mage.tmdb.org/t/p/w1280/rl7Jw8PjhSIjArOlDNv0JQPL1ZV.jpg`" alt="hotel" style="width:100%"> -->
    <div style="height:auto; position: relative; height: 657px;">
      <div id='show1' >
      </div>
      <!-- 배경 그라데이션 -->
      <div class="movie-detail-top-gradation">
  
      </div>
  
      <!-- 영화 정보 box -->
      <div class="movie-detail-box">
        <p class="release" style="font-size: 20px; font-weight: 700; line-height: 27px;" v-if="movieDetail?.release_date!==null">{{movieDetail?.release_date.slice(0, 4)}}</p>
        <h1 class="movie-detail-box-h1">{{ movieDetail?.title }}</h1>
        <p class="movie-detail-box-p">{{ movieDetail?.overview }}</p>
        <p class="movie-detail-box-genre">GENRES</p>
        <div class="d-flex flex-row justify-content-left">
          <p class="me-2 movie-detail-box-p" v-for="(genre,index) in movieDetail.genre" :key="index">{{genre.name}} </p>
        </div>
        <!-- 평점 및 개봉년도 -->
        <div class="d-flex" style="margin-bottom: 30px;">
          <img src="../assets/imdb_logo.png" class="me-2" style="width: 54px; height: 27px;">
          <p class="vote me-3" style="font-size: 20px; font-weight: 700; line-height: 27px;">{{ movieDetail?.vote_average.toFixed(1)}}</p>
        </div>
        <!-- 버튼 box -->
        <div class="d-felx flex-row" style="margin-bottom: 50px;">
          <button class="pinkBtn" style="width: 158px; height: 50px; font-size: 20px" @click="youtubeFullScreen(`https://www.youtube.com/embed/${youtubeSrc}`,$event)" value=" 창 열기 ">WATCH  ▶</button>
          <button class="grayBtn" style="width: 158px; height: 50px;">좋아요</button>
        </div>
        <!-- 리뷰 box -->
        <div style="height:500px; background-color: white;">
          <h1>리뷰</h1>
          <!-- 별점 box -->
          <div class="d-flex">
            <span class="star">
              ★★★★★
              <span>★★★★★</span>
              <input type="range" @change ="drawStar($event)" v-model="reviewScore" value="1" step="1" min="0" max="10">
            </span>
            <div>
              <input v-model.trim="reviewContent" placeholder="내용">
            </div>
            <button @click="reviewCreate">생성</button>
          </div>
          <div>
            <MovieReviewListItem v-for="(review,index) in movieReviewListc" :key="index" :review="review" 
            />
            <h1>작성된 리뷰가 없어요!!</h1>
          </div>
        </div>
      </div>

    </div>


    <!-- <div  class="review-box">
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
    </div> -->

    <div class="actor_box">
      <p class="popular_text">배우 목록</p>
      
      <div class="d-flex flex-row mt-4">
        <MovieActorItem 
          v-for="actor in actor_list" :key="actor.id" :actor="actor"
        />
      </div>
      
    </div>
   
  

    <!-- <div>
      <p class="popular_text">비슷한 영화</p>
      
      <div class="d-flex flex-row">
        <MovieSimilarListItem 
          v-for="similar in movieSimilar" :key="similar.id" :similar="similar"
        />
      </div>
    </div> -->
    
  </div>
</template>

<script>
import axios from 'axios'
// import MovieSimilarListItem from '@/components/MovieSimilarListItem.vue'
import MovieActorItem from '@/components/MovieActorItem.vue'
// import MovieReviewListItem from '@/components/MovieReviewListItem.vue'


export default {
  name:'DetailView',
  components: {
    // MovieSimilarListItem,
    MovieActorItem,
    // MovieReviewListItem
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
  drawStar(e) {
    const starTag = document.querySelector(`.star span`)
    starTag.style.width = `${e.target.value * 10}%`;
    console.log(this.reviewScore)
  },
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
    if (5>=Number(this.reviewScore)>=0){
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
    position: absolute;
    right: 0px;
    top: 0px;
    margin-left: auto;
    width: 80%;
    height: 657px;
    background-size: cover;
    color: white;
    padding: 20px;
 }
.movie-detail-top-gradation {
  box-sizing: border-box;

  position: absolute;
  width: 100%;
  height: 657px;
  left: 0px;
  top: 0px;

  background: linear-gradient(90deg, #000000 17.76%, rgba(0, 0, 0, 0.687449) 31.44%, rgba(196, 196, 196, 0) 100%) , linear-gradient(
            to bottom,
            rgb(0, 0, 0, 0) 0%,
            rgba(20, 20, 20, 0.0) 5%,
            rgba(20, 20, 20, 0) 50%,
            rgba(20, 20, 20, 0.4) 90%,
            rgba(0, 0, 0, 1) 100%
          );
  border: 1px solid #000000;
  filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
}
.movie-detail-box {
  position: absolute;
  top: 100px;
  width:35%;
  margin-left: 70px;
}
.movie-detail-box-h1 {
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 600;
  line-height: 50px;
  font-size: 40px;
  margin-bottom: 40px;
  text-align: left;

  color: #FFFFFF;
}
.movie-detail-box-p {
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 25px;
  text-align: left;

  color: #FFFFFF;

}
.movie-detail-box-genre {
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 600;
  font-size: 23px;
  text-align: left;
  margin-bottom: 0px;
  margin-top: 30px;

  color: #FF2E00;

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

  .star {
    position: relative;
    font-size: 2rem;
    color: #ddd;
  }
  
  .star input {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0;
    opacity: 0;
    cursor: pointer;
  }
  
  .star span {
    width: 0;
    position: absolute; 
    left: 0;
    color: red;
    overflow: hidden;
    pointer-events: none;
  }

</style>