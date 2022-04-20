
DROP TABLE IF EXISTS books;

DROP TABLE IF EXISTS authors;


CREATE TABLE authors (
id SERIAL PRIMARY KEY,
name VARCHAR(255)
);
-- I can include NOT NULL in any element taht I don't want empty.
CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255) ,
  author_id INT REFERENCES authors(id)
);