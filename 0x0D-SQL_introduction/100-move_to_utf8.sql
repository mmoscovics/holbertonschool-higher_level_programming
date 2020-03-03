-- converts a database to UTF8
-- select database
USE hbtn_0c_0;
-- change database defaults
ALTER DATABASE CHARACTER SET utf8mb4;
ALTER DATABASE COLLATE utf8mb4_unicode_ci;
-- change table defautls
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;