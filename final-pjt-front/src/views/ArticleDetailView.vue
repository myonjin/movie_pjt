<template>
  <div id="community" class="mt-2" style="color:#E8E8E8;">
    <div id="comcontent" style="padding: 30px;">
      <!-- 젤윗줄 -->
      <div class="d-flex justify-content-between align-items-center" style="margin: 20px 50px 10px 50px;">
        <!-- 제목 -->
        <h5>{{ article?.title }}</h5>
        <div class="d-flex align-items-center">
          <img class="article-detail-user-img me-2" :src="`http://127.0.0.1:8000${profileImg}`" onerror="this.src='http://127.0.0.1:8000/media/users/default.png'">
          <h6 class="commu-push mb-0 ms-1" style="width: 15%; cursor: pointer; font-size:20px;" @click="goProfile()">{{ article?.username }}</h6>
        </div>
      </div>
      <hr style="border: 2px solid #D0D0D5;">
      <!-- 내용 -->
      <p style="margin-bottom: 80px;">{{ article?.content }}</p>
      <!-- 좋아요 버튼 -->
      <div class="mb-5" style="border:solid; border-color:rgb(208, 208, 213); width:100px; margin:auto; padding: 10px;">
        <button class="like-btn mt-2" :style="is_liked ? 'color:red;' : 'color:white;'" @click="likeBtn">❤</button>
        <p>{{liked_count}}</p>
      </div>
      <!-- 댓글개수 -->
      <div class="d-flex flex-row justify-content-start align-items-center">
        <Icon class="m-2" icon="material-symbols:mode-comment-outline" style="color:white;"/>
        <p>{{ article?.comment_count}}개</p>
      </div>
      <hr style="border: 2px solid #D0D0D5;">
      <ArticleCommentListItem 
        v-for="comment in commentList" :key="comment.id" :comment="comment"
        @delete-comment="deleteComment"/>
      <!-- 댓글 입력폼 -->
      <div class="mt-3">
        <Icon class="m-2" icon="uil:pen" style="color:white;"/>
        <input class="review-input" style="background-color: #2a2b38; width:80%;" v-model.trim="commentContent" @keyup.enter="commentCreate">
        <button class="review-btn2" style="background-color: #2a2b38;" @click="commentCreate">생성</button>
      </div>
    </div>
  </div>
  <!-- <div class="artdetailcontent mt-2" style="position:relative; min-width:320px; ">
    <section class="artdetailsection d-flex flex-column community_font" style="padding: 24px 32px 32px;">
      <p>글 번호 : {{ article?.id }}</p>
      <div class="d-flex justify-content-between">
        <h5 class="ms-5">{{ article?.title }}</h5>
        <h5 class="me-5">{{ article?.created_at.substr(0,10)}}</h5>
      </div>
      <div class="articlecontent">
        <div style="width:auto; height:400px;">
          <h5
          >내용 : {{ article?.content }}</h5>
        </div>
        <div class="" style="border:solid; border-color:blanchedalmond; width:100px; margin:auto;">
          <button class="like-btn mt-2" :style="is_liked ? 'color:red;' : 'color:white;'" @click="likeBtn">❤</button>
          <p>{{liked_count}}</p>
        </div>
        <br>
      </div>
      <div class="d-flex flex-row justify-content-center">
        <Icon class="mt-1" icon="material-symbols:mode-comment-outline" style="color:blanchedalmond"/>
      </div>
      <ArticleCommentListItem 
      v-for="comment in commentList" :key="comment.id" :comment="comment"
      @delete-comment="deleteComment"/>
      <div class="mt-3">
        <input class="review-input" v-model.trim="commentContent" @keyup.enter="commentCreate">



        <button class="review-btn2" @click="commentCreate">생성</button>
      

      </div>
    </section>
  </div> -->
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
        profileImg: '/media/users/default.png',
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
    },
    getProfileImg() {
      console.log('바뀜');
      return this.profileImg
    }
  },
  methods:{
    goProfile() {
      this.$router.push({ name:'profile', params: { username: this.article.username} })
    },
    deleteComment(comment){
      // console.log(comment.id)
      axios({
        method:'delete',
        url: `${API_URL}/api/v1/articles/${this.article.id}/comments/${comment.id}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
      .then((res)=>{
        // console.log('여기')
        this.commentList=res.data
        this.article.comment_count -= 1
        // console.log('여기')
      })
    }
    ,
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
      this.article.comment_count += 1 
        
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
          console.log(res.data);
          this.liked_count= res.data.like_users.length
          if (res.data.like_users.includes(this.$store.state.user.id)){
            this.is_liked=true
          } else {
            this.is_liked=false
          }
          this.commentList=res.data.comment_set
          if (res.data.profile_img !== null) {
            this.profileImg = '/media/' + res.data.pofile_img

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
  },
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
.review-btn2 {
    width: 10%;
    height: 50px;
    border-top: none;
    border-left: none;
    border-right: none;
    border-bottom : 3px solid white;
    background-color: black;
    font-weight: 700;
    color: #FF9999;
  }

.article-detail-user-img {
  width: 50px;
  height: 50px;
  border-radius: 100px;
}
</style>