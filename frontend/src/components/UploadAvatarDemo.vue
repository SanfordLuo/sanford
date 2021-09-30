<template>
  <!-- 个人信息 表单 -->
  <el-form ref="ruleFormPersonalInfo" :model="ruleFormPersonalInfo" :rules="rulesPersonalInfo" label-width="80px">
    <!-- 用户头像 -->
    <el-form-item prop="url">
      <!-- 头像显示 -->
      <div class="demo-image">
        <div class="block">
          <!-- fit值：cover 或 contain -->
          <el-image id="image" style="width: 100px; height: 100px" :src="urlBase+ruleFormPersonalInfo.url+'?'+Date()"
                    fit="cover"></el-image>
          <el-button type="text" title="注意！一旦上传则直接修改" onmouseover="" @click="uploadProfile = true">修改头像</el-button>
        </div>
      </div>
      <!-- 上传头像 dialog弹窗-->
      <el-dialog title="上传头像" width="420px" :visible.sync="uploadProfile" :before-close="beforeDialogClose">
        <!-- drag upload -->
        <el-upload
          class="upload-demo"
          ref="upload"
          drag
          accept=".jpg,.jpeg,.png,.JPG,.JPEG"
          list-type="picture"
          :multiple="false"
          :auto-upload="false"
          action="no_use"
          :http-request="uploadPicturePost"
          :before-upload="beforeAvatarUpload"
          :on-change="onchangeUpload">
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div>
        </el-upload>
        <!-- 头像预览子弹窗 -->
        <el-dialog width="30%" title="预览头像" :visible.sync="confirmProfile" append-to-body
                   :before-close="beforeDialogClose">
          确认更改头像如下吗？<br>
          <div align="center">
            <el-image style="width: 200px; height: 200px" :src="previewImgURL" fit="cover"></el-image>
          </div>
          <div slot="footer" class="dialog-footer">
            <el-button @click="confirmCancel">换一个</el-button>
            <el-button type="primary" @click="confirmSubmit">确认</el-button>
          </div>
        </el-dialog>
        <div slot="footer" class="dialog-footer">
          <el-button @click="cancelAvatarUpload">取 消</el-button>
          <!-- <el-button type="primary" @click="confirmProfile = true">打开内层 Dialog</el-button>-->
        </div>
      </el-dialog>
    </el-form-item>
    <el-form-item label="用户名" prop="name">
      <el-input v-model="ruleFormPersonalInfo.name"></el-input>
    </el-form-item>
    <el-form-item label="个人简介" prop="info">
      <el-input type="textarea" placeholder="请输入个人简介，200字以内" v-model="ruleFormPersonalInfo.info"
                :autosize="{ minRows: 5, maxRows: 5}"
                maxlength="200" show-word-limit
      ></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="personalInfoSubmit('ruleFormPersonalInfo')">确认修改</el-button>
      <!--                  <el-button>取消</el-button>-->
    </el-form-item>
  </el-form>
</template>


<script>
export default {
  name: 'Personal',
  inject: ['reload'], // 全局方法，重新加载页面
  data() {
    return {

      // 个人中心-用户资料修改
      ruleFormPersonalInfo: { // 用户资料表单
        name: this.$store.state.name,
        info: this.$store.state.info,
        url: this.$store.state.image
      },
      rulesPersonalInfo: {
        name: [
          {required: true, message: '用户名不能为空', trigger: 'blur'},
          {min: 2, max: 12, message: '长度在 2 到 12 个字符', trigger: 'blur'}
        ],
        info: [
          {required: false, message: '请输入个人简介，200字以内', trigger: 'blur'},
          {max: 200, message: '字数已经超出200！请删减', trigger: 'blur'}
        ],
        url: [
          {required: false}
        ]
      },
      // 上传头像对话框显示与否
      uploadProfile: false,
      confirmProfile: false,
      // upload-demo
      previewImgURL: '',
      urlBase: '接口url，如http://201.201.201.1',
    }
  },
  methods: {
    cancelCourseCreate() {
      alert('跳转回课程管理页面')
    },
    /* 个人信息修改表单 */
    InfoPost() {
      let notify = this.$notify
      let store = this.$store
      let _this = this
      this.$axios.post('/user/changeInformation',
        {
          'info': this.ruleFormPersonalInfo.info.toString(),
          'name': this.ruleFormPersonalInfo.name.toString()
        })
        .then(function (res) {
          console.log(res)
          // Post成功，但修改信息成功，返回相应的用户信息
          if (res.data.successful) {
            // 把res.data中的数据写入vuex
            store.dispatch('SetUserInfo', res.data.data)
            console.log(store.state)
            alert('修改信息成功！')
            // 刷新页面
            _this.reload()
            return true
          } else {
            // Post成功，但修改信息失败，返回相应的错误信息
            notify.error(
              {
                message: res.data.message
              })
          }
        })
        // Post失败
        .catch(function (err) {
          notify.error(
            {
              message: err.toString() + '失败post'
            })
        })
    },
    // 表单提交
    personalInfoSubmit(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.InfoPost()
        } else {
          this.$message.error('信息填写错误！')
          return false
        }
      })
    },
    /* 上传头像对话框 */
    beforeDialogClose(done) { // 用户临时退出上传头像，应清空
      this.$refs.upload.clearFiles()
      done()
    },
    cancelAvatarUpload() { // 用户临时退出上传头像，应清空
      this.uploadProfile = false
      this.$refs.upload.clearFiles()
    },
    beforeAvatarUpload(file) { // 大小限制
      const isLt2M = file.size / 1024 / 1024 < 2
      if (!isLt2M) {
        this.$message.error('上传头像图片大小不能超过 2MB!')
      }
      // this.previewImgURL = URL.createObjectURL(file.raw)
      // this.confirmProfile = true // 预览图片
      // alert('' + this.confirmProfile)
      return isLt2M
    },
    onchangeUpload(file) {
      // 预保存上传的图片
      this.previewImgURL = URL.createObjectURL(file.raw)
      this.confirmProfile = true // 预览图片
    },
    // 自定义上传方法
    uploadPicturePost(file) {
      let notify = this.$notify
      let img = new FormData()
      let _this = this
      img.append('image', file.file)
      this.$axios.post('/user/uploadImage', img, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
        .then(function (res) {
          // Post成功，上传图片成功
          if (res.data.successful) {
            _this.ruleFormPersonalInfo.url = res.data.data.imageUrl
            notify.success(
              {
                message: '成功修改头像'
              })
            // 关闭，并清空列表
            _this.confirmProfile = false
            _this.uploadProfile = false
            _this.$refs.upload.clearFiles()
            _this.reload() // 全局方法，重新加载页面
            return true
          } else {
            // Post成功，但上传图片失败
            notify.error(
              {
                message: res.data.message
              })
          }
        })
        // Post失败
        .catch(function (err) {
          notify.error(
            {
              message: err.toString()
            })
        })
      return false
    },
    confirmCancel() {
      this.confirmProfile = false
      this.uploadProfile = true
      this.previewImgURL = null
      this.$refs.upload.clearFiles()
    },
    confirmSubmit() {
      // post上传头像 存到数据库，显示在个人中心
      this.$refs.upload.submit()
    }
  }
}
</script>
