-- creates the database hbtn_0d_2 and the user user_0d_2.
CREATE DATABASE IF NOT EXIST hbtn_0d_2;
ALTER USER `user_0d_2`@`localhost`
IDENTIFIED BY The `user_0d_2`@`localhost` 'user_0d_2_pwd';
GRANT ALL PRIVILEGES ON hbtn_0d_2.* TO `user_0d_2`@`localhost`;
FLUSH PRIVILEGES;
