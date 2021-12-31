<template>
  <el-form ref="ruleFormPersonalInfo" :model="ruleFormPersonalInfo" label-width="80px">
    <el-form-item prop="url">
      <div class="demo-image">
        <div class="block">
          <el-image id="image" style="width: 100px; height: 100px" :src="ruleFormPersonalInfo.imageUrl+'?'+Date()"
                    fit="cover"></el-image>
          <el-button type="text" title="注意！一旦上传则直接修改" onmouseover="" @click="uploadProfile = true">修改头像</el-button>
        </div>
      </div>

      <el-dialog title="上传头像" width="420px" :visible.sync="uploadProfile" :before-close="beforeDialogClose">
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
          :on-change="onchangeUpload"
        >
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过2MB</div>
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

  </el-form>

</template>

<script>
import axios from "axios"
import serviceUrl from "@/common/serviceUrl"

export default {
  name: "Test",
  data() {
    return {
      ruleFormPersonalInfo: {
        imageUrl: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
      },
      uploadProfile: false,
      confirmProfile: false,
      previewImgURL: '',


    };
  },
  methods: {
    /* 上传头像对话框 */
    beforeDialogClose(done) { // 用户临时退出上传头像，应清空
      this.$refs.upload.clearFiles()
      done()
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

    confirmCancel() {
      this.confirmProfile = false
      this.uploadProfile = true
      this.previewImgURL = null
      this.$refs.upload.clearFiles()
    },

    confirmSubmit() {
      // post上传头像 存到数据库，显示在个人中心
      this.$refs.upload.submit()
    },

    cancelAvatarUpload() { // 用户临时退出上传头像，应清空
      this.uploadProfile = false
      this.$refs.upload.clearFiles()
    },


    // 自定义上传方法
    uploadPicturePost(file) {
      const newUserInfo = new FormData
      newUserInfo.append('put_type', 'avatar')
      newUserInfo.append('file', file.file)
      const header = {'Authorization': 'Token ' + localStorage.getItem('token')}
      console.log(newUserInfo)
      console.log(header)
      axios
        .put(serviceUrl.userCenter, newUserInfo, {'headers': header})
        .then(response => {
            var res = response.data
            console.log(res);
            if (res.is_succ === true) {
              this.confirmProfile = false
              this.uploadProfile = false
              this.$refs.upload.clearFiles()
              this.refresh(newUserInfo)
              this.$message.success(res.message);
            } else {
              console.log(res.message)
              this.$message.error(res.message)
            }
          }
        )
    },




  }
}
</script>

<!--<style>-->
<!--.avatar-uploader .el-upload {-->
<!--  border: 1px dashed #d9d9d9;-->
<!--  border-radius: 6px;-->
<!--  cursor: pointer;-->
<!--  position: relative;-->
<!--  overflow: hidden;-->
<!--}-->

<!--.avatar-uploader .el-upload:hover {-->
<!--  border-color: #409EFF;-->
<!--}-->

<!--.avatar-uploader-icon {-->
<!--  font-size: 28px;-->
<!--  color: #8c939d;-->
<!--  width: 178px;-->
<!--  height: 178px;-->
<!--  line-height: 178px;-->
<!--  text-align: center;-->
<!--}-->

<!--.avatar {-->
<!--  width: 178px;-->
<!--  height: 178px;-->
<!--  display: block;-->
<!--}-->
<!--</style>-->
