<template>
  <div class="user">
    <el-row display="margin-top:10px">
      <el-input v-model="input" placeholder="请输入user_id"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-button type="primary" icon="el-icon-search" @click="getUser()" style="float:left; margin: 2px;">查询账户</el-button>
      <el-button type="danger" disabled style="float:left; margin: 2px;">注销账户</el-button>
    </el-row>
    <el-row>
      <el-table :data="userInfo" style="width: 100%" border>
        <el-table-column prop="uuid" label="账户" min-width="100">
          <template slot-scope="scope"> {{ scope.row.uuid }}</template>
        </el-table-column>
        <el-table-column prop="username" label="用户名" min-width="100">
          <template slot-scope="scope"> {{ scope.row.username }}</template>
        </el-table-column>
      </el-table>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "User",
  data() {
    return {
      input: '',
      userInfo: []
    }
  },
  mounted: function () {
    this.getUser()
  },
  methods: {
    getUser() {
      this.$http.get('http://127.0.0.1:8000/user/center?user_id=' + this.input)
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.is_succ === true) {
            this.userInfo = this.userInfo.concat(res['data'])
          } else {
            this.$message.error('查询用户失败')
            console.log(res['message'])
          }
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
