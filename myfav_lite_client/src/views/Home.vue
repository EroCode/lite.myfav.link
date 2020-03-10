<template>
  <div>
    <PostLink msg="Welcome to Your Vue.js App" />
    <LinkFeeds />
  </div>
</template>

<script>
// @ is an alias to /src
import PostLink from '@/components/PostLink.vue';
import LinkFeeds from '@/components/LinkFeeds.vue';

export default {
  name: 'Home',
  components: {
    PostLink,
    LinkFeeds,
  },
};
</script>

<style lang="stylus" scoped>
.favlist-list {
  float: left;
  width: 400px;
  text-align: left;
}
</style>
