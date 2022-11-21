<template>
  <div>
    <p>{{comment.id}} {{comment.content}} 글 작성자 : {{comment.username}} </p>
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
