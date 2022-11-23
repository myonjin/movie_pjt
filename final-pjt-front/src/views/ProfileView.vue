<template>
  <div style="height: 1000px">
    <div style="height:350px; position:relative;">
      <div class="profile-box">
        <div style="position:relative;">
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
        <div style="margin-left:20px;">
          <p class="profile-username">{{ user?.username }}</p>
          <p>상태메세지</p>
        </div>
        <div style="margin-left:300px;">
          <p class="follow-count">팔로잉 : <span id="following-count">{{ user?.following_count }}</span></p>
          <p class="follow-count">팔로워 : <span id="followers-count">{{ user?.followers_count }}</span></p>
        </div>
        <button id="follow" class="pinkBtn" @click="follow"
          v-if="this.$route.params.username !== this.$store.state.user.username"  style="margin-left:30px;"
        ></button>
      </div>
    </div>

    <ProfileUserLikeMovie v-if="user!==null" :userId="userId"/>

    <ProfileUserReviewMovie v-if="user!==null" :userId="userId" :username="user.username"/>
    <div id="chart">
        <p>Today's Chart</p>
        <apexChart class="" width="500" height="350" type="bar" :options="options" :series="series"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ProfileUserLikeMovie from '@/components/ProfileUserLikeMovie.vue'
// import ProfileUserReviewMovie from '@/components/ProfileUserReviewMovie.vue';
import ProfileUserReviewMovie from '@/components/ProfileUserReviewMovie.vue';
// import ApexCharts from 'apexcharts'
import VueApexCharts from 'vue-apexcharts'

export default {
    name: "ProfileView",
    conponents: {
        ProfileUserLikeMovie,
        ProfileUserReviewMovie,
        apexcharts: VueApexCharts
    },
    data() {
        return {
          options: {
                    xaxis: {
                        categories: ['모험', '판타지', '애니메이션', '드라마', '공포', '액션', '코미디', '범죄','SF'],
                        labels:{
                          style:{
                            colors:['#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF'],
                          }
                        }
                    },
                    fill: {
                        type: 'gradient',
                        gradient: {
                            shadeIntensity: 1,
                            type: "vertical",
                            opacityFrom: 0.7,
                            opacityTo: 0.9,
                            colorStops: [
                                {offset: 0, color: "#FF9999", opacity: 1},
                                {offset: 100, color: "FF2E00", opacity: 1}
                            ]
                        }
                    }, 
                      plotOptions: {
                        bar: {columnWidth: '40%', endingShape: 'rounded', dataLabels: {position: 'top'}}
                    },
                },
          series: [{
              name: 'data',
              data: [this.movieList]
            }],
          movieList:[1,2,3,4,5],
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
              // this.movieList.push(graphData)
              // console.log(this.movieList)
              this.series[0].data = graphData
              // console.log(this.series[0].data)
              // const q = document.querySelector("#follow")
              
              // var chart = new ApexCharts(document.querySelector("#chart"), this.options);
              // // console.log(chart)
              
              // chart.updateSeries([{
              //   data: [32, 44, 31, 41, 22]
              // }])
              // chart.render()
            
            })

        });
        
    },
    mounted(){
      const q = document.querySelector("#follow")
      console.log(q)
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
  line-height: 22px;
  color: #FFFFFF;
}

.uploadBtn {
  position: absolute;
  right: -15px;
  bottom: -10px;
  width: 40px;
  height: 40px;

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
</style>
