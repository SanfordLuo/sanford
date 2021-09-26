<template>
  <div class="center">
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
              <el-col :span="12">手机号:</el-col>
              <el-col :span="12">{{ userInfo.phone }}</el-col>
            </el-row>
            <el-row>
              <el-col :span="12">邮箱号:</el-col>
              <el-col :span="12">{{ userInfo.email }}</el-col>
            </el-row>
            <el-row>
              <el-col :span="12">所在省份:</el-col>
              <el-col :span="12">{{ userInfo.province }}</el-col>
            </el-row>
            <el-row>
              <el-col :span="12">所在市区:</el-col>
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

    <el-container>
      <el-button type="primary" icon="el-icon-edit" @click="dialogFormVisibleBasic = true">修改基本信息</el-button>
      <el-dialog title="修改基本信息" :visible.sync="dialogFormVisibleBasic">
        <el-form :model="newUserInfo">
          <el-form-item label="用户名" :label-width="formLabelWidth">
            <el-input v-model="newUserInfo.username" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="省份" :label-width="formLabelWidth">
            <el-input v-model="newUserInfo.province" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="市区" :label-width="formLabelWidth">
            <el-input v-model="newUserInfo.city" auto-complete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisibleBasic = false, refresh(newUserInfo)">取 消</el-button>
          <el-button type="primary" @click="updateUser('basic')">确 定</el-button>
        </div>
      </el-dialog>

      <el-button type="primary" icon="el-icon-edit" @click="dialogFormVisiblePassword = true">修改密码</el-button>
      <el-dialog title="修改密码" :visible.sync="dialogFormVisiblePassword">
        <el-form :model="newUserInfo">
          <el-form-item label="旧密码" :label-width="formLabelWidth">
            <el-input v-model="newUserInfo.oldPassword" show-password auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="新密码" :label-width="formLabelWidth">
            <el-input v-model="newUserInfo.password" show-password auto-complete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisiblePassword = false">取 消</el-button>
          <el-button type="primary" @click="updateUser('password')">确 定</el-button>
        </div>
      </el-dialog>

      <el-button type="primary" icon="el-icon-edit" @click="dialogFormVisiblePhone = true">修改手机号</el-button>
      <el-dialog title="修改手机号" :visible.sync="dialogFormVisiblePhone">
        <el-form :model="newUserInfo">
          <el-form-item label="旧手机号" :label-width="formLabelWidth">
            <el-input v-model="newUserInfo.oldPhone" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="新手机号" :label-width="formLabelWidth">
            <el-input v-model="newUserInfo.phone" auto-complete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisiblePhone = false">取 消</el-button>
          <el-button type="primary" @click="updateUser('phone')">确 定</el-button>
        </div>
      </el-dialog>

      <el-button type="primary" icon="el-icon-edit" @click="dialogFormVisibleEmail = true">修改/添加 邮箱号</el-button>
      <el-dialog title="修改/添加 邮箱号" :visible.sync="dialogFormVisibleEmail">
        <el-form :model="newUserInfo">
          <el-form-item label="旧邮箱号" :label-width="formLabelWidth">
            <el-input v-model="newUserInfo.oldEmail" placeholder="仅修改邮箱时填" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="新邮箱号" :label-width="formLabelWidth">
            <el-input v-model="newUserInfo.email" auto-complete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisibleEmail = false">取 消</el-button>
          <el-button type="primary" @click="updateUser('email')">确 定</el-button>
        </div>
      </el-dialog>

      <el-button type="primary" icon="el-icon-edit" @click="dialogFormVisibleEmailStatus = true">激活邮箱</el-button>
      <el-dialog title="激活邮箱" :visible.sync="dialogFormVisibleEmailStatus">
        <el-main>确认激活邮件?</el-main>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisibleEmailStatus = false">取 消</el-button>
          <el-button type="primary" @click="updateUser('email_status')">确 定
          </el-button>
        </div>
      </el-dialog>

      <el-button type="primary" icon="el-icon-edit" @click="dialogFormVisibleIdCard = true">实名认证</el-button>
      <el-dialog title="实名认证" :visible.sync="dialogFormVisibleIdCard">
        <el-form :model="newUserInfo">
          <el-form-item label="身份证号" :label-width="formLabelWidth">
            <el-input v-model="newUserInfo.idCard" auto-complete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisibleIdCard = false">取 消</el-button>
          <el-button type="primary" @click="updateUser('id_card')">确 定</el-button>
        </div>
      </el-dialog>

      <el-button type="primary" icon="el-icon-delete" @click="userLogout()">退出登录</el-button>
    </el-container>

  </div>

</template>

<script>
import axios from "axios"
import config from "@/../static/config.json"

export default {
  inject: ['reload'],
  name: "UserCenter",
  data() {
    return {
      input: '',
      userInfo: {},
      newUserInfo: {},
      default: {
        'username': '网友',
        'avatar': 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
      },
      dialogFormVisibleBasic: false,
      dialogFormVisiblePassword: false,
      dialogFormVisiblePhone: false,
      dialogFormVisibleEmail: false,
      dialogFormVisibleEmailStatus: false,
      dialogFormVisibleIdCard: false,
      formLabelWidth: '120px'
    }
  },
  mounted: function () {
    this.getUser()
  },
  methods: {
    getUser() {
      const header = {'Authorization': 'Token ' + localStorage.getItem('token')}
      axios.get(config.user_center_url, {'headers': header})
        .catch(error => {
          console.log(error.response)
          this.$message.error(error.message)
        })
        .then(response => {
          var res = response.data
          console.log(res);
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
            console.log(res.message)
            this.$message.error(res.message)
          }
        })
    },

    userLogout() {
      const header = {'Authorization': 'Token ' + localStorage.getItem('token')}
      axios.get(config.user_logout_url, {'headers': header})
        .catch(error => {
          console.log(error.response)
          localStorage.removeItem('token')
          localStorage.removeItem('username')
          this.$message.success('已退出登录')
          this.$router.push({path: "/sanford"});
        })
        .then(response => {
          var res = response.data
          console.log(res);
          if (res.is_succ === true) {
            localStorage.removeItem('token')
            localStorage.removeItem('username')
            this.$message.success('已退出登录')
            this.$router.push({path: "/sanford"});
          } else {
            console.log(res.message)
            this.$message.error(res.message)
          }
        })
    },

    updateUser(put_type) {
      const newUserInfo = this.newUserInfo
      this.$set(newUserInfo, 'put_type', put_type)
      const header = {'Authorization': 'Token ' + localStorage.getItem('token')}
      console.log(newUserInfo)
      console.log(header)
      axios
        .put(config.user_center_url, newUserInfo, {'headers': header})
        .then(response => {
            var res = response.data
            console.log(res);
            if (res.is_succ === true) {
              this.refresh(newUserInfo)
              this.$message.success(res.message);
            } else {
              console.log(res.message)
              this.$message.error(res.message)
            }
          }
        )
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
    },

    refresh(newUserInfo) {
      this.dialogFormVisibleBasic = false;
      this.dialogFormVisiblePassword = false;
      this.dialogFormVisiblePhone = false;
      this.dialogFormVisibleEmail = false;
      this.dialogFormVisibleEmailStatus = false;
      this.dialogFormVisibleIdCard = false;
      if (newUserInfo.username) {
        localStorage.setItem("username", newUserInfo.username);
      }
      this.reload()
    }
  }
}
</script>

<style scoped>

</style>
