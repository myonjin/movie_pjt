<template>
  <div>
    <ArticleListItem class="ms-5"
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