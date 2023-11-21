const http = require("http");
const PORT = process.env.PORT || 5000;

const server = http.createServer(async (req, res) => {});
server.listen(PORT, () => {
  console.log(`Server started on port: ${PORT}`);
});
