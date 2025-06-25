-- Creation de table id_not_null avec comme valeur par défaut 1
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);