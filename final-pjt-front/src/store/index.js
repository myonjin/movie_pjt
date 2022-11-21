import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    articles: [
    ],
    token: null,
    user: {
      id: null,
      username: null,
      profile_img_src: null,
      profile_msg: null,
      following: null,
      followers: null,
      following_count: null,
      followers_count: null,
    }
  },
  
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    // 회원가입 && 로그인
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'home' })
    },
    SAVE_USER_PROFILE(state, user) {
      const loginUser = {
        id: user.id,
        username: user.username,
        profile_img_src: user.profile_img_src,
        profile_msg: user.profile_msg,
        following: user.following,
        followers: user.followers,
        following_count: user.following_count,
        followers_count: user.followers_count,
      }
      state.user = loginUser
    },
    DELETE_TOKEN(state) {
      state.token = null
      router.push({ name: 'login' })
    },
    UPDATE_FOLLOWING(state, newFollowing) {
      state.user.following = newFollowing
    }
  },
  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
        // headers: {
        //   Authorization: `Token ${context.state.token}`
        // }
      })
        .then((res) => {
          console.log(res.data)
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getMyProfile(context, username) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/api/profile/${username}/`,
      })
      .then((res) => {
        context.commit('SAVE_USER_PROFILE', res.data)
      })
    },
    follow(context, followUserId) {
      const oldFollowing = context.state.user.following
      oldFollowing.push(followUserId)
      context.commit('UPDATE_FOLLOWING', oldFollowing)
    },
    unFollow(context, UnfollowUserId) {
      const oldFollowing = context.state.user.following
      const newFollowing = oldFollowing.filter((exist) => exist!==UnfollowUserId)
      context.commit('UPDATE_FOLLOWING', newFollowing)
    },
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
      .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
        this.dispatch('getMyProfile', payload.username)
      })
      .catch((err) => {
        console.log(err);
      })
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
      .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
        this.dispatch('getMyProfile', payload.username)
      })
    },
    logOut(context) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
      .then(() => {
        context.commit('DELETE_TOKEN')
      })
    },

  },
  modules: {
  }
})
