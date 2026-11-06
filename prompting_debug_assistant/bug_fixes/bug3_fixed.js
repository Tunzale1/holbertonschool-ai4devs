// Calculate the total price of products in a shopping cart

function calculateTotal(cart) {
    let total = 0;

    for (let i = 0; i < cart.length; i++) {
        total += cart[i].price;
    }

    return total;
}

const shoppingCart = [
    { name: "Laptop", price: 900 },
    { name: "Mouse", price: 25 },
    { name: "Keyboard", price: 50 }
];

console.assert(calculateTotal(shoppingCart) === 975);
console.assert(calculateTotal([]) === 0);

console.log("Bug 3 fixed successfully!");
console.log("Total:", calculateTotal(shoppingCart));