const data = require("./data");
class Controller {
  async getAllUsers() {
    return new Promise((resolve, _) => resolve(data));
  }
  async getUser(id) {
    return new Promise((resolve, reject) => {
      let user = data.find((user) => user.id === parseInt(id));
      if (user) {
        resolve(user);
      } else {
        reject(`User with id ${id} not found`);
      }
    });
  }

  async createUser(user) {
    return new Promise((resolve, _) => {
      let newUser = {
        id: Math.floor(4 + Math.random) * 10,
        ...user,
      };
      resolve(newUser);
    });
  }

  async deleteUser(id) {
    return new Promise((resolve, reject) => {
      let user = data.find((user) => user.id === parseInt(id));
      if (!user) {
        reject(`No user with id ${id} found`);
      }
      resolve("User deleted successfully")``;
    });
  }
}

module.exports = Controller;
