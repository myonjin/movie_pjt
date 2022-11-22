<template>
  <div id="community2" class="mt-2">
    <div id="comcontent2" style="position:relative; background:#101322; max-width: 700px;">
      <h1 class="mt-3">게시글 작성</h1>
      <form @submit.prevent="createArticle" style="padding: 32px 32px 24px; position: relative;">
        <div class="d-flex justify-content-center">
          <label for="title"> 제목 : </label>
          <input class="ms-1" type="text" id="input1" v-model.trim="title"><br>
        </div>
        <div style="vertical-align:middle;" class="d-flex align-items-center">
          <label class="mb-4"> 내용 : </label>
          <textarea class="ms-2" id="input2" cols="30" rows="10" v-model="content"></textarea><br>
        </div>
        <input class="grayBtn" type="submit" id="submit">
      </form>
    </div>
  </div>
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
#input1 {
width: 300px;
        height: 50px;
        border-top: none;
        border-left: none;
        border-right: none;
        border-bottom : 3px solid black;
        border-radius: 10px;
        
    }
#input2 {
width: 480px;
        height: 200px;
        border-top: none;
        border-left: none;
        border-right: none;
        border-bottom : 3px solid black;
        border-radius: 10px;
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