-- create db and tables
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE,
	state_id INT NOT NULL FOREIGN KEY(id) REFERENCES hbtn_0d_usa.states(id))