async function Orderbook() {
  const items = await fetch("http://127.0.0.1:5000/pricelevels");
  console.log(items);
  return <h1>Orderbook</h1>;
}

export default Orderbook;
