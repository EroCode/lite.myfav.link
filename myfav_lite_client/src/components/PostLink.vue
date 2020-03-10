<template>
  <a-card title="Post a link to favlist">
    <a-button type="primary" href="#" slot="extra">Post</a-button>
    <a-form :form="form" @submit="handleSubmit">
      <a-form-item label="Post Link" :label-col="{ span: 5 }" :wrapper-col="{ span: 12 }">
        <a-textarea
          placeholder="Autosize height with minimum and maximum number of lines"
          :autosize="{ minRows: 1 }"
        />
      </a-form-item>
      <a-form-item label="To Favlist" :label-col="{ span: 5 }" :wrapper-col="{ span: 12 }">
        <PostLinkToFavlist />
      </a-form-item>
      <a-form-item label="Tags" :label-col="{ span: 5 }" :wrapper-col="{ span: 12 }">
        <div>
          <template v-for="(tag, index) in tags">
            <a-tooltip v-if="tag.length > 20" :key="tag" :title="tag">
              <a-tag
                :key="tag"
                :closable="index !== 0"
                :afterClose="() => handleClose(tag)"
              >{{`${tag.slice(0, 20)}...`}}</a-tag>
            </a-tooltip>
            <a-tag
              v-else
              :key="tag"
              :closable="index !== 0"
              :afterClose="() => handleClose(tag)"
            >{{tag}}</a-tag>
          </template>
          <a-input
            v-if="inputVisible"
            ref="input"
            type="text"
            size="small"
            :style="{ width: '78px' }"
            :value="inputValue"
            @change="handleInputChange"
            @blur="handleInputConfirm"
            @keyup.enter="handleInputConfirm"
          />
          <a-tag v-else @click="showInput" style="background: #fff; borderStyle: dashed;">
            <a-icon type="plus" />New Tag
          </a-tag>
        </div>
      </a-form-item>
      <a-form-item label="Description" :label-col="{ span: 5 }" :wrapper-col="{ span: 12 }">
        <a-textarea
          placeholder="Autosize height with minimum and maximum number of lines"
          :autosize="{ minRows: 1 }"
        />
      </a-form-item>
    </a-form>
  </a-card>
</template>

<script>
import PostLinkToFavlist from '@/components/PostLinkToFavlist.vue';

function hasErrors(fieldsError) {
  return Object.keys(fieldsError).some(field => fieldsError[field]);
}
export default {
  name: 'PostLink',
  props: {
    msg: String,
  },
  components: {
    PostLinkToFavlist,
  },
  data() {
    return {
      tags: ['Unremovable', 'Tag 2', 'Tag 3Tag 3Tag 3Tag 3Tag 3Tag 3Tag 3'],
      inputVisible: false,
      inputValue: '',
      hasErrors,
      visible: false,
      form: this.$form.createForm(this, { name: 'horizontal_login' }),
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
    filter(inputValue, path) {
      return path.some(
        option =>
          option.label.toLowerCase().indexOf(inputValue.toLowerCase()) > -1
      );
    },
    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFields((err, values) => {
        if (!err) {
          console.log('Received values of form: ', values);
        }
      });
    },
    handleClose(removedTag) {
      const tags = this.tags.filter(tag => tag !== removedTag);
      console.log(tags);
      this.tags = tags;
    },

    showInput() {
      this.inputVisible = true;
      this.$nextTick(function() {
        this.$refs.input.focus();
      });
    },

    handleInputChange(e) {
      this.inputValue = e.target.value;
    },

    handleInputConfirm() {
      const inputValue = this.inputValue;
      let tags = this.tags;
      if (inputValue && tags.indexOf(inputValue) === -1) {
        tags = [...tags, inputValue];
      }
      console.log(tags);
      Object.assign(this, {
        tags,
        inputVisible: false,
        inputValue: '',
      });
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

<style scoped lang="stylus"></style>
