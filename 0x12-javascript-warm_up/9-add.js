#!/usr/bin/node

const arg = process.argv.slice(2);

add(arg[0], arg[1]);

function add(a, b) {
    const sum = Number(a) + Number(b);
    console.log(sum);
}
