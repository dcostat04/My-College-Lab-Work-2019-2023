pragma solidity ^0.5.0;
contract EmployeeRecs {
mapping(uint => string) public employeeRecordMap;
mapping(uint => mapping(string => bool)) attendanceMap;
function employeeEntry(string memory name,uint id) public {
employeeRecordMap[id] = name;
}
function enterStatus(string memory _day,uint id,bool isPresent) public{
attendanceMap[id][_day] = isPresent;
}
function getStatus(string memory _day,uint id) public view returns (bool){
return attendanceMap[id][_day];
}
}
