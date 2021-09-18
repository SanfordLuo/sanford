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
    </el-row>

    <el-footer>&copy; 2021 Sanford</el-footer>

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

.el-row {
  position: fixed;
  top: 0;
  width: 100%
}

.el-footer {
  background-color: #252d36;
  color: #ffc852;
  text-align: center;
  line-height: 60px;
  position: fixed;
  bottom: 0;
  width: 100%
}

</style>
