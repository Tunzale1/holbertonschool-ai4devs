function registerUser(username, age) {
    if (username = "") {
        return "Username is required";
    }

    if (age < 18) {
        return "User must be at least 18";
    }

    return "Registration successful";
}

console.log(registerUser("", 25));
console.log(registerUser("Alex", 15));
console.log(registerUser("Sarah", 25));