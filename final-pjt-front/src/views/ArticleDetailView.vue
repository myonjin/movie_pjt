<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>
    <button @click="likeBtn">{{like_hate}}</button>
    <p>{{liked_count}}</p>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  name:'ArticleDetailView',
  data(){
    return{
        article:null,
        is_liked:false,
        liked_count:null,
    }
  },
  created(){
    this.getArticleDetail()
    this.getCommentList()
    
  },
  computed:{
    like_hate(){
      if (this.is_liked){
        return '❤'
      } else {
        return '🤍'
      }
    }
  },
  methods:{
    getArticleDetail(){
        axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}`
      })
        .then((res) => {
          console.log(res.data)
          this.article = res.data
          this.liked_count= res.data.like_users.length
          if (res.data.like_users.includes(this.$store.state.user.id)){
            this.is_liked=true
          } else {
            this.is_liked=false
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getCommentList(){
        axios({
            method: 'get',
            url: `${API_URL}/api/v1/articles/comments/`
        })
        .then((res)=>{
            console.log(res.data);
        })
    },
    likeBtn(){
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/${this.article.id}/likes/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.is_liked=res.data.is_liked
        this.liked_count=res.data.liked_count
      })
    }
  }
}
</script>

<style>

</style>