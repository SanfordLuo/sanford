<template>
  <div>
    <el-row :span="2">
      <el-menu
        :default-active="this.$route.path"
        router mode="horizontal"
        class="el-menu-vertical-demo"
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


      </el-menu>
    </el-row>

    <router-view/>

  </div>
</template>
<script>
export default {
  data() {
    return {
      navList: [
        {name: '/', navItem: '首页'},
        {name: '/hot', navItem: '热榜'},
        {name: '/user', navItem: '个人中心'},
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

</style>
