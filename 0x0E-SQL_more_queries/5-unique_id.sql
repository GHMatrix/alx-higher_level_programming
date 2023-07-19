-- Creating a table named unique_id on MySQL server
-- with id INT with the default value 1 and must be unique
CREATE TABLE IF NOT EXISTS `unique_id` (`id` INT	DEFAULT 1 UNIQUE, `name` VARCHAR(256));
