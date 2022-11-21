<template>
  <div>
    <h1>CommunityView</h1>
    <router-link :to="{name: 'create'}">Create</router-link>
    <ArticleList/>
    <div>
  <b-button v-b-modal.modal-1>Launch demo modal</b-button>

  <b-modal  size="lg"  id="modal-1" title="BootstrapVue">
    <h2 class="my-4">Hello from modal!</h2>
  </b-modal>
</div>
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