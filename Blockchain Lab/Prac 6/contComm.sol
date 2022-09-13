pragma solidity ^0.8.0;
contract Calculator{
function add (int a,int b) external pure returns(int){
return a+b;
}
function multiply (int a,int b) external pure returns(int){
return a*b;
}
}
contract calcTest{
Calculator calc = new Calculator();
function FourTimesSix() external view returns(int){
return calc.multiply(4,6);
}
function FourPlusSix() external view returns(int){
return calc.add(4,6);
}

}
