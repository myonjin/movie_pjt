<template>
  <div style="height: 1000px">
    <div style="height:350px; position:relative;">
      <div class="profile-box">
        <!-- 프로필 사진 -->
        <div style="position:relative; width:20%; margin-left: 150px;">
          <img
            class="profile-image"
            :src="`http://127.0.0.1:8000${user?.profile_img_src}`"
            onerror="this.src='http://127.0.0.1:8000/media/users/default.png'" 
            alt="">
          <label for="file" class="uploadBtn" v-if="this.$route.params.username === this.$store.state.user.username">+</label>
          <input @change="fileUpload"
            accept="image/*" type="file" id="file" style="display:none;"
            v-if="this.$route.params.username === this.$store.state.user.username"
          />
        </div>
        <!-- 이름 + 팔로우정보 -->
        <div style="margin-left:80px; width:40%;">
          <p class="profile-username">{{ user?.username }}</p>
          <div class="d-flex align-items-center">
            <div style="margin-left:10px;">
              <p class="follow-count">팔로잉 : <span id="following-count">{{ user?.following_count }}</span></p>
              <p class="follow-count">팔로워 : <span id="followers-count">{{ user?.followers_count }}</span></p>
            </div>
            <button id="follow" class="pinkBtn" @click="follow"
              v-if="this.$route.params.username !== this.$store.state.user.username"  style="margin-left:30px;"
            ></button>
          </div>
        </div>
        <!-- 차트 -->
        <div id="chart" style=" width:500px; height:230px; text-align:center; margin-left:180px;">
          <p style="width: 100%; margin-bottom:0;">선호 장르</p>
          <apexChart width="500" height="230" type="bar" :options="options" :series="[this.movieList]"></apexChart>
        </div>
      </div>
      
    </div>

    <ProfileUserLikeMovie v-if="user!==null" :userId="userId"/>

    <ProfileUserReviewMovie v-if="user!==null" :userId="userId" :username="user.username"/>
    <!-- <div id="chart">
        <p>Today's Chart</p>
        <apexChart width="500" type="bar" :options="options" :series="[this.movieList]"></apexChart>
    </div> -->
  </div>
</template>

<script>
import axios from 'axios'
import ProfileUserLikeMovie from '@/components/ProfileUserLikeMovie.vue'
// import ProfileUserReviewMovie from '@/components/ProfileUserReviewMovie.vue';
import ProfileUserReviewMovie from '@/components/ProfileUserReviewMovie.vue';
// import ApexCharts from 'apexcharts'
// import VueApexCharts from 'vue-apexcharts'

