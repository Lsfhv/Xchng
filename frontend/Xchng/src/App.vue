<script setup lang="ts">
import { reactive } from 'vue'
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import Orderbook from './components/Orderbook.vue';
import Navbar from './components/Navbar.vue'

// export default {
//   data() {return {title:"hi"}}
// }

</script>

<template>
  <!-- <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div>
  </header> -->

  <main>
    <div id="mm">
      <div>hi</div>
      <div><Orderbook/></div>
    </div>
  </main>

</template>

<style scoped>

baka {
  font-size: 20px;
}

#mm {
  display: flex;
  align-items: stretch;
  gap: 10px;
  justify-content: space-between;
}

/* header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}

h1 {
  display: inline-block;
  border-bottom: 1px solid #0e0e0f;
  padding-top: 100px;
} */
</style>
