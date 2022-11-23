<template>
  <div id="community" class="mt-2" style="color:#E8E8E8;">
    <div id="comcontent" class="p-5">
      <!-- 제목 -->
      <h1>Timeline</h1>
      <hr class="mb-3" style="margin:0px; border: 2px solid #D0D0D5;">
      <TimelineItems v-for="line in lines" :key="line.id" :line="line"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import TimelineItems from '@/components/TimelineItems'

export default {
  name: 'TimelineView',
  components: {
    TimelineItems,
  },
  data() {
    return {
      lines: null,
    }
  },
  created() {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/timeline/getlist/${this.$store.state.user.id}/`
    })
      .then((res) => {
        this.lines = res.data
      })
  }
}
</script>

<style>

</style>