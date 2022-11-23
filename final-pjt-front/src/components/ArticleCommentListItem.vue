<template>
  <div class="">
    <div class="d-flex">
      <p class="commu-push me-2" style="width: 15%; cursor: pointer;" @click="goProfile()">{{comment.username}}</p>
      <p class="ms-2">{{comment.content}}</p>
      <button v-if="comment.username === this.$store.state.user.username" @click="deleteComment" class="review-btn3">[x]</button>
   <!-- {{comment}} -->
    </div>
    <hr class="my-3" style="margin:0px; border: 1px solid #D0D0D5;">
  </div>
</template>

<script>
// const API_URL = 'http://127.0.0.1:8000'
// import axios from 'axios'
export default {
  
  name:'ArticleCommentListItem',
  props:{
    comment:Object
  },
  data(){
    return{
      
    }
  },
  methods:{
    deleteComment : function () {
      this.$emit('delete-comment',this.comment)
    },
    goProfile() {
      this.$router.push({ name:'profile', params: { username: this.comment.username} })
    },
    // deleteComment(){
    //   console.log(this.comment.id)
    //   axios({
    //     method:'delete',
    //     url: `${API_URL}/api/v1/articles/${this.article.id}/comments/${this.comment.id}`,
    //     headers: {
    //       Authorization: `Token ${this.$store.state.token}`
    //     },
    //   })
    // }
  }
}
</script>

<style>
.review-btn3 {
    margin-left: 3px;
    border: none;
    background:#2a2b38;
    font-weight: 700;
    color: #FF9999;
  }
</style>
