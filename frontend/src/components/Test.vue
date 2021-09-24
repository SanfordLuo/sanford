<template>
  <el-container>
    <el-button type="primary" icon="el-icon-edit" @click="dialogFormVisible = true">修改基本资料</el-button>
    <el-dialog title="基本信息" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="用户名" :label-width="formLabelWidth">
          <el-input v-model="form.name" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="用户名哈哈哈" :label-width="formLabelWidth">
          <el-input v-model="form.namehhh" auto-complete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
      </div>
    </el-dialog>
  </el-container>

</template>

<script>
export default {
  data() {
    return {
      dialogFormVisible: false,
      form: {
        name: '',
        namehhh: '',
      },
      formLabelWidth: '120px'
    };
  }
};
</script>
