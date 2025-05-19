const express = require("express");
const dotenv = require("dotenv");
const cors = require("cors");

dotenv.config();

const app = express();

app.use(express.json());
app.use(cors());

console.log("Hello Ankit");
const API_KEY = process.env.OPEN_AI_API_KEY;
console.log("API_KEY", API_KEY);
