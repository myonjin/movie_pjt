<template>
  <div id="app">
    <nav class="navbar fixed-top" style="position:relative;">
      <div class="d-flex justify-contents-between" style="position:absolute; top:35px; width:100%">
        <p @click="goHome()" class="logo-text">Kim&Jang</p>
        <div class="d-flex" style="width:100%">
          <a class="navbar-brand" href="#"> 
          </a>
          <router-link :to="{ name: 'home' }">
            <p class="nav_font">Home</p>
            <div class="nav_active"></div>
          </router-link>
          <router-link :to="{ name: 'profile', params:{ username: this.$store.state.user.username } }" v-if="isLogin">
            <p class="nav_font">MY</p>
            <div class="nav_active"></div>
          </router-link>

          <router-link :to="{ name: 'community'}">
            <p class="nav_font">Community</p>
            <div class="nav_active"></div>
          </router-link>
        </div>
        <!-- search + logout -->
        
        <Icon class="search-icon" icon="uil:search" />
        <div class="d-flex" v-if="this.$route.name!=='login'">
          <!-- 검색바 -->
          <form class="search-form" @submit.prevent="onSearch">
            <input class="search-bar" type="text" v-model="inputKeyword" name="" placeholder="SEARCH">
          </form>


          <!-- <router-link class="nav_font" to="/search">Search</router-link> -->

          <button class="loginBtnPosition grayBtn" @click="logOut" v-if="isLogin" style="height:37px; background: none; opacity: 0.4; font-size: 16px;">LOGOUT</button>
          <button class="loginBtnPosition pinkBtn" @click="logIn" v-if="!isLogin" style="height:37px;">LOGIN</button>

        </div>

      </div>  
    </nav>

    <!-- router params 변경 시 페이지 새로고침 -->
    <router-view :key="$route.fullPath"/>

  </div>
</template>

<script>
// import axios from 'axios'
import { Icon } from '@iconify/vue2';

export default ({
  data() {
    return {
      inputKeyword: null,
    }
  },
  components:{
    Icon
  },
  methods: {
    logIn() {
      this.$router.push({ name: 'login' })
    },
    logOut() {
      this.$store.dispatch('logOut')
    },
    goHome() {
      this.$router.push({ name:'home' })
    },
    onSearch() {
      this.$router.push({ name:'search', params:{ keyword: this.inputKeyword }}).catch(()=>{})
      this.inputKeyword = ''
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
})
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
  background-color: black;
}

nav {
  padding: 30px;
  background: rgba(0, 0, 0, 0.75);
  box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.25);
  height: 93px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
  height: 20px;
  overflow: hidden;
  margin-right: 40px;
}

nav a.router-link-exact-active {
  color: #FF9999;
  text-decoration: none;
  overflow: visible;
}
.nav_font {
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  line-height: 20px;
  text-decoration: none;
  margin-bottom: 8px;

  color: #FFFFFF;
}
.nav_font:hover {
  color: #FF9999;
}
.nav_active {
  width: 10px;
  height: 10px;
  margin: auto;

  background: #FF9999;
  border-radius: 30px;
}
.logo-text {
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 400;
  font-size: 36px;
  line-height: 44px;
  /* identical to box height */
  line-height: 22px;
  margin-left: 20px;
  margin-right: 20px;

  color: #FF9999;
}
.pinkBtn {
  width: 80px;
  height: 30px;
  border: none;
  margin-right: 5px;

  background: #FF9999;
  border-radius: 30px;

  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 600;
  font-size: 13px;
  line-height: 20px;
  text-align: center;

  color: #FFFFFF;
  }
.search-form {
  position: absolute;
  top: -7px;
  right: 120px;
}
.search-bar {
  width: 324px;
  height: 37px;
  border: none;
  outline: none;
  background: rgba(255, 153, 153, 0.6);
  border-radius: 18.5px;
  padding-left: 40px;

  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 500;
  font-size: 16px;
  line-height: 20px;
  letter-spacing: 2px;

  color: #FFFFFF;
  opacity: 1;
}
.search-form ::placeholder {
  color: #FFFFFF;
  opacity: 0.6;
}
.search-form ::-webkit-input-placeholder {
  color: #FFFFFF;
  opacity: 0.6;
}
.loginBtnPosition {
  position:absolute;
  top: -7px;
  right: 20px;
  height:37px;

}
.search-icon {

  position: absolute;
  top: -13px;
  right: 410px;
  height: 48px;
  font-size: 22px;
  line-height: 48px;
  text-align: left;
  color: #ffffff;
  opacity: 1;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}

</style>
