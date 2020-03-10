<template>
  <div>
    <div>
      <a-tag>Tag 1</a-tag>
      <a-tag>
        <a href="https://github.com/vueComponent/ant-design">Link</a>
      </a-tag>
      <a-tag closable @close="log">Tag 2</a-tag>
      <a-tag closable @close="preventDefault">Prevent Default</a-tag>
    </div>
    <a-row :gutter="12">
      <a-col :span="8">
        <a-cascader
          :options="options"
          :showSearch="{ filter }"
          @change="onChange"
          placeholder="Please select"
        />
      </a-col>
      <a-col :span="4">
        <a-button>Add</a-button>
      </a-col>
      <a-col :span="4">
        <a-popover
          placement="bottom"
          title="Create a new Favlist or Section"
          trigger="click"
          v-model="visible"
        >
          <a-form slot="content" :form="form" @submit="handleSubmit">
            <a-form-item label="Title" :label-col="{ span: 5 }" :wrapper-col="{ span: 12 }">
              <a-input
                v-decorator="['note', { rules: [{ required: true, message: 'Please input your note!' }] }]"
              />
              <a-button type="primary" html-type="submit">Submit</a-button>
            </a-form-item>
          </a-form>
          <a @click="hide" slot="content">Close</a>
          <a-button>New</a-button>
        </a-popover>
      </a-col>
    </a-row>
  </div>
</template>
<script>
export default {
  name: 'PostLinkToFavlist',
  data() {
    return {
      inputValue: '',
      visible: false,
      options: [
        {
          value: 'zhejiang',
          label: 'Zhejiang',
          children: [
            {
              value: 'hangzhou',
              label: 'Hangzhou',
              children: [
                {
                  value: 'xihu',
                  label: 'West Lake',
                },
                {
                  value: 'xiasha',
                  label: 'Xia Sha',
                  disabled: true,
                },
              ],
            },
          ],
        },
        {
          value: 'jiangsu',
          label: 'Jiangsu',
          children: [
            {
              value: 'nanjing',
              label: 'Nanjing',
              children: [
                {
                  value: 'zhonghuamen',
                  label: 'Zhong Hua men',
                },
              ],
            },
          ],
        },
      ],
    };
  },
  methods: {
    hide() {
      console.log(111);
      this.visible = false;
    },
    onChange(value, selectedOptions) {
      console.log(value, selectedOptions);
    },
    filter(inputValue, path) {
      return path.some(
        option =>
          option.label.toLowerCase().indexOf(inputValue.toLowerCase()) > -1
      );
    },
  },
  mounted() {
    this.$nextTick(() => {
      // To disabled submit button at the beginning.
      this.form.validateFields();
    });
  },
};
</script>