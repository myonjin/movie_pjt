<template>
  <div style="position:relative; top:0px; height:1400px;">
    <!-- <img class="bakcimage" :src="`https://mage.tmdb.org/t/p/w1280/rl7Jw8PjhSIjArOlDNv0JQPL1ZV.jpg`" alt="hotel" style="width:100%"> -->
    <div style="height:auto; position: relative; height: 657px;">
      <div id='show1' >
      </div>
      <!-- 예고편 유튜부 -->
      <iframe
      id="ytplayer"
      width="80%"
      height="653px"
      align="right"
      type="text/html"
      allowfullscreen=""
      frameborder="0"></iframe>
      <!-- 배경 그라데이션 -->
      <div class="movie-detail-top-gradation">
  
      </div>
  
      <!-- 영화 정보 box -->
      <div class="movie-detail-box">
        <p class="release" style="font-size: 20px; font-weight: 700; line-height: 27px;" v-if="movieDetail?.release_date!==null">{{movieDetail?.release_date?.slice(0, 4)}}</p>
        <h1 class="movie-detail-box-h1">{{ movieDetail?.title }}</h1>
        <p class="movie-detail-box-p">{{ movieDetail?.overview }}</p>
        <p class="movie-detail-box-genre">GENRES</p>
        <div class="d-flex flex-row justify-content-left">
          <p class="me-2 movie-detail-box-p" v-for="(genre,index) in movieDetail.genre" :key="index">#{{genre.name}} </p>
        </div>
        <!-- 평점 및 개봉년도 -->
        <div class="d-flex" style="margin-bottom: 30px;">
          <img src="../assets/imdb_logo.png" class="me-2" style="width: 54px; height: 27px;">
          <p class="vote me-3" style="font-size: 20px; font-weight: 700; line-height: 27px;">{{ movieDetail?.vote_average?.toFixed(1)}}</p>
        </div>
        <!-- 버튼 box -->
        <div class="d-felx flex-row align-items-center" style="margin-bottom: 90px; height:54.5px; position:relative;">
          <!-- <button class="pinkBtn" style="width: 158px; height: 50px; font-size: 20px" @click="youtubeFullScreen(`https://www.youtube.com/embed/${youtubeSrc}`,$event)" value=" 창 열기 ">Trailler  ▶</button> -->
          <button id="ytplaybtn" v-if="youtubeSrc!==null" class="pinkBtn" style="width: 158px; height: 54.5px; font-size: 20px; position:absolute; top:0px; left:0px;" @click="youtubePlay()">Trailer  ▶</button>
          <button id="detaillikebtn" @click="likeMovie" class="like-btn" style="font-size: 35px; margin:auto; position:absolute; top:0px; left:170px;">❤</button>
        </div>
        <!-- 리뷰 box -->
        <div style="height:500px;">
          <h1 class="movie-detail-box-h1">User Review</h1>
          <!-- 별점 box -->
          <div class="d-flex flex-column" style="height:100px;">
            <div class="d-flex justify-contents-left">
              <span class="star">
                ★★★★★
                <span>★★★★★</span>
                <input type="range" @change ="drawStar($event)" v-model="reviewScore" value="1" step="1" min="0" max="10">
              </span>
              <p class="user-score" style="line-height:55px; margin-left:5px; margin-right: auto;">{{ reviewScore }}</p>

            </div>

            <div>
              <input class="review-input" v-model.trim="reviewContent" placeholder="이 영화의 한줄평을 입력해주세요!">
              <button id="reviewbtn" class="review-btn" @click="reviewCreate">생성</button>
            </div>

          </div>
          <div>
            <MovieReviewListItem v-for="(review,index) in movieReviewListc" :key="index" :review="review" 
            />
            <!-- <h1>작성된 리뷰가 없어요!!</h1> -->
          </div>
        </div>
      </div>
    </div>
    <!-- 출연진 정보 -->
    <div class="actor_box">
      <p class="popular_text">CAST</p>
      <div id="slideShow">
      <ul class="slides" id="slides-actor">
        <li v-for="actor in actor_list?.slice(0,100)" :key="actor.id">
          <MovieActorItem 
          :actor="actor"
            />
          </li>  
        </ul>
      </div>
      <p class="controller">
        <!-- &lang: 왼쪽 방향 화살표
        &rang: 오른쪽 방향 화살표 -->
        <span class="prev" @click="prevBtnActor">&lang;</span>  
        <span class="next" @click="nextBtnActor">&rang;</span>
      </p>
      
    </div>
    <!-- 비슷한 영화 -->
    <div class="similar_box">
      <p class="popular_text">SIMILAR MOVIES</p>
      <div id="slideShow">
        <ul class="slides" id="slides-similar">
          <li v-for="similar in movieSimilar" :key="similar.id">
            <MovieSimilarListItem
            :similar="similar"
            />
          </li>  
        </ul>
      </div>
      <p class="controller">
        <!-- &lang: 왼쪽 방향 화살표
        &rang: 오른쪽 방향 화살표 -->
        <span class="prev" @click="prevBtnSimilar">&lang;</span>  
        <span class="next" @click="nextBtnSimilar">&rang;</span>
      </p>
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
      youtubeSrc:null, //임시로 넣어둠 if 로 방지할수있을듯 (console에러)
      actor_list:null,
      movieReviewList:null,
      reviewContent:null,
      reviewScore:0,
      isYtPlaying: 0,
      isLiked: null,
      currentIdxActor: 0,
      currentIdxSimilar: 0,
    }
  },
