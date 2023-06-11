<script setup lang="ts">



function buy(){
    document.getElementById("price").value = ""
    document.getElementById("size").value = ""
}

function sell() {
    document.getElementById("price").value = ""
    document.getElementById("size").value = ""
}

</script>

<template>
    <form>
        <label for="price">Price</label><br>
        <input type="number" id="price" name="price"><br>
        <label for="size">Size</label><br>
        <input type="number" id="size" name="size">
        <br/>
        <button type="button" @click="buy()">Buy</button>
        <button type="button" @click="sell()">Sell</button>
    </form>
</template>