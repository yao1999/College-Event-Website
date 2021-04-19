CREATE TABLE university_photos(
    id INT PRIMARY KEY NOTNULL,
    university_name VARCHAR(100) NOTNULL,
    photo_path VARCHAR(100) NOTNULL
);

INSERT INTO university_photos(
    id,	
    university_name,	
    photo_path
)
VALUES(
    1,	
    "University of Central Florida",	
    "University-Central-Florida-940x338.jpg"
) 