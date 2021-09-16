<template>
  <div class="login" clearfix>
    <div class="login-wrap">
      <el-row type="flex" justify="center">
        <el-form ref="loginForm" :model="user" :rules="rules" status-icon label-width="80px">
          <h3>登录</h3>
          <hr>
          <el-form-item prop="uuid" label="账号">
            <el-input v-model="user.uuid" placeholder="请输入账号或手机号" prefix-icon></el-input>
          </el-form-item>
          <el-form-item id="password" prop="password" label="密码">
            <el-input v-model="user.password" show-password placeholder="请输入密码"></el-input>
          </el-form-item>
          <router-link to="/">找回密码</router-link>
          <router-link to="/sanford/user/register">注册账号</router-link>
          <el-form-item>
            <el-button type="primary" icon="el-icon-upload" @click="userLogin()">登 录</el-button>
          </el-form-item>
        </el-form>
      </el-row>
    </div>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: "UserLogin",
  data() {
    return {
      user: {
        uuid: "",
        password: ""
      }
    };
  },
  created() {
  },
  methods: {
    userLogin() {
      if (!this.user.uuid) {
        this.$message.error("请输入账号");
        return;
      } else if (!this.user.password) {
        this.$message.error("请输入密码");
        return;
      } else {
        axios
          .post('http://127.0.0.1:8000/user/login', {
            uuid: this.user.uuid,
            password: this.user.password
          })
          .then(response => {
            var res = response.data
            console.log(res);
            if (res.is_succ === true) {
              localStorage.setItem("token", res.data.token);
              this.$message.success("登录成功");
              this.$router.push({path: "/sanford"});
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
.login {
  width: 100%;
  height: 740px;
  /*background: url("../assets/images/bg1.png") no-repeat;*/
  background-size: cover;
  overflow: hidden;
}

.login-wrap {
  /*background: url("../assets/images/login_bg.png") no-repeat;*/
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
