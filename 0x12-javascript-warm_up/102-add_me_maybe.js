#!/usr/bin/node
this.addMeMaybe = function (number, theFunction) {
  theFunction(number += 1);
};