-- create user and assign privileges
IF NOT EXISTS CREATE USER 'user_0d_1'@'localhost' IDENTIFIED WITH IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
