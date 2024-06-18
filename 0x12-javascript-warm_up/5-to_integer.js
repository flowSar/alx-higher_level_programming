#!/usr/bin/node

const arg = process.argv.slice(2);

if (!Number(arg[0]))
    console.log('Not a number');
else
    console.log(`My number: ${parseInt((arg[0]), 10)}`);
