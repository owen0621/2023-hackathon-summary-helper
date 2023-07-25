DROP DATABASE IF EXISTS `HACKATHON`;
CREATE SCHEMA `HACKATHON`;
USE `HACKATHON`;
CREATE TABLE `court_cases` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `court` VARCHAR(50),
    `date` DATETIME,
    `no` VARCHAR(50),
    `sys` VARCHAR(50),
    `reason` VARCHAR(255),
    `type` VARCHAR(50),
    `historyHash` VARCHAR(100),
    `mainText` TEXT,
    `opinion` TEXT,
    `judgement` TEXT NOT NULL,
    `summary` TEXT
);