<template>
  <div>
    <el-row :span="2">
      <el-menu
        :default-active="this.$route.path"
        router mode="horizontal"
        class="el-menu-demo"
        @open="handleOpen"
        @close="handleClose"
        background-color="#fff"
        text-color="#333"
        active-text-color="#0084ff"
        style="flex:1">
        <el-menu-item v-for="(item,i) in navList" :key="i" :index="item.name">
          <template slot="title">
            <span> {{ item.navItem }}</span>
          </template>

        </el-menu-item>

        <el-header>
          {{ username }}
        </el-header>


      </el-menu>
    </el-row>

    <router-view/>

  </div>
</template>

<script>
export default {
  name: "Sanford",
  data() {
    return {
      navList: [
        {name: '/sanford/hot', navItem: '热榜'},
        {name: '/sanford/user/center', navItem: '个人中心'},
      ],
      username: localStorage.getItem('username'),
    }
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }
  }
}
</script>

<style scoped>
.el-header {
  text-align: right;
  line-height: 60px;
  color: #6495ED;
  font-size: 15px;
  font-weight: bold
}
</style>
