const axios = require('axios');
const express = require('express');
const path = require('path'); // Add this line to include the 'path' module
const app = express();

app.use(express.json());

// Set view engine
app.set('view engine', 'ejs'); // Menggunakan EJS sebagai view engine

// Set folder views sebagai folder yang berisi file-file view Anda
app.set('views', path.join(__dirname, 'views')); // Use 'path' to join the directory

app.get('/', (req, res) => {
    res.render('index'); // Ini akan mencari file "index.ejs" di folder "views"
  });
app.post('/make-prediction', async (req, res) => {
    try {
        const data = req.body;

        // Kirim permintaan ke server Python
        const response = await axios.post('http://localhost:5000/predict', data);

        // Tanggapan dari server Python berisi hasil prediksi
        const prediction = response.data.prediction;

        res.json({ prediction });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Terjadi kesalahan dalam menghubungkan ke server Python.' });
    }
});

app.listen(3000, () => {
    console.log('http://localhost:3000');
});
