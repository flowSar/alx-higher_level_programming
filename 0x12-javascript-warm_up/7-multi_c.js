#!/usr/bin/node

const arg = process.argv.slice(2);
const x = parseInt(arg[0], 10);
if (!x)
    console.log('Missing number of occurrences');
else {
    for (let i = 0; i < x; i++)
        console.log('C is fun');
}
