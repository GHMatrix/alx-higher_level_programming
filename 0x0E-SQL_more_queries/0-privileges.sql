-- Listing all previleges of MySQL users, user_0d_1 and user_0d_2 on server
SELECT * FROM mysql.user WHERE User IN ('user_0d_1', 'user_0d_2') AND Host = 'localhost';
