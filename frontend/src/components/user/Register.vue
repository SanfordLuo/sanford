<template>
  <div class="register" clearfix>
    <div class="register-wrap">
      <el-row type="flex" justify="center">
        <el-form ref="registerForm" :model="user" :rules="rules" status-icon label-width="80px">
          <h3>注册</h3>
          <hr>
<!--          <el-form-item prop="username" label="用户名">-->
<!--            <el-input v-model="user.username" placeholder="请输入用户名(可选)" prefix-icon></el-input>-->
<!--          </el-form-item>-->
          <el-form-item prop="phone" label="手机号">
            <el-input v-model="user.phone" placeholder="请输入手机号" prefix-icon></el-input>
          </el-form-item>
          <el-form-item id="password" prop="password" label="密码">
            <el-input v-model="user.password" show-password placeholder="请输入密码"></el-input>
          </el-form-item>
          <router-link to="/sanford/user/login">登录账号</router-link>
          <el-form-item>
            <el-button type="primary" icon="el-icon-upload" @click="userRegister()">注 册</el-button>
          </el-form-item>
        </el-form>
      </el-row>
    </div>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: "UserRegister",
  data() {
    return {
      user: {
        username: null,
        phone: null,
        password: null
      }
    };
  },
  created() {
  },
  methods: {
    userRegister() {
      if (!this.user.phone) {
        this.$message.error("请输入手机号！");
        return;
      } else if (!this.user.password) {
        this.$message.error("请输入密码！");
        return;
      } else {
        axios
          .post('http://127.0.0.1:8000/user/register', {
            username: this.user.username,
            phone: this.user.phone,
            password: this.user.password
          })
          .then(response => {
            var res = response.data
            console.log(res);
            if (res.is_succ === true) {
              this.$router.push({path: "/sanford/user/login"});
            } else {
              console.log(res.message)
              this.$message.error(res.message)
            }
          });
      }
    }
  }
};
</script>


<style scoped>
.register {
  width: 100%;
  height: 740px;
  /*background: url("../assets/images/bg1.png") no-repeat;*/
  background-size: cover;
  overflow: hidden;
}

.register-wrap {
  /*background: url("../assets/images/register_bg.png") no-repeat;*/
  background-size: cover;
  width: 400px;
  height: 300px;
  margin: 215px auto;
  overflow: hidden;
  padding-top: 10px;
  line-height: 40px;
}

#password {
  margin-bottom: 5px;
}

h3 {
  color: #0babeab8;
  font-size: 24px;
}

hr {
  background-color: #444;
  margin: 20px auto;
}

a {
  text-decoration: none;
  color: #aaa;
  font-size: 15px;
}

a:hover {
  color: coral;
}

.el-button {
  width: 80%;
  margin-left: -50px;
}
</style>
