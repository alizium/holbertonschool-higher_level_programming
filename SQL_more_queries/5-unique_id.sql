-- Creation table unique_id
-- avec 1 comme valeur par défaut

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);