<template>
  <div>
  <div class="section">
    <div class="container">
      <div class="row full-height justify-content-center">
        <div class="col-12 text-center align-self-center pb-5">
          <div class="section pb-5 pt-5 pt-sm-2 text-center">
            <h6 class="mb-0 pb-3"><span>Log In </span><span>Sign Up</span></h6>
                  <input class="checkbox" type="checkbox" id="reg-log" name="reg-log"/>
                  <label for="reg-log"></label>
            <div class="card-3d-wrap mx-auto">
              <div class="card-3d-wrapper">
                <div class="card-front">
                  <div class="center-wrap">
                    <div class="section text-center">
                      <h4 class="mb-4 pb-3">Log In</h4>
                      <div class="form-group">
                        <input type="text" name="logeid" class="form-style" placeholder="Your Id" id="logeid" autocomplete="off" v-model="logId">
                        <Icon class="input-icon" icon="uil:user" />
                      </div>  
                      <div class="form-group mt-2">
                        <input  @keyup.enter="logIn" type="password" name="logpass" class="form-style mb-2" placeholder="Your Password" id="logpass" autocomplete="off" v-model="logPassword">
                        <Icon class="input-icon" icon="uil:lock-alt" />
                        <p class="text-danger errorcode m-auto" v-if="this.$store.state.loginError !== undefined">
                          {{this.$store.state.loginError}}
                        </p>
                      </div>
                      <button class="btna mt-3" @click="logIn">submit</button>
                                   
                        </div>
                      </div>
                    </div>
                <div class="card-back">
                  <div class="center-wrap">
                    <div class="section text-center">
                      <h4 class="mb-4 pb-3">Sign Up</h4>
                      <div class="form-group">
                        <input type="text" name="logid" class="form-style" placeholder="Your ID" id="logid" autocomplete="off" v-model="username"
                        @keyup="validLogin">
                        <Icon class="input-icon" icon="uil:user" />
                        <p class="text-danger errorcode m-auto" v-if="validation !== undefined">
                        {{ validation.firstError('username') }}
                        </p>
                      </div>  
                      <div class="form-group mt-2">
                        <input type="password" name="logpassword1" class="form-style" placeholder="Password" id="logpassword1" autocomplete="off" v-model="password1"
                        >
                        <p class="text-danger errorcode m-auto" v-if="validation !== undefined">
                        {{ validation.firstError('password1') }}</p>
                        <Icon class="input-icon" icon="uil:lock-alt"/>
                      </div>  
                      <div class="form-group mt-2">
                        <input type="password" name="logpassword2" class="form-style mb-2" placeholder="Password 확인" id="logpassword2" autocomplete="off" v-model="password2">
                        <Icon class="input-icon" icon="uil:check" />
                        <p class="text-danger errorcode m-auto" v-if="samePassword">
                        비밀번호가 같지 않습니다</p>
                      </div>
                      <button class="btna mt-3" @click="signUp">submit</button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
      </div>
  </div>

  </div>
</template>

<script>
import { Icon } from '@iconify/vue2';
import SimpleVueValidation from 'simple-vue-validator';

    const Validator = SimpleVueValidation.Validator;
    SimpleVueValidation.extendTemplates({
        required: '필수 입력 항목입니다.',
        length: '길이가 {0} 이어야 합니다.',
        minLength: '{0} 글자 이상이어야 합니다.',
        maxLength: '{0} 글자 이하여야 합니다.',
        digit: '숫자만 입력해주세요.',
        regex: '숫자,영대소문자로 구성되어야 합니다'
    })
  // console.log(Validator)
export default {
  name:'LoginViewtest',
  components:{
    Icon
  },
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      logId: null,
      logPassword: null,
    }
  },
  validators: {
        username: function (value) {
                // console.log(this.validation)
               
                return Validator.value(value).required().regex('^[A-Za-z0-9]*$')
            },
        password1: function (value) {
                return Validator.value(value).required().minLength(8).maxLength(15).regex('^.*(?=^.{8,15}$)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=]).*$','숫자,특수문자,영문자를 포함해야합니다');
            },
    },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    samePassword(){
      if (this.password2 !==null ){
        if (this.password1===this.password2){
          return false
        }else{
          return true
        }
      } 
      return 0
    }
  },
  methods: {
    validLogin(){
      
    },
    validPassword1(){
      // console.log('pass')
    },
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username: username,
        password1: password1,
        password2: password2,
      }

      this.$store.dispatch('signUp', payload)
      
    },
    logIn() {
      const username = this.logId
      const password = this.logPassword

      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('logIn', payload)
    },
    checkLogin() {
      if (this.isLogin === true) {
        alert('이미 로그인 된 사용자입니다.')
        this.$router.push({ name: 'home'})
      }
    },
  },
  created() {
    this.checkLogin()
  }
}

</script>


<style>
@import url('https://fonts.googleapis.com/css?family=Poppins:400,500,600,700,800,900');

.errorcode{
  font-family: 'Montserrat';
font-style: normal;
font-weight: 600;
font-size: 15px;

color: #FF2E00;
}
.errorcodelog{
  font-family: 'Montserrat';
font-style: normal;
font-weight: 600;
font-size: 15px;

color: #ff4500;
}

