#!/usr/bin/node

const arg = process.argv.slice(2);

function factorial(n) {
    
    if (!n)
        return 1;
    let result = n * factorial(n - 1);
    return result;
}

console.log(factorial(Number(arg[0])));
