<template>
  <div class="d-flex flex-row justify-content-center">
    <h3 >{{article.id}}</h3>
    <router-link :to="{name:'articledetail', params:{id:article.id}}" class="ms-3">{{article.title}}</router-link>
    <p :to="{name:'articledetail', params:{id:article.id}}" class="ms-3">{{article.title}}</p>
    <!-- <p class="ms-3">{{article.content}}</p> 클릭 매서드를 이용하여서 
    this.$router.push({name:'articledetail', params:{id:article.id}})-->
    <p class="ms-3">{{article.username}}</p>
    
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