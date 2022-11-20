<template>
  <div>
    <h2>aritclelist</h2>
    <ArticleListItem
    v-for="article in articles" :key="article.id" :article="article"
    />
  </div>

</template>

<script>
import ArticleListItem from './ArticleListItem';
export default {
    name:'ArticleList',
    components:{
        ArticleListItem,
    },
    computed:{
        articles(){
            return this.$store.state.articles
        }
    }
}
</script>

<style>

</style>