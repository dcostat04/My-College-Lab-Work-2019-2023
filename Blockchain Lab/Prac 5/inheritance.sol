//SPDX-License-Identifier: MIT
pragma solidity ^0.5.0;
contract quadrilateral{
int public sides = 4;
int public sumAngles = 360;
}
contract rombus is quadrilateral{
bool public sidesConcurent = true;
}
contract parallelogram is quadrilateral{
bool public angleConcurent = true;
}
contract rectangle is paralleogram{
bool public rightAngles = true;
}
contract square is rombus,reactangle{
}
