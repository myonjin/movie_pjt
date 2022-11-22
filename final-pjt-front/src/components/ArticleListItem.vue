<template>
  <div>
    <div class="d-flex flex-row justify-content-between align-items-center">
      <h3 class="community_font" style="width:80px;" >{{article.id}}</h3>
      <div style="width:55%">
        <router-link :to="{name:'articledetail', params:{id:article.id}}" class="ms-3">
          <p class="nav_font">{{article.title}}</p>
        </router-link>
      </div>
      <router-link style="width: 100px; text-align: start;" :to="{name:'profile', params:{username:article.username}}" class="ms-3">
        <p class="nav_font">{{article.username}}</p>
      </router-link>
      
    </div>
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