<template>
  <a-menu
    mode="inline"
    :defaultSelectedKeys="['10']"
    :defaultOpenKeys="['sub1']"
    :style="{ height: '100%', borderRight: 0 }"
  >
    <!-- <h1>1</h1> -->
    <a-menu-item disabled>
      <h1>myfav.link</h1>
    </a-menu-item>
    <a-menu-item key="10">
      <a-icon type="pie-chart" />
      <span>Home</span>
    </a-menu-item>
    <a-menu-item key="11">
      <a-icon type="pie-chart" />
      <span>Explore</span>
    </a-menu-item>
    <a-sub-menu key="sub1">
      <span slot="title">
        <a-icon type="user" />MyLists
      </span>
      <a-menu-item key="1">option1</a-menu-item>
      <a-menu-item key="2">option2</a-menu-item>
      <a-menu-item key="3">option3</a-menu-item>
      <a-menu-item key="4">option4</a-menu-item>
    </a-sub-menu>
  </a-menu>
</template>