body{
	font-family: 'Poppins', sans-serif;
	font-weight: 300;
	font-size: 15px;
	line-height: 1.7;
	color: #c4c3ca;
	background-color: #1f2029;
	overflow-x: hidden;
}
a {
	cursor: pointer;
  transition: all 200ms linear;
}
a:hover {
	text-decoration: none;
}
.link {
  color: #c4c3ca;
}
.link:hover {
  color: #3E3E3E;
}
p {
  font-weight: 500;
  font-size: 14px;
  line-height: 1.7;
}
h4 {
  font-weight: 800;
  color: #E8E8E8;
}
h6 span{
  padding: 0 20px;
  text-transform: uppercase;
  font-weight: 700;
  color: #E8E8E8;
}
.section{
  position: relative;
  width: 100%;
  display: block;
}
.full-height{
  min-height: 100vh;
}
[type="checkbox"]:checked,
[type="checkbox"]:not(:checked){
  position: absolute;
  left: -9999px;
}
.checkbox:checked + label,
.checkbox:not(:checked) + label{
  position: relative;
  display: block;
  text-align: center;
  width: 60px;
  height: 16px;
  border-radius: 8px;
  padding: 0;
  margin: 10px auto;
  cursor: pointer;
  background-color: #3E3E3E;
}
.checkbox:checked + label:before,
.checkbox:not(:checked) + label:before{
  position: absolute;
  display: block;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  color: #3E3E3E;
  background-color: #FFC0CB;
  font-family: 'unicons';
  content: '\eb4f';
  z-index: 20;
  top: -10px;
  left: -10px;
  line-height: 36px;
  text-align: center;
  font-size: 24px;
  transition: all 0.5s ease;
}
.checkbox:checked + label:before {
  transform: translateX(44px) rotate(-270deg);
}


.card-3d-wrap {
  position: relative;
  width: 440px;
  max-width: 100%;
  height: 400px;
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
  perspective: 800px;
  margin-top: 60px;
}
.card-3d-wrapper {
  width: 100%;
  height: 100%;
  position:absolute;    
  top: 0;
  left: 0;  
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
  transition: all 600ms ease-out; 
}
.card-front, .card-back {
  width: 100%;
  height: 100%;
  background-color: #2a2b38;
  /* background-image: url('https://s3-us-west-2.amazonaws.com/s.cdpn.io/1462889/pat.svg'); */
  background-position: bottom center;
  background-repeat: no-repeat;
  background-size: 300%;
  position: absolute;
  border-radius: 6px;
  left: 0;
  top: 0;
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
  -webkit-backface-visibility: hidden;
  -moz-backface-visibility: hidden;
  -o-backface-visibility: hidden;
  backface-visibility: hidden;
}
.card-back {
  transform: rotateY(180deg);
}
.checkbox:checked ~ .card-3d-wrap .card-3d-wrapper {
  transform: rotateY(180deg);
}
.center-wrap{
  position: absolute;
  width: 100%;
  padding: 0 35px;
  top: 50%;
  left: 0;
  transform: translate3d(0, -50%, 35px) perspective(100px);
  z-index: 20;
  display: block;
}


.form-group{ 
  position: relative;
  display: block;
    margin: 0;
    padding: 0;
}
.form-style {
  padding: 13px 20px;
  padding-left: 55px;
  height: 48px;
  width: 100%;
  font-weight: 500;
  border-radius: 4px;
  font-size: 14px;
  line-height: 22px;
  letter-spacing: 0.5px;
  outline: none;
  color: #c4c3ca;
  background-color: #1f2029;
  border: none;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
  box-shadow: 0 4px 8px 0 rgba(21,21,21,.2);
}
.form-style:focus,
.form-style:active {
  border: none;
  outline: none;
  box-shadow: 0 4px 8px 0 rgba(21,21,21,.2);
}
.input-icon {
  position: absolute;
  top: 0;
  left: 18px;
  height: 48px;
  font-size: 24px;
  line-height: 48px;
  text-align: left;
  color: #FFC0CB;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}

.form-group input:-ms-input-placeholder  {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input::-moz-placeholder  {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:-moz-placeholder  {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input::-webkit-input-placeholder  {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:focus:-ms-input-placeholder  {
  opacity: 0;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:focus::-moz-placeholder  {
  opacity: 0;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:focus:-moz-placeholder  {
  opacity: 0;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:focus::-webkit-input-placeholder  {
  opacity: 0;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}

.btna{  
  border-radius: 4px;
  height: 44px;
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  -webkit-transition : all 200ms linear;
  transition: all 200ms linear;
  padding: 0 30px;
  letter-spacing: 1px;
  display: -webkit-inline-flex;
  display: -ms-inline-flexbox;
  display: inline-flex;
  -webkit-align-items: center;
  -moz-align-items: center;
  -ms-align-items: center;
  align-items: center;
  -webkit-justify-content: center;
  -moz-justify-content: center;
  -ms-justify-content: center;
  justify-content: center;
  -ms-flex-pack: center;
  text-align: center;
  border: none;
  background-color: #1b1b22;
  color: #FFC0CB;
  box-shadow: 0 8px 24px 0 rgba(144, 144, 144, 0);
}
.btna:active,
.btna:focus{  
  background-color: #FFC0CB;
  color: #1b1b22;
  box-shadow: 0 8px 24px 0 rgba(16,39,112,.2);
}
.btna:hover{  
  background-color: #FFC0CB;
  color: #1b1b22;
  box-shadow: 0 8px 24px 0 rgba(16,39,112,.2);
}




.logo {
	position: absolute;
	top: 30px;
	right: 30px;
	display: block;
	z-index: 100;
	transition: all 250ms linear;
}
.logo img {
	height: 26px;
	width: auto;
	display: block;
}
</style>