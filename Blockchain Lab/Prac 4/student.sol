// SPDX-License-Identifier: Unlicensed
pragma solidity >=0.4.0 <0.9.0;
contract test {
    struct Student{
        uint id;
        string name;
        uint rollno ;
        string subject;
        uint marks;
    }
    
    Student[] student;
    function addStudent(uint id,string calldata name, uint rollno, string calldata subject , uint marks) external{
        Student memory newStudent = Student(id,name,rollno,subject,marks);
        student.push(newStudent);
       
    }
    
   function getStudent(uint id) public view returns (uint,string memory,uint,string memory,uint) {
      return (student[id].id,student[id].name, student[id].rollno,student[id].subject,student[id].marks);
   }
}
    
