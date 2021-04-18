SELECT DISTINCT*FROM 'Event_event' e 
    WHERE e.is_public = 1


SELECT DISTINCT*FROM 'Event_event' e, 'user' m
    WHERE e.is_private = 1 And m.university_id = e.university_id


SELECT DISTINCT*FROM 'Event_event' e, 'Users_rsonumber' u 'user' m
    WHERE e.is_RSO = 1 And u.rso_id = e.rso_id AND m.username = u.username

