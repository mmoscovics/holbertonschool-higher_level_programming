#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  args.sort().reverse();
}
console.log(args[1]);
