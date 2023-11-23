const http = require("http");
const User = require("./controller");
const { getReqData } = require("./utils");

const PORT = process.env.PORT || 5000;

const server = http.createServer(async (req, res) => {
  if (req.url === "/api/users" && req.method === "GET") {
    const users = await new User().getAllUsers();
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(users));
  } else if (req.url.match(/\/api\/user\/([0-9]+)/) && req.method === "POST") {
    const id = req.url.split("/")[3];
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ message: `Post user ${id} successfully` }));
  } else if (
    req.url.match(/\/api\/user\/([0-9]+)/) &&
    req.method === "DELETE"
  ) {
    const id = req.url.split("/")[3];
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ message: `Delete user ${id} successfully` }));
  } else if (req.url.match(/\/api\/user\/([0-9]+)/) && req.method === "PATCH") {
    const id = req.url.split("/")[3];
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ message: `Patch user ${id} successfully` }));
  } else {
    res.writeHead(404, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ message: "Root not found" }));
  }
});
server.listen(PORT, () => {
  console.log(`Server started on port: ${PORT}`);
});
