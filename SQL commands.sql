-- CREATE DATABASE BBC;
USE BBC;

CREATE TABLE news (
title TEXT,
url TEXT,
publish_date DATETIME
)

SELECT *
FROM bbc.news
ORDER by publish_date DESC;


