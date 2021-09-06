<template>
  <div class="user">
    <el-container>
      <el-header>个人中心</el-header>
      <el-container>
        <el-aside width="400px">
          <el-col :span="12">
            <div class="sub-title"></div>
            <div>
              <div>
                <el-avatar :size="100" :src="userInfo.avatar"></el-avatar>
              </div>
              <span>{{ userInfo.username }}</span>
            </div>

            <el-row>
              <el-col :span="12">账号:</el-col>
              <el-col :span="12">{{ userInfo.uuid }}</el-col>
            </el-row>
            <el-row>
              <el-col :span="12">手机:</el-col>
              <el-col :span="12">{{ userInfo.phone }}</el-col>
            </el-row>
            <el-row>
              <el-col :span="12">邮箱:</el-col>
              <el-col :span="12">{{ userInfo.email }}</el-col>
            </el-row>
            <el-row>
              <el-col :span="12">所在省:</el-col>
              <el-col :span="12">{{ userInfo.province }}</el-col>
            </el-row>
            <el-row>
              <el-col :span="12">所在市:</el-col>
              <el-col :span="12">{{ userInfo.city }}</el-col>
            </el-row>
            <el-row>
              <el-col :span="12">邮箱状态:</el-col>
              <el-col :span="12">{{ userInfo.email_status }}</el-col>
            </el-row>
            <el-row>
              <el-col :span="12">用户状态:</el-col>
              <el-col :span="12">{{ userInfo.real_status }}</el-col>
            </el-row>
            <el-row>
              <el-col :span="12">注册时间:</el-col>
              <el-col :span="12">{{ userInfo.register_time }}</el-col>
            </el-row>
            <el-row>
              <el-col :span="12">认证时间:</el-col>
              <el-col :span="12">{{ userInfo.real_time }}</el-col>
            </el-row>

          </el-col>
        </el-aside>
      </el-container>
    </el-container>

  </div>
</template>

<script>
export default {
  name: "User",
  data() {
    return {
      input: '',
      userInfo: {},
      default: {
        'username': '网友',
        'avatar': 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
      }
    }
  },
  mounted: function () {
    this.getUser()
  },
  methods: {
    getUser() {
      this.$http.get('http://127.0.0.1:8000/user/center?user_id=8')
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          if (res.is_succ === true) {
            this.userInfo = res.data
            if (this.userInfo.username == null) {
              this.userInfo.username = this.default.username
            }
            if (this.userInfo.avatar == null) {
              this.userInfo.avatar = this.default.avatar
            }
            if (this.userInfo.register_timestamp !== null) {
              this.userInfo.register_time = this.timestampToTime(this.userInfo.register_timestamp)
            }
            if (this.userInfo.real_timestamp !== null) {
              this.userInfo.real_time = this.timestampToTime(this.userInfo.real_timestamp)
            }
          } else {
            this.$message.error(res.message)
          }
        })
    },

    timestampToTime(timestamp) {
      var date = new Date(timestamp)
      var Y = date.getFullYear() + '-';
      var M = (date.getMonth() + 1 < 10 ? '0' + (date.getMonth() + 1) : date.getMonth() + 1) + '-';
      var D = (date.getDate() < 10 ? '0' + (date.getDate()) : date.getDate()) + ' ';
      var h = (date.getHours() < 10 ? '0' + (date.getHours()) : date.getHours()) + ':';
      var m = (date.getMinutes() < 10 ? '0' + (date.getMinutes()) : date.getMinutes()) + ':';
      var s = (date.getSeconds() < 10 ? '0' + (date.getSeconds()) : date.getSeconds());
      return Y + M + D + h + m + s;
    }
  }
}
</script>

<style scoped>

</style>
