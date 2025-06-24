-- Liste tout les enregistrements de second_table sans nom vide par ordre croissant
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;