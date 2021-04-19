CREATE TABLE university_pictures(
    id INT PRIMARY KEY NOTNULL,
    university_id INT NOTNULL,
    photo_id INT NOTNULL
);


INSERT INTO university_pictures(
    id, 
    university_id,
    photo_id
)

VALUES(
    1,	
    1,	
    1
) 