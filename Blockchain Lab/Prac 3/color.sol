contract MyContract {
    enum State {red,blue,green,yellow}
    State  state;
    function setRed() public {
      state = State.red;
   }
   function setBlue() public {
      state = State.blue;
   }
   function setGreen() public {
      state = State.green;
   }
   function setYellow() public {
      state = State.yellow;
   }

    function returnState() external view returns (string memory) {
        State temp = state;
        if (temp == State.red) return "RED";
        if (temp == State.blue) return "BLUE";
        if (temp == State.green) return "GREEN";
        if (temp == State.yellow) return "YELLOW";
        return "";
    }
}
