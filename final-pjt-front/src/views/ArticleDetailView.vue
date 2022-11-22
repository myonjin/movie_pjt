<template>
  <div class="artdetailcontent mt-2" style="position:relative; min-width:320px; ">
    <section class="artdetailsection d-flex flex-column community_font" style="padding: 24px 32px 32px;">
      <p>글 번호 : {{ article?.id }}</p>
      <div class="d-flex justify-content-between">
        <p class="ms-5">{{ article?.title }}</p>
        <p class="me-5">{{ article?.created_at.substr(0,10)}}</p>
      </div>
      <div class="articlecontent">
        <div style="width:auto; height:400px;">
          <p>내용 : {{ article?.content }}</p>
        </div>
        <div class="" style="border:solid; border-color:blanchedalmond; width:100px; margin:auto;">
          <button class="like-btn mt-2" :style="is_liked ? 'color:red;' : 'color:white;'" @click="likeBtn">❤</button>
          <p>{{liked_count}}</p>
        </div>
        <br>
      </div>
      <!-- <p>{{commentList}}</p> -->
      <div class="d-flex flex-row justify-content-center">
        <Icon class="mt-1" icon="material-symbols:mode-comment-outline" style="color:blanchedalmond"/>
        <h5 class="ms-2">{{commentList.length}}</h5>
      </div>
      <ArticleCommentListItem v-for="comment in commentList" :key="comment.id" :comment="comment"/>
      <div class="mt-3">
        <input v-model.trim="commentContent" @keyup.enter="commentCreate">
        <button @click="commentCreate">생성</button>
      </div>
    </section>
  </div>
</template>

<script>
import { Icon } from '@iconify/vue2';
import axios from 'axios'
import ArticleCommentListItem from '@/components/ArticleCommentListItem'
const API_URL = 'http://127.0.0.1:8000'
export default {
  name:'ArticleDetailView',
  components:{
    ArticleCommentListItem,
    Icon,
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

.artdetailcontent{
    min-height: calc(100vh - env(safe-area-inset-bottom) - 56px);
    max-width: 700px;
    margin: 0 auto;
    padding-bottom: calc(env(safe-area-inset-bottom) + 56px);
    box-sizing: border-box;
  
}
.artdetailsection{
    margin: 56px 16px 0;
    margin: 0 auto;
    padding-bottom: 56px;
    background:#101322;
    min-height: calc(100vh - 56px);
    max-width: 668px;
    border-top-left-radius: 50px;
    border-top-right-radius: 50px;
}
</style>