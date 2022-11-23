<template>
  <div class="ms-4" v-if="movie.poster_path">
    <img @click="goDetail()" class="poster" :src="`https://image.tmdb.org/t/p/w400/${movie.poster_path}`" alt="">
    <p @click="goDetail()" class="title">{{movie.title}}</p>
    <p @click="goDetail()" class="release" v-if="movie.release_date!==null">{{movie.release_date.slice(0, 4)}}</p>
    <div class="d-flex justify-content-between align-items-center">
      <div @click="goDetail()" class="d-flex">
        <img src="../assets/imdb_logo.png" alt="" style="width: 28px; height: 14px;">
        <p class="vote">{{ movie.vote_average.toFixed(1) }}</p>
      </div>
      <!-- 임시!! 좋아요기능 구현 후 버튼넣을거임 -->
      <button class="like-btn" @click="likeMovie" :name="`like-btn-${movie.id}`">❤</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  },
  data() {
    return {
      isLiked: null,
    }
  },
  methods:{
    goDetail(){
      this.$router.push({name:'detail', params:{id : this.movie.id}})
    },
    likeMovie() {
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/movies/like/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          movie_id: this.movie.id,
        }
      })
      .then((res) => {
        this.isLiked = res.data['is_liked']
      })
    }
  },
  created() {
    console.log(this.movie);
    if (this.movie.like_users.includes(this.$store.state.user.id)) {
      this.isLiked = true
    } else {
      this.isLiked = false
    }
  },
  watch: {
    isLiked() {
      const likeBtn = document.querySelectorAll(`button[name=like-btn-${this.movie.id}]`)
      if (this.isLiked === true) {
        likeBtn.forEach((tag) => tag.style.color = 'red')
      } else {
        likeBtn.forEach((tag) => tag.style.color = 'white')
      }
    }
  }
}
</script>

<style>
.poster {
  width:150px;
  height:225px;
  border-radius: 7px;
}
.title {
  width: 150px;
  margin-top: 8px;
  margin-bottom: 8px;
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  line-height: 20px;
  /* identical to box height */
  overflow: hidden;
  white-space: nowrap;
  text-align: left;
  text-overflow: ellipsis;

  color: #FFFFFF;
  }
.release {
  margin-bottom: 5px;
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 700;
  font-size: 11px;
  line-height: 13px;
  text-align: left;

  color: #AFAFAF;
}
.vote {
  margin-left: 4px;
  margin-bottom: 0px;
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 700;
  font-size: 14px;
  line-height: 13px;

  color: #FFC907;
  }

.like-btn {
  border: none;
  background: none;
  color: white;
  line-height: -20px;
}
</style>