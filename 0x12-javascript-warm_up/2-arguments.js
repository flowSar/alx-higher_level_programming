#!/usr/bin/node

const arg = process.argv.slice(2);

if (arg.length === 1) {
  console.log('Argument found');
} else if (arg.length > 1) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
