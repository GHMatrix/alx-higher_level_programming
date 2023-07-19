-- Creating database named hbtn_0d_2 and user user_0d_2.
-- Giving only SELECT privelege to user user_0d_2.
-- Assigning password user_0d_2_pwd to user user_0d_2
CREATE DATABSE IF NOT EXISTS `hbtn_0d_2`;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
FLUSH PREVILEGES;