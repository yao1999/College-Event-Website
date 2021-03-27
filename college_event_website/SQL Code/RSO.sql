CREATE TABLE RSO_rso(
    id INT PRIMARY KEY NOTNULL,
    name VARCHAR(255) NOTNULL,
    description TEXT,
    total_students INT NOTNULL,
    admin_id INT NOTNULL,
    university_id INT NOTNULL,
);
