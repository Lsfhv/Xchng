<script setup lang="ts">
import {reactive} from 'vue';

var x = [10,11]


</script>

<template>
    <div class="orderbook">
        <div class="bidsTable">bids table</div>

        <div class="bids">Bids</div>

        <div class="mutualData">Mutual data</div>

        <div class="asksTable">asksTable</div>

        <div class="asks"><div class="container">
  <div class="text">ACTION ITEMS</div>
  <div class="box">
    <ul>
      <li>something</li>
      <li>something</li>
      <li>something</li>
      <li>something</li>
      <li>something</li>
      <li>something</li>
      <li>something</li>
      <li>something</li>
      <li>something</li>
    </ul>
  </div>
  <a href="www.something.com" class="link-item" onclick="document.querySelector('.box').scrollTop = 10000; return false;">GO TO THE LAST ITEM</a>
</div></div>
    </div>
</template>





<style>

.orderbook {
    color: blue;
}

.container {
  position: relative;
  float: right;
  width: 74.4%;
  height: 150px;
  background-color: rgb(230, 230, 233);
  margin-top: 30px;
  box-shadow: 2px 2px 2px 0px rgba(0, 0, 0, 0.1), 0 4px 4px 0 rgba(0, 0, 0, 0.15);
  text-align: left;
  border-radius: 4px;
}

.text {
  position: fixed;
  font-size: 12px;
  font-weight: 600;
  font-family: 'Open Sans', sans-serif;
  color: rgb(116, 124, 142);
  float: left;
  padding: 10px 0px 0px 40px;
}

.link-item {
  position: absolute;
  top: 15px;
  width: 100%;
  font-weight: 400;
  font-size: 12px;
  font-family: 'Open Sans', sans-serif;
  color: rgb(87, 135, 253);
  text-align: right;
  padding-right: 40px;
  text-decoration: none;
}


</style>