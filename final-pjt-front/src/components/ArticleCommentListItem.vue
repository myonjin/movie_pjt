<template>
  <div class="border mt-3" style="border-radius:15px;">
    <div class="d-flex justify-content-between">
      <h5 class="ms-2" style="margin:0.5em">{{comment.content}}</h5>
      <div class="d-flex">
        <h5 class="me-2" style="margin:0.5em">{{comment.username}}</h5>
        <button @click="deleteComment" class="review-btn3">[x]</button>
      </div>
   <!-- {{comment}} -->
    </div>
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
    width: 15%;
    height: 50px;
    border-top: none;
    border-left: none;
    border-right: none;
    background:#101322;
    font-weight: 700;
    color: #FF9999;
  }
</style>
