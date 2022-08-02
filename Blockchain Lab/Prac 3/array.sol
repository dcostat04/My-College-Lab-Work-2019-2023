pragma solidity >=0.4.0 <0.9.0;
contract Array {
    uint[] arr;

    function getArrayElements(uint i) public view returns (uint) {
        return arr[i];
    }
    function getArray() public view returns (uint[] memory) {
        return arr;
    }

    function push(uint i) public {
        arr.push(i);
    }

    function pop() public {
        arr.pop();
    }

    function remove(uint index) public {
        delete arr[index];
    }

}
