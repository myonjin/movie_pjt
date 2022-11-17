<template>
  <div id="app">
    <nav class="navbar fixed-top">
      <div class="container-fluid">
        <a class="navbar-brand" href="#"> 
        </a>
        <router-link class="nav_font" :to="{ name: 'home' }">Home</router-link> |
        <router-link class="nav_font" to="/about">About</router-link>
      </div>  
    </nav>
    
        <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
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
</style>
