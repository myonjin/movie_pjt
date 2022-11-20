<template>
  <div>
    <h1>CommunityView</h1>
    <router-link :to="{name: 'create'}">Create</router-link>
    <ArticleList/>

  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList';
export default {
    name:'CommunityView',
    components:{
        ArticleList,
    },
    created(){
    this.getArticles()
  },
  methods:{
    getArticles() { 
        this.$store.dispatch('getArticles')
    }
  }
}
</script>

<style> 

</style>