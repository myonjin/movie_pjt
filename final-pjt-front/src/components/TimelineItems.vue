<template>
  <div> 
    <div @click="checkLine()" :class="line.is_checked ? '' : 'newline'">
      <div class="d-flex align-items-center">
        <!-- 프사 -->
        <img class="article-detail-user-img me-2" :src="`http://127.0.0.1:8000/media/${line.profile_img}`" onerror="this.src='http://127.0.0.1:8000/media/users/default.png'">
        <!-- 누구님이 뭐시기 했어요 -->
        <p class="timeline-text">
          <span>{{ line.username }}</span>
          님이
          <span>'{{ line.content }}'</span>
          {{ msg }}
        </p>
      </div>
    </div>
    <hr class="my-3" style="margin:0px; border: 1px solid #D0D0D5;">
  </div>
</template>

<script>
export default {
  name: 'TimelineItems',
  props: {
    line: Object,
  },
  data() {
    return {
      msg: null,
    }
  },
  methods: {
    checkLine() {
      this.$router.push({ name:`${this.line.router}`, params: { id: `${Number(this.line.params)}` } })
    }
  },
  created() {
    if (this.line.what === 'movielike') {
      this.msg = '영화를 좋아합니다.'
    }
    if (this.line.what === 'review') {
      this.msg = '영화에 한줄평을 남겼습니다.'
    }
    if (this.line.what === 'article') {
      this.msg = '게시글을 남겼습니다.'
    }
  }
}
</script>

<style>
.timeline-text span{
  color: #F99999;
}
.newline {
  background-color: #FFC0CB;
  color: black;
  border-radius: 10px;
  padding: 2px;
}
.newline span{
  color: black;
}
</style>