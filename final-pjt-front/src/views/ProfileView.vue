<template>
  <div>
    <div style="height:350px; position:relative;">
      <div class="profile-box">
        <img src="../assets/logo.png" alt="">
        <p>{{ this.$route.params.username }}</p>

      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'ProfileView',
  created() {
    // console.log(user)
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

.profile-box p {
  font-family: 'Roboto';
  font-style: normal;
  font-weight: 700;
  font-size: 64px;
  line-height: 75px;

  /* pink */

  color: #FFC0CB;
}
</style>