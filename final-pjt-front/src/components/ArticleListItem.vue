<template>
  <div>
    <div class="d-flex">
          <!-- 글번호 -->
          <div style="width:10%;">
            <p>{{ article.id }}</p>
          </div>
          <!-- 제목 -->
          <div style="width:50%; text-align: left;">
            <p>{{ article.title }}</p>
          </div>
          <!-- 작성자 -->
          <div style="width:20%">
            <p>{{ article.username }}</p>
          </div>
          <!-- 날짜 -->
          <div style="width:20%">
            <p>{{ article.created_at.slice(0,10) }}</p>
          </div>
        </div>
        <hr class="my-3" style="margin:0px; border: 1px solid #D0D0D5;">
    <!-- <div class="d-flex flex-row justify-content-between align-items-center">
      <h3 class="community_font" style="width:80px;" >{{article.id}}</h3>
      <div style="width:55%">
        <router-link :to="{name:'articledetail', params:{id:article.id}}" class="ms-3">
          <p class="nav_font">{{article.title}}</p>
        </router-link>
      </div>
      <router-link style="width: 100px; text-align: start;" :to="{name:'profile', params:{username:article.username}}" class="ms-3">
        <p class="nav_font">{{article.username}}</p>
      </router-link>
      
    </div> -->


    <!-- <p :to="{name:'articledetail', params:{id:article.id}}" class="ms-3">{{article.title}}</p> -->
    <!-- <p class="ms-3">{{article.content}}</p> 클릭 매서드를 이용하여서 
      this.$router.push({name:'articledetail', params:{id:article.id}})-->
    </div>
  </template>

<script>
export default {
    name:'ArticleListItem',
    props:{
        article:Object
    }
}
</script>

<style>

</style>