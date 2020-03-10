<template>
  <wl-card hoverable>
    <wl-textarea outlined label="Post Link" style=" --textarea-max-height: 300px;"></wl-textarea>
  </wl-card>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String,
  },
};
</script>

<style scoped lang="stylus"></style>
