// backend/server.js
import express from 'express';
import cors from 'cors';
import bodyParser from 'body-parser';

const app = express();
const PORT = 5000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Test route for root
app.get('/', (req, res) => {
  res.send('Backend is running ✅');
});

// Example messages API
app.get('/api/messages', (req, res) => {
  res.json([
    { id: 1, text: 'Hello from server!' },
    { id: 2, text: 'Welcome to your chat app!' },
  ]);
});

// Optional: prevent favicon 404 errors
app.get('/favicon.ico', (req, res) => res.status(204));

// Start server
app.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`);
});
