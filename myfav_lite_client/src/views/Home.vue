<template>
  <div>
    <wl-nav>
      <div slot="left">
        <wl-button slot="left" fab flat inverted>
          <wl-icon alt="menu">menu</wl-icon>
        </wl-button>
      </div>
      <h1 slot="title">Page title</h1>
      <div slot="right">
        <a href="#">Link 1</a>
        <a href="#">Link 2</a>
      </div>
    </wl-nav>
    <div class="favlist-list">
      <wl-tab-group vertical style="text-align: left">
        <wl-tab>
          <wl-icon slot="before">supervised_user_circle</wl-icon>
          <span>Index</span>
        </wl-tab>
        <wl-tab>
          <wl-icon slot="before">verified_user</wl-icon>
          <span>Cats</span>
        </wl-tab>
      </wl-tab-group>
      <!-- <wl-list-item active>
        <wl-icon slot="before">account_circle</wl-icon>
        <span slot="after">5 days</span>
        <wl-title level="4" style="margin: 0">Listname</wl-title>
      </wl-list-item>
      <wl-list-item clickable>
        <wl-icon slot="before">account_circle</wl-icon>
        <span slot="after">5 days</span>
        <wl-title level="4" style="margin: 0">Listname</wl-title>
      </wl-list-item>-->
    </div>
    <PostLink msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
// @ is an alias to /src
import PostLink from '@/components/PostLink.vue';

export default {
  name: 'Home',
  components: {
    PostLink,
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
