// Find the total price of products in a shopping cart

function calculateTotal(cart) {
    let total = 0;

    for (let i = 0; i <= cart.length; i++) {
        total += cart[i].price;
    }

    return total;
}

const shoppingCart = [
    { name: "Laptop", price: 900 },
    { name: "Mouse", price: 25 },
    { name: "Keyboard", price: 50 }
];

console.log("Total:", calculateTotal(shoppingCart));