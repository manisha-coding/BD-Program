const express = require("express");

const app = express();

app.use(express.json());

// Hardcoded username and password
const correctUsername = "admin";
const correctPassword = "admin@1234";

// Login API
app.post("/login", (req, res) => {
    const { username, password } = req.body;

    if (username === correctUsername && password === correctPassword) {
        res.status(200).json({
            message: "Login successful"
        });
    } else {
        res.status(401).json({
            message: "Invalid username or password"
        });
    }
});

app.listen(3000, () => {
    console.log("Server running on http://localhost:3000");
});