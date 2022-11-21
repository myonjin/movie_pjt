<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>
    <button class="like-btn" :style="is_liked ? 'color:red;' : 'color:white;'" @click="likeBtn">❤</button>
    <p>{{liked_count}}</p>
    <!-- <p>{{commentList}}</p> -->
    <ArticleCommentListItem v-for="comment in commentList" :key="comment.id" :comment="comment"/>
    <div>
      <input v-model.trim="commentContent" @keyup.enter="commentCreate">
      <button @click="commentCreate">생성</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ArticleCommentListItem from '@/components/ArticleCommentListItem'
const API_URL = 'http://127.0.0.1:8000'
export default {
  name:'ArticleDetailView',
  components:{
    ArticleCommentListItem
  },
  data(){
    return{
        article:null,
        is_liked:false,
        liked_count:null,
        commentList:null,
        commentContent:null,
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
    commentCreate(){
      // console.log(this.commentContent)
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/${this.article.id}/comments/`,
        data:{
          content: this.commentContent,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
      .then((res)=> {
        console.log(res.data)
      
      this.commentList.push({
        id:res.data.id,
        content:res.data.content,
        username:res.data.username,
      })
        
      })
      this.commentContent=null

    }
    ,
    getArticleDetail(){
        axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}`
      })
        .then((res) => {
          // console.log(res.data)
          this.article = res.data
          this.liked_count= res.data.like_users.length
          if (res.data.like_users.includes(this.$store.state.user.id)){
            this.is_liked=true
          } else {
            this.is_liked=false
          }
          this.commentList=res.data.comment_set
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
        .then(()=>{
            // console.log(res.data);
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