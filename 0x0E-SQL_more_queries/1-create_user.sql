-- Creating MySQL user user_0d_1
-- user_0d_1 should have all privileges on your MySQL server
-- Setting password for user_0d_1 to be set to user_0d_1_pwd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANTS ALL PRIVELEGES ON *.* TO 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd";
FLUSH PRIVILEGES;
