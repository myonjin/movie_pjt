<template>
    <div>
        
        <h2>리뷰 번호:{{review.id+1}} 내용: {{review.content}} 평점:{{review.score}} 글작성자:{{review.user.username}}</h2>
        
    </div>
</template>

<script>

export default {
    name:'MovieReviewListItem',
    props:{
        review:Object
    }
}
</script>

<style>

</style>