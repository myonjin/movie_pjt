<template>
  <div id="community" class="mt-2" style="color:#E8E8E8;">
    <div id="comcontent">
      <!-- 제목 -->
      <h1 class="mt-5">Create Post</h1>

      <form @submit.prevent="createArticle" style="padding: 32px 32px 24px; position: relative;">
        <div class="d-flex">
          <label for="title"> 제목</label>
          <input id="input-title" type="text" v-model.trim="title"><br>
        </div>
        <div class="d-flex">
          <label class="mb-4"> 내용</label>
          <textarea id="input-content" cols="30" rows="10" v-model.trim="content"></textarea><br>
        </div>
        <input class="grayBtn" type="submit" id="submit">
      </form>

    </div>
  </div>


  <!-- <div id="community2" class="mt-2">
    <div id="comcontent2" style="position:relative; background:#101322; max-width: 700px;">
      <h1 class="mt-3">게시글 작성</h1>
    </div>
  </div> -->
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name:'CraeteView',
    data() {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content
      if (!title) {
        alert('제목을 입력해주세요')
        return
      } else if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/`,
        data: {
          title: title,
          content: content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          this.$router.push({ name: 'community' })
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }

}
</script>

<style>
#community2 {
  margin:0;
  padding: 0;
  box-sizing: border box;
  margin: 30px ;
  
}
#community2 div{
  display: block;
}
#comcontent2{
   min-height: calc(100vh - env(safe-area-inset-bottom) - 56px);
    max-width: 700px;
    margin: 0 auto;
    padding-bottom: calc(env(safe-area-inset-bottom) + 56px);
    box-sizing: border-box;
    overflow: hidden;
    justify-content: center;
    border-radius: 50px;

}
#input-title {
  width: 100%;
  height: 30px;
  background-color: #2a2b38;
  border-top: none;
  border-left: none;
  border-right: none;
  border-bottom : 3px solid #D0D0D5;
  color: #D0D0D5;
  /* opacity: 0.5; */
  outline: none;
  /* border: none; */
  margin-bottom: 5px;
  /* background: none; */
  /* border-radius: 10px; */
  
}
#input-content {
  width: 100%;
  height: 200px;
  /* border-top: none;
  border-left: none;
  border-right: none;
  border-bottom : 3px solid black; */
  /* opacity: 0.5; */
  outline: none;
  border: none;
  background-color: #D0D0D5;
  /* border-radius: 10px; */
  }
label{
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 600;
  font-size: 16px;
  color: #FFFFFF;
  display:inline-block;
	text-align:center;
	width:80px;
	font-weight:bold;
}
</style>