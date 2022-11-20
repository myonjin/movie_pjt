<template>
  <div>
    <div style="height:350px; position:relative;">
      <div class="profile-box">
        <img class="profile-image" src="../assets/profile_default.png" alt="">
        <input @change="fileUpload($event)"
          v-if="this.$route.params.username === this.$store.state.user.username"
          type="file" accept="image/*"/>
        <div style="margin-left:20px;">
          <p class="profile-username">{{ user?.username }}</p>
          <p>상태메세지</p>
        </div>
        <div>
          <p>팔로잉 : <span id="following-count">{{ user?.following_count }}</span></p>
          <p>팔로워 : <span id="followers-count">{{ user?.followers_count }}</span></p>
        </div>
        <button id="follow" class="pinkBtn" @click="follow"></button>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ProfileView',
  data() {
    return {
      user: null,
      isFollowing: null,
    }
  },
  methods: {
    fileUpload(e) {
      console.log(e.target.files);
    },
    follow() {
      const userId = this.user.id
      const followersCountTag = document.querySelector('#followers-count')
      if (this.isFollowing === false) {
        // 팔로우
        this.$store.dispatch('follow', userId)
        this.isFollowing = true
        followersCountTag.innerText++
      } else {
        // 언팔로우
        this.$store.dispatch('unFollow', userId)
        this.isFollowing = false
        followersCountTag.innerText--
      }
      this.changeFollowBtn()
      
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/accounts/api/follow/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          user_id: userId,
        }
      })
      .then((res) => {
        console.log(res);
        return res.data
      })
      .then(() => {
        this.dispatch('getMyProfile', this.$store.state.user.username)
      })
      .catch((err) => {
        console.log(err);
      })
    },

  },
  created() {
    // 내 계정이면 store에서 가져오기
    // if (this.$route.params.username === this.$store.state.user.username) {
    //   this.user = this.$store.state.user
    // }
    // 아님 axios 받아오기
    // else {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/accounts/api/profile/${this.$route.params.username}/`,
    })
    .then((res) => {
      this.user = res.data
      const me = this.$store.state.user.id
      if (this.user.followers.includes(me)) {
        this.isFollowing = true
      } else {
        this.isFollowing = false
      }
    })
    // }
  },
  watch: {
    isFollowing: function() {
      const followBtn = document.querySelector('#follow')
      if (this.isFollowing === true) {
        followBtn.innerText = '언팔로우'
        followBtn.classList = 'grayBtn'
      } else {
        followBtn.innerText = '팔로우'
        followBtn.classList = 'pinkBtn'
      }
    }
  },
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
  font-family: 'Roboto';
  font-style: normal;
  font-weight: 700;
  font-size: 64px;
  line-height: 75px;

  /* pink */

  color: #FFC0CB;
}

.profile-image {
  width: 180px;
  height: 180px;
}
</style>