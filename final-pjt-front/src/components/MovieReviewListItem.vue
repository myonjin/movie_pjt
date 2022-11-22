<template>
    <div class="d-flex">
        <img @click="goProfile(review.user.username)" class="follow-user-image" :src="`http://127.0.0.1:8000${review?.user.profile_img_src}`" onerror="this.src='http://127.0.0.1:8000/media/users/default.png'">
        <div style="padding-bottom:10px">
            <!-- 위 -->
            <div class="d-flex">
                <p class="review-user">{{ review.user.username }}</p>
                <span class="user-star">
                  ★★★★★
                  <span :id="`star-${review.user.id}`">★★★★★</span>
                </span>
                <p class="user-score">{{ starScore }}</p>
            </div>
            <!-- 아래 -->
            <p class="review-content">{{ review.content }}</p>

        </div>
        
    </div>
</template>

<script>

export default {
    name:'MovieReviewListItem',
    props:{
        review:Object
    },
    data() {
        return {
            starScore : 0,
        }
    },
    methods: {
        goProfile(username) {
            this.$router.push({name:'profile', params:{username : username}})
        }
    },
    watch: {
        starScore() {
            const scoreSpanTag = document.querySelector(`#star-${this.review.user.id}`)
            scoreSpanTag.style.width = `${this.starScore * 10}%`
        }
    },
    mounted() {
        this.starScore = this.review.score
    },
    updated() {
        this.starScore = this.review.score
    }
}
</script>

<style>
  .user-star {
    position: relative;
    font-size: 1.5rem;
    color: #ddd;
    line-height: 70px;
  }
  
  .user-star span {
    width: 0;
    position: absolute; 
    left: 0;
    color: #FFC907;
    overflow: hidden;
    pointer-events: none;
    line-height: 70px;
  }

  .review-user {
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 600;
  font-size: 25px;
  line-height: 25px;
  text-align: left;
  margin-bottom: 0px;
  margin-right: 15px;
  line-height: 70px;

  color: #FF9999;
}
  .review-content {
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 25px;
  text-align: left;
  line-height: 0px;

  color: #FFFFFF;
 }
 .user-score {
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 400;
  font-size: 25px;
  line-height: 25px;
  text-align: left;
  line-height: 75px;
  margin-bottom: 0px;
  margin-left: 4px;

  color: #FFFFFF;
 }
</style>