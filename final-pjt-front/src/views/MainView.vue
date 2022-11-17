<template>

  <div class="main" >
    <div class="box">
    </div>
    <div class="popular_box">
      <movieList/>
    </div>
    <p class="popular_text">인기영화</p>
    <img style="width:100%;" alt="Hotel" src="../assets/hotel.jpg">
    
    
  </div>

</template>

<script>
// @ is an alias to /src
// import axios from 'axios'
import MovieList from '@/components/MovieList'
export default {
  name: 'MainView',
  components: {
    MovieList
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
width: 1440px;
height: 907px;
left: 0px;
top: 0px;

background: linear-gradient(90deg, #000000 0%, rgba(0, 0, 0, 0.720349) 0.01%, rgba(1, 1, 1, 0.682696) 0.02%, rgba(5, 5, 5, 0.668436) 0.03%, rgba(0, 0, 0, 0.687449) 0.04%, rgba(183, 183, 183, 0.0458299) 99.99%, rgba(196, 196, 196, 0) 100%);
}
.popular_box{
  position: absolute;
width: 1429px;
height: 399px;
left: 125px;
top: 625px;

background: rgba(11, 15, 22, 0.47);
box-shadow: 8px -8px 10px rgba(0, 0, 0, 0.25);
backdrop-filter: blur(12.5px);
/* Note: backdrop-filter has minimal browser support */

border-radius: 24px;
}
.popular_text{
  position: absolute;
width: 351px;
height: 22px;
left: 148px;
top: 651px;

font-family: 'Montserrat';
font-style: normal;
font-weight: 700;
font-size: 18px;
line-height: 22px;
/* identical to box height */


color: #FFFFFF;

}
</style>
