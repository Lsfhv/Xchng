<script setup lang="ts">
var props = defineProps(['title', 'side'])
const data = props.title

var keys = Object.keys(data)
keys.sort()
keys.reverse();
</script>

<template>
<div class="box">
    <ol class="orderss" v-bind:style="[(props.side == 'ASK') ? 'color:red' : 'color:green;']">
      <li v-for="key in keys">
        {{ key }}, {{ data[key] }} 
       </li>
    </ol>
  </div>
</template>

<style>
.orderss {
    width:300px;
    height: 400px;
    overflow:auto;
    list-style: none;
    padding-left:0;   
}


</style>