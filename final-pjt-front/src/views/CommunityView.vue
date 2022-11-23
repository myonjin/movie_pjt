<template>
  <div id="community" class="mt-2" style="color:#E8E8E8;">
    <div id="comcontent">
      <!-- 제목 -->
      <h1 class="mt-5">Community</h1>

      <!-- 글 목록 -->
      <div class="mx-3" style="text-align: center;">
        <!-- 항목(테이블) -->
        <div class="d-flex">
          <!-- 글번호 -->
          <div style="width:10%;">
            <p>No.</p>
          </div>
          <!-- 제목 -->
          <div style="width:50%">
            <p>제목</p>
          </div>
          <!-- 작성자 -->
          <div style="width:20%">
            <p>작성자</p>
          </div>
          <!-- 날짜 -->
          <div style="width:20%">
            <p>날짜</p>
          </div>
        </div>
        <hr class="mb-3" style="margin:0px; border: 2px solid #D0D0D5;">
        <ArticleList/>


      </div>

      <button @click="goCreate()" class="create-btn">+</button>


      <!-- <h1 class="mt-3 mb-3 community_font">Community</h1>

      <div class="me-5 rounded-pill" style="height:30px; float:right">  
        <router-link :to="{name: 'create'}">
          <h2  style="width:100px" class="nav_font_user rounded-pill bg-secondary">Create</h2>  
        </router-link>
      </div>
      <br>
      <div style="padding: 29px 0px 21px;">
        <ArticleList/>
      </div> -->
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
    },
    goCreate() {
      this.$router.push({ name:'create' })
    }
  }
}
</script>

<style> 
.create-btn {
  position: fixed;
  bottom: 80px;
  left: calc( 50% + 250px );
  width: 70px;
  height: 70px;
  font-size: 70px;
  line-height: 47px;
  border-radius: 100px;
  border: none;
  outline: none;
  background-color: #FF9999;
  color: white;
}

#comcontent {
    position:relative;
    min-height: calc(100vh - env(safe-area-inset-bottom) - 56px);
    margin: 0 auto;
    padding-bottom: calc(env(safe-area-inset-bottom) + 56px);
    box-sizing: border-box;
    overflow: hidden;
    justify-content: center;
    border-radius: 50px;
    background:#2a2b38;
    max-width: 700px;
    margin-bottom: 50px;
}
#comcontent p {
  margin-bottom: 0px;
}
#comcontent h1 {
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 700;
  font-size: 40px;
  margin-bottom: 50px;
  /* identical to box height */
  color: #FFFFFF;
}
/* .nav_font {
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
  color: #FFFFFF;} */
</style>