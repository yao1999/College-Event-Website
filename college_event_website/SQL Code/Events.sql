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
);