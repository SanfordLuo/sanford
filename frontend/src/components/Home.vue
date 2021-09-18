<template>
  <div class="home">
    <el-container>
      <el-menu
        :default-active="this.$route.path"
        router mode="horizontal"
        class="el-menu-demo"
        @open="handleOpen"
        @close="handleClose"
        background-color="#fff"
        text-color="#333"
        active-text-color="#0084ff">

        <el-menu-item v-for="(item,i) in leftNavList" :key="i" :index="item.name">
          <template slot="title">
            <span> {{ item.navItem }}</span>
          </template>
        </el-menu-item>

        <el-menu-item v-for="(item,i) in rightNavList" :key="i" :index="item.name" style="float:right">
          <template slot="title">
            <span> {{ item.navItem }}</span>
          </template>
        </el-menu-item>

      </el-menu>
      <el-main>这是主页</el-main>
      <el-footer>&copy; 2021 Sanford</el-footer>
    </el-container>

    <router-view/>

  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      leftNavList: [
        {name: '/', navItem: 'sanford'}
      ],
      rightNavList: [
        {name: '/home/login', navItem: '登录'},
        {name: '/home/register', navItem: '注册'},
      ]
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

.home {
  height: 100%;
}

.el-container {
  height: 100%;
}

.el-footer {
  background-color: #252d36;
  color: #ffc852;
  text-align: center;
  line-height: 60px;
}

.el-main {
  color: #333;
  text-align: center;
}

</style>
