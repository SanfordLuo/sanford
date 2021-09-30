<template>
  <el-container>
    <el-button type="primary" icon="el-icon-edit" @click="dialogFormVisible = true">修改头像</el-button>
    <el-dialog :visible.sync="dialogFormVisible">


      <el-upload
        class="avatar-uploader"
        accept=".jpg,.jpeg,.png,.JPG,.JPEG"
        action="https://jsonplaceholder.typicode.com/posts/"
        :auto-upload="false"
        :show-file-list="false"
        :on-change="changePictureUpload">
        <img v-if="imageUrl" :src="imageUrl" class="avatar">
        <i v-else class="el-icon-plus avatar-uploader-icon"></i>
      </el-upload>


      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="submitUpload">确 定</el-button>
      </div>
    </el-dialog>
  </el-container>

</template>

<script>
export default {
  name: "Test",
  data() {
    return {
      imageUrl: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png',
      dialogFormVisible: false,
      file: null,
    };
  },
  methods: {
    changePictureUpload(file) {
      this.imageUrl = URL.createObjectURL(file.raw)
      this.file = file
      console.log('aaaaa', this.file)
    },
    submitUpload() {
      this.dialogFormVisible = false
      console.log('bbb')
    },
  }
}
</script>

<style>
.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.avatar-uploader .el-upload:hover {
  border-color: #409EFF;
}

.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}

.avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>
