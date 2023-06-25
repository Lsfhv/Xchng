<script setup lang="ts">

function clearInputAndReload() { 
    document.getElementById("price").value = ""
    document.getElementById("size").value = ""
    document.getElementById("name").value = ""
    window.location.reload()
}

function getInputs() {
    var price = document.getElementById("price").value 
    var size = document.getElementById("size").value 
    var name = document.getElementById("name").value
    return [price, size, name]
}

async function placeOrder(price: number, size: number, side: string, userId: string){
    console.log(price, size, side, userId);
    await fetch('http://127.0.0.1:5000/placeorder', {
    method: 'PUT',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ "price":Number(price), "size":Number(size), "side":side, "userId":userId })
    })
   .then(response => response.json())
   .then(response => console.log(JSON.stringify(response)))
}

function buy(){
    var lst = getInputs()
    placeOrder(lst[0], lst[1], "BID", lst[2])

    clearInputAndReload()
}

async function sell() {
    var lst = getInputs()

    console.log(lst)
    await placeOrder(lst[0], lst[1], "ASK", lst[2])

    clearInputAndReload()
}

</script>

<template>
    <form>
        <label for="price">Price</label><br>
        <input type="number" id="price" name="price"><br>
        <label for="size">Size</label><br>
        <input type="number" id="size" name="size"><br>
        <label for="name">Name</label><br>
        <input type="text" id="name" name="name">
        <br/>
        <br><br>
        <button type="button" @click="buy()">Buy</button>
        <button type="button" @click="sell()">Sell</button>
    </form>
</template>