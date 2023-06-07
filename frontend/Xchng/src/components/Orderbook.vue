<script setup lang="ts">
import {reactive} from 'vue';
import axios from 'axios';

import Orders from './Orders.vue'

var x = reactive({data:null});

axios.get("http://localhost:5000/orderbook")
  .then((response) => {
    x.data = response.data
  })
  .catch((error) => {console.log(error);});

</script>

<template>
    <div class="orderbook">
        <div class="bidsTable">Bids table</div>

        <div class="bids"><Orders/></div>

        <div class="mutualData">Mutual data</div>

        <div class="asksTable">{{ x }}</div>

        <div class="asks"><Orders/></div>
    </div>
</template>





<style>



</style>