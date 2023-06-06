<script setup lang="ts">
import {reactive} from 'vue';
var hi = 10;
var x = reactive({"id":1})

function test() {
    x.id--
}

function increase() {x.id++}

</script>

<template>
    <div class="variable">
        <h1>{{ x.id }}</h1>
        <button v-on:click="increase">Increase</button>
        <button @click="test">Decrease</button>
    </div>

</template>


<style>
</style>