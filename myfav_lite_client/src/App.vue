<template>
  <a-layout>
    <a-layout>
      <a-layout-sider width="200" style="background: #fff">
        <NavLeft />
      </a-layout-sider>
      <a-layout style="padding: 0 24px 24px">
        <a-layout-content
          :style="{ background: '#fff', padding: '24px', margin: 0, minHeight: '280px' }"
        >
          <router-view />
        </a-layout-content>
      </a-layout>
    </a-layout>
  </a-layout>
</template>

<script>
// @ is an alias to /src
import NavLeft from '@/components/NavLeft.vue';

export default {
  name: 'App',
  components: {
    NavLeft,
  },
};
</script>

<style lang="stylus" scoped></style>

<style lang="stylus">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
