// Print all numbers from 1 to the given limit

function printNumbers(limit) {
    let numbers = [];

    for (let i = 1; i < limit; i++) {
        numbers.push(i);
    }

    return numbers;
}

const result = printNumbers(10);

console.log("Numbers:", result);
console.log("Count:", result.length);