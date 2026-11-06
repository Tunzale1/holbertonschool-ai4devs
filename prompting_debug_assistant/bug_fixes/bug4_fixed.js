// Print all numbers from 1 to the given limit

function printNumbers(limit) {
    let numbers = [];

    for (let i = 1; i <= limit; i++) {
        numbers.push(i);
    }

    return numbers;
}

const result = printNumbers(10);

console.assert(result.length === 10);
console.assert(result[0] === 1);
console.assert(result[9] === 10);

console.log("Bug 4 fixed successfully!");
console.log("Numbers:", result);
console.log("Count:", result.length);