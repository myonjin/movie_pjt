<template>
  <div id="app">
    <nav class="navbar fixed-top">
      <div class="container-fluid">
        <a class="navbar-brand" href="#"> 
        </a>
        <router-link class="nav_font" :to="{ name: 'home' }">Home</router-link> |
        <router-link class="nav_font" to="/search">Search</router-link> |
        <router-link class="nav font" :to="{ name: 'profile', params:{ username: this.$store.state.user.username } }" v-if="isLogin">MY</router-link>

        <router-link class="nav font" :to="{ name: 'community'}">Community</router-link>
        <button @click="logOut" v-if="isLogin">LOGOUT</button>

      </div>  
    </nav>

    <!-- router params 변경 시 페이지 새로고침 -->
    <router-view :key="$route.fullPath"/>

  </div>
</template>

<script>

export default ({
  methods: {
    logOut() {
      this.$store.dispatch('logOut')
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
  height: 63px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  
}

nav a.router-link-exact-active {
  color: #42b983;
}
.nav_font {
  font-family: 'Montserrat';
font-style: normal;
font-weight: 700;
font-size: 16px;
line-height: 20px;
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
</style>
