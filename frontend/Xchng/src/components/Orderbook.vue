<script setup lang="ts">
import {reactive} from 'vue';
import axios from 'axios';

import Orders from './Orders.vue'

var x = reactive({bids:0, asks:null});

axios.get("http://localhost:5000/orderbook")
  .then((response) => {

    x.bids = response.data['bids']
    x.asks = response.data['asks']

  })
  .catch((error) => {console.log(error);});

</script>
<!-- <Suspense> -->

  <template>
      <div class="orderbook">
          <div class="asksTable">Asks</div>

          <div class="asks"><Orders v-bind:title="x['asks']" side="ASK"/></div>

          <!-- <div class="mutualData">Mutual data</div> -->

          <div class="bidsTable">Bids</div>

          <div class="bids"><Orders v-bind:title="x['bids']" side="BID"/></div>
      </div>
  </template>

<!-- </Suspense> -->



<style>



</style>