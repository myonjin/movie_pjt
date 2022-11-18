
<template>
  <div >
  
      <div class="col-sm-4">
          <div class="card bg-dark text-white bg-card">
              <div class="card-img-overlay">
                  <p>
                  <button @click = "modal = true" type="button" class="btn btn-link"><i class="fa fa-play-circle" style="color:rgb(85,85,85);font-size:90px;margin:0;text-shadow: 3px 3px 3px rgba(0,0,0,0.8);"></i></button>
                  </p>
              </div>
          </div>
      </div>
                  <div class="black-bg" v-if="modal == true">
                          <div>
                              <button @click="modal = false" class="btn btn-link"><i class="fa fa-times" style="color:rgba(255,255,255,0.5);font-size:30px; position:absolute; top:10px; left:1360px;"></i></button>
                          </div>
                      <!-- <div class="white-bg"> -->
                          <div>
                              <video controls width=1360px; height=660px;>
                                  <!-- <source src="../img/SampleVideo_1280x720_5mb.mp4" > -->
                                  <video tabindex="-1" class="video-stream html5-main-video" controlslist="nodownload" style="width: 127px; height: 226px; left: 136px; top: 0px;" src="blob:https://www.youtube.com/4e179a1f-73da-4047-95f0-66f6adde9676"></video>
                              </video>
                          </div>
                  </div>
  </div>
</template>

<script>
export default {
  name:'AboutView',
  data () {
  return {
    modal: false
  }
}
}
</script>
<style>
*{
text-align: left;
}
p{
text-align: center;
}
h5{
text-align: center;
}
/* 모달창 */
body{
margin :0
}
div{
box-sizing:border-box;
}
.black-bg {
z-index: 100;
width : 1400px; height: 720px;
background: rgba(0,0,0,1);
position: fixed; top:70px; left:300px; padding: 10px;
}
.white-bg {
padding: 10px;
background: rgba(255,255,255,0.9);
border-radius: 20px;
margin-top: 25px;
margin-left: 10px;
margin-right: 10px;
}

a {
color: rgb(255,255,255);
}

.card1
{
padding: 10px;
background: rgba(240, 231, 218,0.5);
color: rgb(100,100,100);
}

body {
  margin: 0;
   /* -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"; */
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #8b8b8b;
  text-align: center;
  background-color: #ffffff;
}
</style>