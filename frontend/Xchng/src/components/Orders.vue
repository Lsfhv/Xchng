<script setup lang="ts">
var props = defineProps(['title', 'side'])
</script>

<template>
<div class="box">
    <ul class="orderss" v-bind:style="[(props.side == 'ASK') ? 'color:red' : 'color:green']">
      <li v-for="item in title">
        {{ item['price'] }}, {{ item['size'] }}
      </li>
    </ul>
  </div>
</template>

<style>
.orderss {
    width:300px;
    height: 400px;
    overflow:auto;
    list-style: none;
}

</style>