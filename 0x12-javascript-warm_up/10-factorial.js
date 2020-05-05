#!/usr/bin/node
function factorial (number) {
  let value = 1;
  if (isNaN(number)) {
    return value;
  } else {
    while (number > 1) {
      value *= number;
      number -= 1;
    }
  }
  return value;
}
console.log(factorial(parseInt(process.argv[2])));
