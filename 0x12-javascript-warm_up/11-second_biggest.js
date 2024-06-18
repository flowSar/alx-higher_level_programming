#!/usr/bin/node

const arg = process.argv.slice(2);


if (!arg[0] || arg.length === 1)
    console.log(0);
else {
    let bigest = 0;
    let tmp;
    for (num of arg) {
        if (bigest < Number(num))
        {
            tmp = bigest;
            bigest = Number(num);
        }
    }
    console.log(tmp);
}
