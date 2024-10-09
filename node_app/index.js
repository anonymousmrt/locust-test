const express = require('express');
const app = express();
const port = 3000;

const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get("/hello", (req, res) => {
  const data = { hello: "world" };
  res.json(data);
});
app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`);
});