<template>
  <div>
    <el-col :span="2">
      <el-menu
        :default-active="this.$route.path"
        router mode="horizontal"
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b">
        <el-menu-item v-for="(item,i) in navList" :key="i" :index="item.name">
          <template slot="title">
            <i class="el-icon-s-platform"></i>
            <span> {{ item.navItem }}</span>
          </template>

        </el-menu-item>


      </el-menu>
    </el-col>

    <router-view class="menu-right"/>

  </div>
</template>
<script>
export default {
  data() {
    return {
      navList: [
        {name: '/', navItem: '主页页面'},
        {name: '/user', navItem: '个人中心'},
        {name: '/news', navItem: '新闻页面'},
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

<style>
.menu-right {
  margin-left: 200px;
}

</style>
