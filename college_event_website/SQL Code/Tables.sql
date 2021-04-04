CREATE TABLE Events_comment(
    id INT PRIMARY KEY NOTNULL,
    content TEXT NOTNULL,
    rating INT NOTNULL,
    event_id INT NOTNULL,
    user_id INT NOTNULL,
    timestamp TIME NOTNULL
);

CREATE TABLE Events_locations(
    id INT PRIMARY KEY NOTNULL,
    location_name VARCHAR(100) NOTNULL,
    latitude VARCHAR(100) NOTNULL,
    longitude VARCHAR(100) NOTNULL
);


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
    admin_id INT,
    is_approved BOOL NOTNULL,
    location_id INT,
    university_id INT,
    category VARCHAR(150)
);

CREATE TABLE RSO_students(
    id INTEGER PRIMARY KEY NOTNULL,
    rso_id INTEGER NOTNULL,
    user_id INTEGER NOTNULL
);

CREATE TABLE RSO_rso(
    id INT PRIMARY KEY NOTNULL,
    name VARCHAR(255) NOTNULL,
    description TEXT,
    total_students INT NOTNULL,
    admin_id INT NOTNULL,
    university_id INT NOTNULL,
);

CREATE TABLE Universities_locations(
    id INT PRIMARY KEY NOTNULL,
    location_name VARCHAR(100) NOTNULL,
    latitude VARCHAR(100) NOTNULL,
    longitude VARCHAR(100) NOTNULL
);

CREATE TABLE Universities_photos(
    id INT PRIMARY KEY NOTNULL,
    university_name VARCHAR(100) NOTNULL,
    photo_path VARCHAR(100) NOTNULL
);

CREATE TABLE Universities_pictures(
    id INT PRIMARY KEY NOTNULL,
    university_id INT NOTNULL,
    photo_id INT NOTNULL
);

CREATE TABLE Universities_university(
    id INT PRIMARY KEY NOTNULL,
    name VARCHAR(100) NOTNULL,
    description TEXT NOTNULL,
    number_of_students INT NOT NULL,
    location_id INT NOTNULL
);

CREATE TABLE Users_user (
    id INT PRIMARY KEY NOTNULL,
    password VARCHAR(128) NOTNULL,
    last_login DATATIME,
    is_superuser BOOL NOTNULL,
    username VARCHAR(150) NOTNULL,
    first_name VARCHar(150) NOTNULL,
    last_name VARCHAR(150) NOTNULL,
    email VARCHAR(254) NOTNULL,
    is_staff BOOL NOTNULL,
    is_active BOOL NOTNULL,
    data_joined DATETIME,
    is_admin BOOL NOTNULL,
    is_super_admin BOOL NOTNULL,
    university_id INT,
    rso_id INT Null
);