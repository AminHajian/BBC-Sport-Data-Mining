-- CREATE DATABASE BBC;
USE BBC;

CREATE TABLE news(
Title TEXT,
url TEXT,
publish_date DATETIME,
image BLOB

);

SELECT *
FROM bbc.news
ORDER by publish_date DESC;


