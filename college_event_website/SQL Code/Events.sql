CREATE TABLE Event_event(
    id INT PRIMARY KEY NOTNULL,
    name VARCHAR(150) NOTNULL,
    description TEXT NOTNULL,
    date DATE NOTNULL,
    start_time TIME NOTNULL,
    end_time TIME NOTNULL,
    phone VARCHAR(31) NOTNULL,
    email VARCHAR(254) NOTNULL,
    is_public BOOL NOTNULL,
    is_private BOOL NOTNULL,
    is_RSO BOOL NOTNULL,
    user_id INT,
    is_approved BOOL NOTNULL,
    location_id INT,
    university_id INT,
    category VARCHAR(150)
    rso_id
);

CREATE TRIGGER Event_check
    AFTER INNER ON  Event_event
REFERENCING NEW AS NEW Event
WHEN ((SELECT COUNT(*)  
    FROM Event M
    WHERE M.start_time = NewEvent.start_time
    WHERE M.endt_time = NewEvent.end_time
    WHERE M.location_id = NewEvent.location_id
    ))


CREATE TRIGGER Event_admin_checker
    AFTER INNER ON Event
REFERENCING NEW AS NEW Event
WHEN ((SELECT COUNT(*)
    FROM Users M
    WHERE M.rso_id = NewEvent.admin_id.rso_id
    ))
FOR EACH ROW
UPDATE Event


INSERT INTO Event_event (
    id,
    name,
    description,
    date,
    start_time,
    end_time,
    phone,
    email,
    is_public,
    is_private,
    is_RSO,
    is_approved,
    location_iD,
    university_id,
    category
    admin_id,
    rso_id
    )

VALUES(
    24,
    "Star War 9",
    "talk about star wars",
    "2025-12-15",
    "10:20:00",
    "12:00:00",
    "1234567890",
    "starwar@gmail.com”,	
    1,	
    0,	
    0,
    1,	
    7,	
    NULL,	
    "movie,game",
    2,
    NULL
) 