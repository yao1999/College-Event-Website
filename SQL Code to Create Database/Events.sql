CREATE TABLE Events_event(
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
    AFTER INNER ON  Events_event
REFERENCING NEW AS NEW Events_event
WHEN ((SELECT COUNT(*)  
    FROM Events_event M
    WHERE M.start_time = NewEvent.start_time
    WHERE M.endt_time = NewEvent.end_time
    WHERE M.location_id = NewEvent.location_id
    ))


CREATE TRIGGER Event_admin_checker
    AFTER INNER ON Events_event
REFERENCING NEW AS NEW Events_event
WHEN ((SELECT COUNT(*)
    FROM Users_user M
    WHERE M.rso_id = NewEvent.admin_id.rso_id
    ))
FOR EACH ROW
UPDATE Events_event