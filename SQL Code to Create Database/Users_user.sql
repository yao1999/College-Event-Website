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
    university_id INT
);
