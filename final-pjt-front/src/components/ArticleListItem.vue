<template>
  <div>
    <div class="d-flex">
      <!-- 글번호 -->
      <div style="width:10%;">
        <p>{{ article.id }}</p>
      </div>
      <!-- 제목 -->
      <div style="width:50%; text-align: left;">
        <p @click="goArticleDetail()" class="commu-push" style="cursor: pointer;">{{ article.title }}</p>
      </div>
      <!-- 작성자 -->
      <div style="width:20%">
        <p @click="goProfile()" class="commu-push" style="cursor: pointer;">{{ article.username }}</p>
      </div>
      <!-- 날짜 -->
      <div style="width:20%">
        <p>{{ article.created_at.slice(0,10) }}</p>
      </div>
    </div>
    <hr class="my-3" style="margin:0px; border: 1px solid #D0D0D5;">
  </div>
</template>

<script>
export default {
    name:'ArticleListItem',
    props:{
        article:Object
    },
    methods: {
      goArticleDetail() {
        this.$router.push({ name:'articledetail', params: {id: this.article.id} })
      },
      goProfile() {
        this.$router.push({ name:'profile', params: { username: this.article.username} })
      },
    }
}
</script>

<style>
.commu-push {
  color: rgb(232, 232, 232);
}
.commu-push:hover{
  color: #FF9999;
  text-decoration: underline;
  /* overflow: visible; */
}
</style>