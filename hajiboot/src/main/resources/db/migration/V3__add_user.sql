CREATE TABLE users (
  username         VARCHAR(100) NOT NULL PRIMARY KEY,
  encoded_password VARCHAR(255)
);

INSERT INTO users (username, encoded_password) VALUES ('user1', 'b9b1a1fb64960e03ebb6d66727cd635c23981ff7a65b1ace8fe393063888a76120977818290bb7bb');

INSERT INTO users (username, encoded_password) VALUES ('user2', 'b9b1a1fb64960e03ebb6d66727cd635c23981ff7a65b1ace8fe393063888a76120977818290bb7bb');

ALTER TABLE customers
  ADD username VARCHAR(100) NOT NULL DEFAULT 'user1';

ALTER TABLE customers
  ADD CONSTRAINT FK_CUSTOMERS_USERNAME FOREIGN KEY (username) REFERENCES users;
