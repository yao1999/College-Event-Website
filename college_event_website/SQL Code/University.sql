CREATE TABLE university(
    id INT PRIMARY KEY NOTNULL,
    name VARCHAR(100) NOTNULL,
    description TEXT NOTNULL,
    number_of_students INT NOT NULL,
    location_id INT NOTNULL,
    super_admin
);

CREATE TRIGGER UniversityChecker
    AFTER INNER ON university_locations
REFERENCING NEW AS NEW University
WHEN ((SELECT COUNT(*)  
    FROM RSO_students M
    WHERE M.rso_id = NewMember.rso_id) > 4) 
FOR EACH ROW   
UPDATE RSOs    
SET Status = ‘active’    
WHERE RSO_ID = NewMember.RSO_ID

INSERT INTO University_university(
    id，	
    name，	
    description，	
    number_of_students，	
    location_id,
    super_admin
)
VALUES (
    1,	
    "University of Central Florida",	
    "UCF is an academic, partnership and research leader in numerous 
    fields, such as optics and lasers, modeling and simulation, engineering 
    and computer science, business, public administration, education, 
    hospitality management, healthcare and video game design.",	
    66183,	
    1,	
    12
) 