export default {
    name: "ProfileView",
    conponents: {
        ProfileUserLikeMovie,
        ProfileUserReviewMovie,
        // apexcharts: VueApexCharts
    },
    data() {
        return {
          options: {
                    xaxis: {
                        categories: ['모험','판타지','애니메이션','드라마','공포','액션','코미디','범죄','SF',],
                        labels:{
                          style:{
                            colors:['#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF',]
                          }
                        },
                        title:{
                          style:{
                            color:'#FFFFFF',
                          }
                        }
                      },
                    yaxis:{
                      labels:{
                        style:{
                          colors:['#000000']
                        }
                      }
                    },
                    colors: ['#FEDD36'],
                    // group:{
                    //   style:{
                    //     colors:['FFFFFF','FFFFFF']
                    //   }
                    // },
                    fill: {
                        
                        type: 'gradient',
                        gradient: {
                            shadeIntensity: 1,
                            type: "vertical",
                            opacityFrom: 0.7,
                            opacityTo: 0.9,
                            colorStops: [
                                {offset: 0, color: "#fbc2eb", opacity: 1},
                                {offset: 100, color: "#FF9999", opacity: 0.7}
                            ]
                        }
                    }, 
                    dataLabels:{
                      offsetY: -20,
                      style:{
                        // fontSize:'10px',
                        // fontWeight:'bold'
                      }
                    },
                    plotOptions: {
                        bar: {columnWidth: '40%', endingShape: 'rounded', 
                        dataLabels: {
                          position: 'top'}}
                    },
                },
                series: [{name: 'data', data: [1, 2, 3, 4, 5, 4]}],
            
        
          movieList:{
            name: 'first',
            data: []
        },
          user: null,
          isFollowing: null,
          imgFile: null,
          profileImg: null,
        };
    },
    methods: {
        // selectFile(file) {
        //   this.imgFile = file
        // },
        fileUpload(e) {
            let info = new FormData();
            info.append("img-file", e.target.files[0]);
            axios.post("http://127.0.0.1:8000/accounts/api/uploadimg/", info, {
                headers: {
                    "Authorization": `Token ${this.$store.state.token}`,
                    "Content-Type": "multipart/form-data"
                }
            })
                .then((res) => {
                const src = res.data.src;
                // console.log(src);
                this.user.profile_img_src = "/media/" + src;
            });
        },
        follow() {
            const userId = this.user.id;
            const followersCountTag = document.querySelector("#followers-count");
            if (this.isFollowing === false) {
                // 팔로우
                this.$store.dispatch("follow", userId);
                this.isFollowing = true;
                followersCountTag.innerText++;
            }
            else {
                // 언팔로우
                this.$store.dispatch("unFollow", userId);
                this.isFollowing = false;
                followersCountTag.innerText--;
            }
            this.changeFollowBtn();
            axios({
                method: "put",
                url: `http://127.0.0.1:8000/accounts/api/follow/`,
                headers: {
                    Authorization: `Token ${this.$store.state.token}`
                },
                data: {
                    user_id: userId,
                }
            })
                .then(() => {
                this.$store.dispatch("getMyProfile", this.$store.state.user.username);
            })
                .catch((err) => {
                  
                console.log(err);
            });
        },
        changeFollowBtn() {
            const followBtn = document.querySelector("#follow");
            if (this.isFollowing === true) {
                followBtn.innerText = "언팔로우";
                followBtn.classList = "grayBtn";
            }
            else {
                followBtn.innerText = "팔로우";
                followBtn.classList = "pinkBtn";
            }
        },
    },
    computed: {
      userId() {
        return this.user.id
      }
    },
    created() {
        axios({
            method: "get",
            url: `http://127.0.0.1:8000/accounts/api/profile/${this.$route.params.username}/`,
        })
            .then((res) => {
            this.user = res.data;
            const me = this.$store.state.user.id;
            if (this.user.id !== me) {
                if (this.user.followers.includes(me)) {
                    this.isFollowing = true;
                }
                else {
                    this.isFollowing = false;
                }
                this.changeFollowBtn();
            }
            // console.log(this.user)
            axios({
            method: 'get',
            url: `http://127.0.0.1:8000/accounts/api/userlikemovie/${this.user.id}/`,
            })
            .then((res) => {
              // console.log('2222')
              let movie_number = {
                12:0, 14:0,16:0,18:0,27:0,28:0,35:0,80:0,878:0,
                36:0, 37:0, 53:0, 99:0, 9648:0, 10402:0, 10749:0
              }
              // this.movieList = res.data.movie_set
              for (const movie of res.data.movie_set) {
                for (const genre_id of movie.genre){
                  movie_number[genre_id]++
                } 
              }
              // console.log(movie_number)
              const graphData = [movie_number[12],movie_number[14],movie_number[16],movie_number[18],movie_number[27],movie_number[28],movie_number[35],movie_number[80],movie_number[878]]            
              // console.log(graphData)
              // console.log(this.series[0])

              this.movieList= {name:'data',data: graphData}
              
              // chart.render()
            
            })

        });
        
    },
    mounted(){
      
    },
    components: { ProfileUserLikeMovie, ProfileUserReviewMovie }
}
</script>

<style>
.profile-box {
  height:150px;
  position:absolute;
  top:120px;
  left:50px;
  display: flex;
  align-items: center;
}

.profile-username {
  text-align: left;
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 700;
  font-size: 64px;
  line-height: 75px;
  color: #FFC0CB;
}

.profile-image {
  width: 180px;
  height: 180px;
  border: 1px solid #FFFFFF;
  border-radius: 9px;
}

.follow-count {
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 700;
  font-size: 18px;
  margin-top: 10px;
  margin-bottom: 10px;
  color: #FFFFFF;
}

.uploadBtn {
  position: absolute;
  right: -15px;
  bottom: -10px;
  width: 40px;
  height: 40px;
  cursor: pointer;

  border: none;
  background: #FF9999;
  border-radius: 30px;

  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 600;
  font-size: 50px;
  line-height: 36px;
  text-align: center;

  color: #FFFFFF;
}
#chart p {
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 700;
        font-size: 20px;
        font-weight: bold;
        color: #FFFFFF;
        
    }
</style>