methods:{
  likeMovie() {
    axios({
      method: 'put',
      url: `http://127.0.0.1:8000/movies/like/`,
      headers: {
        Authorization: `Token ${this.$store.state.token}`
      },
      data: {
        movie_id: this.movieDetail.id,
      }
    })
    .then((res) => {
      this.isLiked = res.data['is_liked']
    })
  },
  drawStar(e) {
    const starTag = document.querySelector(`.star span`)
    starTag.style.width = `${e.target.value * 10}%`;
  },
  youtubePlay() {
    const btn = document.querySelector('#ytplaybtn')
    const iframeTag = document.querySelector('#ytplayer')
    const backImg = document.querySelector('#show1')
    if (this.isYtPlaying === 0) {
      backImg.style.visibility = 'hidden'
      iframeTag.src= `https://www.youtube.com/embed/${this.youtubeSrc}?autoplay=1&mute=1&loop=1`
      btn.innerText = 'Stop  ■'
      this.isYtPlaying = 1
    } else {
      backImg.style.visibility = 'visible'
      btn.innerText = 'Trailer  ▶'
      this.isYtPlaying = 0
    }
  },
  // youtubeFullScreen(url){
  //   window.open(url,"","fullscreen,scrollbars")
  // },
  getReviewList(){
    axios({
      method:'get',
      url:`http://127.0.0.1:8000/movies/detail/${this.movieId}`,
    })
    .then((res)=>{
      this.movieReviewList = res.data.reviews

    })
  },
  reviewCreate(){
    // const array1=["1","2","3","4","5"]
    // console.log(this.reviewScore)
    if (10>=Number(this.reviewScore) && Number(this.reviewScore)>=0){

      axios({
        method:'post',
        url:`http://127.0.0.1:8000/movies/detail/${this.movieId}/review/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data:{
          content:this.reviewContent,
          score:Number(this.reviewScore),
        },
      })
      .then(()=>{
        this.getReviewList()
      })
      this.reviewContent=null
      this.reviewScore=null
    }else{
      // console.log(22)
      alert('평점은 1~10사이숫자만가능^^')
      this.reviewContent=null
      this.reviewScore=null
      }
    },
    prevBtnActor() {
      if (this.currentIdxActor !== 0) {
        this.movieSlideActor(this.currentIdxActor - 1)
      }
    },
    nextBtnActor() {
      const slideImg = document.querySelectorAll('#slides-actor li')
      const slideCount = slideImg.length
      if (this.currentIdxActor !== slideCount - 1) {
        this.movieSlideActor(this.currentIdxActor + 1);
      }
    },
    movieSlideActor(num) {
      const slides = document.querySelector('#slides-actor')
      slides.style.left = -num * 800 + 'px';
      this.currentIdxActor = num;
    },
    prevBtnSimilar() {
      if (this.currentIdxSimilar !== 0) {
        this.movieSlideSimilar(this.currentIdxSimilar - 1)
      }
    },
    nextBtnSimilar() {
      const slideImg = document.querySelectorAll('#slides-similar li')
      const slideCount = slideImg.length
      if (this.currentIdxSimilar !== slideCount - 1) {
        this.movieSlideSimilar(this.currentIdxSimilar + 1);
      }
    },
    movieSlideSimilar(num) {
      const slides = document.querySelector('#slides-similar')
      slides.style.left = -num * 800 + 'px';
      this.currentIdxSimilar = num;
    }
  },
  watch: {
    movieReviewList() {
      const isMyRiviewExist = this.movieReviewList.some((review) => review.user.id === this.$store.state.user.id)
      if (isMyRiviewExist) {
        const reviewBtn = document.querySelector('#reviewbtn')
        reviewBtn.innerText = '수정'
      }
    },
    isLiked() {
      const likeBtn = document.querySelectorAll(`#detaillikebtn`)
      if (this.isLiked === true) {
        likeBtn.forEach((tag) => tag.style.color = 'red')
      } else {
        likeBtn.forEach((tag) => tag.style.color = 'white')
      }
    }
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
            let movies = this.movieDetail.actor
            let cnt = 0
            movies=movies.split(",")
            var actor_list=new Array()
            var actor_index=new Array()
            for (let ac of movies){
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
            this.actor_list=actor_list
          })
          .then(()=>{
            document.getElementById("show1").style.backgroundImage = 
            `linear-gradient(to left, rgba(255, 255, 255, 0), rgba(24, 23, 23, 0.73)), 
            url('https://image.tmdb.org/t/p/original${this.movieDetail.backdrop_path}')`;
            if (this.movieDetail.like_users.includes(this.$store.state.user.id)) {
              this.isLiked = true
            } else {
              this.isLiked = false
            }
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
              const likeBtn = document.querySelector('#detaillikebtn')
              likeBtn.style.left = '0px'
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

  background: linear-gradient(90deg, #000000 24.76%, rgba(0, 0, 0, 0.687449) 42.44%, rgba(196, 196, 196, 0) 100%) , linear-gradient(
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
  font-size: 35px;
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
    /* margin-left: 20px; */
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
    color: #FFC907;
    overflow: hidden;
    pointer-events: none;
  }
  .review-input {
    width: 85%;
    height: 50px;
    background-color: black;
    border-top: none;
    border-left: none;
    border-right: none;
    border-bottom : 3px solid white;
    outline: none;

    font-family: 'Montserrat';
    font-style: normal;
    font-weight: 400;
    font-size: 16px;
    line-height: 25px;
    text-align: left;

    color: #FFFFFF;
    }
  .review-btn {
    width: 15%;
    height: 49px;
    border-top: none;
    border-left: none;
    border-right: none;
    border-bottom : 3px solid white;
    background-color: black;
    font-weight: 700;
    color: #FF9999;
  }
  
</style>