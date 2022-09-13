//SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;
contract Lottery {
    address payable public manager;
    address payable[] public  players;
    uint public lotteryId;
    mapping (uint => address payable) lotteryHistory;

    constructor() payable {
        manager = payable(msg.sender);
        lotteryId = 1;
    }
    function enter() public payable {
        require((msg.value) > 1 ether);
        players.push(payable(msg.sender));
    }
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
    function getBalanceOfAddress() public view returns (uint) {
        return msg.sender.balance;
    }
    function random() private view returns(uint) {
        return uint(keccak256(abi.encodePacked(block.difficulty, block.timestamp,players)));
    }
    function winner() public payable restricted {
        uint index = random() % players.length;
        players[index].transfer(address(this).balance);
        lotteryHistory[lotteryId] = players[index];
        lotteryId++;
        players=new address payable [](0);
    }

    function allplayers() public view returns(address payable[] memory) {
        return players;
    }

    function getWinnerByLottery(uint lottery) public view returns (address
    payable) {
    return lotteryHistory[lottery];
    }
    modifier restricted() {
    require(msg.sender == manager);
    _ ;
    }

}
