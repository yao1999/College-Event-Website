CREATE TABLE university(
    id INT PRIMARY KEY NOTNULL,
    name VARCHAR(100) NOTNULL,
    description TEXT NOTNULL,
    number_of_students INT NOT NULL,
    location_id INT NOTNULL
);