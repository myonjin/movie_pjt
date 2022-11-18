<template>

  <div class="container">
    <!-- <img style="position:relative; width:100%; height:80%;" alt="Hotel" src="../assets/hotel.jpg"> -->
    <div class="main-image">
      <div class="background-gradation"></div>
    </div>
    <!-- <div style="height:1000px"></div> -->


    <div class="popular_box">
      <MovieList/>
    </div>

    <div class="genre_box">
      <MovieGenreList/>
    </div>
    
  </div>

</template>

<script>
// import axios from 'axios'
import MovieList from '@/components/MovieList'
import MovieGenreList from '@/components/MovieGenreList'

export default {
  name: 'MainView',
  components: {
    MovieList,
    MovieGenreList,
  },
  data() {
    return {
      movieList:null,
    }
  },
  methods: {
  },
  
}
</script>
<style>
.box {
  position: absolute;
  width: 100%;
  height: 80%;
  left: 0px;
  top: 0px;

  background: linear-gradient(90deg, #000000 0%, rgba(0, 0, 0, 0.720349) 0.01%, rgba(1, 1, 1, 0.682696) 0.02%, rgba(5, 5, 5, 0.668436) 0.03%, rgba(0, 0, 0, 0.687449) 0.04%, rgba(183, 183, 183, 0.0458299) 99.99%, rgba(196, 196, 196, 0) 100%);
  }
.popular_box{
  position: absolute;
  width: 85%;
  height: 300px;
  right: -20px;
  bottom: -150px;

  background: rgba(11, 15, 22, 0.47);
  box-shadow: 8px -8px 10px rgba(0, 0, 0, 0.25);
  backdrop-filter: blur(12.5px);
  /* Note: backdrop-filter has minimal browser support */

  border-radius: 24px;
  } 
.popular_text{
  height: 22px;
  text-align: left;
  margin-top: 20px;
  margin-left: 20px;
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 700;
  font-size: 18px;
  line-height: 22px;
  /* identical to box height */
  color: #FFFFFF;
  }
  .genre_box{
    position: absolute;
    width: 85%;
    height: 300px;
    right: -20px;
    bottom: -550px;
  
    background: rgba(11, 15, 22, 0.47);
    box-shadow: 8px -8px 10px rgba(0, 0, 0, 0.25);
    backdrop-filter: blur(12.5px);
    /* Note: backdrop-filter has minimal browser support */
  
    border-radius: 24px;
    } 

.genre_text{
  height: 22px;
  text-align: left;
  margin-top: 20px;
  margin-left: 20px;
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 700;
  font-size: 18px;
  line-height: 22px;
  /* identical to box height */

  color: #FFFFFF;
  }

.main-image {
        position: relative;
        margin: 0;
        width: 100%;
        height: 100vh;
        background: linear-gradient(
            to left,
            rgb(0, 0, 0, 1) 0%,
            rgba(20, 20, 20, 0.4) 5%,
            rgba(20, 20, 20, 0.3) 50%,
            rgba(20, 20, 20, 0.4) 95%,
            rgba(0, 0, 0, 1) 100%
          ), url(../assets/hotel.jpg);
        background-size: cover;
      }

.background-gradation {
  position: absolute;
  width: 100%;
  height: 931px;
  left: 0px;
  bottom: 0px;

  background: linear-gradient(
            to bottom,
            rgb(0, 0, 0, 1) 0%,
            rgba(20, 20, 20, 0.4) 5%,
            rgba(20, 20, 20, 0) 50%,
            rgba(20, 20, 20, 0.4) 90%,
            rgba(0, 0, 0, 1) 100%
          );  
  background-size: inherit;
  }

select {
  width: 139px;
  height: 40px;

  background: #5C5C5C;
  border-radius: 30px;

  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 600;
  font-size: 16px;
  line-height: 20px;
  text-align: center;

  color: #FFFFFF;
}
</style>
