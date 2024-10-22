import { useState } from "react";
import { Alert } from "./components/Alert";
import { Buttons } from "./components/Buttons";

function App() {
  const handlerOnClick = () => {
    console.log("clicked");
    setAlertVisibility(true);
  };

  const [alertVisible, setAlertVisibility] = useState(false);

  const handleOnClose = () => {
    setAlertVisibility(false);
  };

  return (
    <div>
      {alertVisible && (
        <Alert onClose={handleOnClose}>This need to be set</Alert>
      )}
      <Buttons onClick={handlerOnClick} color="danger">
        testbtn
      </Buttons>
    </div>
  );
}

export default App;
