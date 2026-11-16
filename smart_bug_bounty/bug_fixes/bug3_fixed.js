
function registerUser(username, age) {
    if (typeof username !== "string" || username.trim() === "") {
        return "Username is required";
    }

    if (!Number.isInteger(age) || age < 18) {
        return "User must be at least 18";
    }

    return "Registration successful";
}

console.log(registerUser("", 25));
console.log(registerUser("Alex", 15));
console.log(registerUser("Sarah", 25));

module.exports = registerUser;