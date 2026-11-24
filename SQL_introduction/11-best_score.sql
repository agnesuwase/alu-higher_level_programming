-- Lists records of second_table with a score >= 10, top score first
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
