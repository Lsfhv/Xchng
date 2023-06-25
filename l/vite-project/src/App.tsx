import Navbar from "./components/Navbar";
import Orderbook from "./components/Orderbook";
import Buy from "./components/Buy";
import "./App.css";

function App() {
  return (
    <div>
      <Navbar></Navbar>
      <div className="column">
        <Orderbook></Orderbook>
      </div>
      <div className="left">
        <Buy></Buy>
      </div>
    </div>
  );
}

export default App;
