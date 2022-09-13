pragma solidity ^0.7.0;
contract ModifierTest{
address owner;
string private name;
constructor(){
owner = msg.sender;
}
modifier onlyOwner(){
require (msg.sender == owner,&#39;Not Owner&#39;);
_;
}
function setName(string memory newName) public onlyOwner{
name = newName;
}
function getName() public view returns(string memory){
return name;
}
}
