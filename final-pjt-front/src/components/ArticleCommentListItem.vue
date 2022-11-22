<template>
  <div class="border mt-3 ms-4 me-4 "  style="border-radius:15px;">
    <div class="d-flex justify-content-between">
      <h5 class="ms-2" style="margin:0.5em">{{comment.content}}</h5>
      <h5 class="me-2" style="margin:0.5em">{{comment.username}}</h5>
      <button class="review-btn">삭제</button>
    </div>
  </div>
</template>

<script>
export default {
  name:'ArticleCommentListItem',
  props:{
    comment:Object
  }
}
</script>

<style>

</style>
