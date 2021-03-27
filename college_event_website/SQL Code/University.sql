

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
    location_id
)
VALUES (
    1，	
    "University of Central Florida",	
    "it is UCF", 	
    10000,	
    1
)