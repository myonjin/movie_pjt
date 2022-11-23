<template>
  <div id="community" class="mt-2">
    <div id="comcontent">
      <h1 class="mt-3 mb-3 community_font">CommunityView</h1>
      <div class="me-5 rounded-pill" style="height:30px; float:right">  
        <router-link :to="{name: 'create'}">
          <h2  style="width:100px" class="nav_font_user rounded-pill bg-secondary">Create</h2>  
        </router-link>
      </div>
      <br>
      <div style="padding: 29px 0px 21px;">
        <ArticleList/>
      </div>
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
#community {
  margin:0px;
  padding: 5px;
  box-sizing: border box;
  margin: 30px ;
  
}
#community div{
  display: block;
}

#community a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
  height: 20px;
  overflow: hidden;
  margin-right: 40px;
}

#community a.router-link-exact-active {
  color: #FF9999;
  text-decoration: none;
  overflow: visible;
}
#comcontent {
    position:relative;
    min-height: calc(100vh - env(safe-area-inset-bottom) - 56px);
    max-width: 800px;
    margin: 0 auto;
    padding-bottom: calc(env(safe-area-inset-bottom) + 56px);
    box-sizing: border-box;
    overflow: hidden;
    justify-content: center;
    border-radius: 50px;
    background:#2a2b38;
    max-width: 700px;
}
.nav_font {
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  line-height: 20px;
  text-decoration: none;
  margin-bottom: 1px;

  color: #FFFFFF;
}

.nav_font_user {
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 700;
  font-size: 24px;
  text-decoration: none;
  font-style: normal;
  font-weight: 700;
  color: #FFFFFF;
}
.nav_font_user:hover {
  color: #FF9999;
}
.nav_active {
  width: 10px;
  height: 10px;
  margin: auto;

  background: #FF9999;
  border-radius: 30px;
}
.community_font{
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 700;
  font-size: 18px;
  line-height: 22px;
  /* identical to box height */
  color: #FFFFFF;
}
</style>