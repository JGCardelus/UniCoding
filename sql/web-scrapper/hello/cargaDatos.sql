LOAD DATA LOCAL INFILE 'rolandGarros.csv' INTO TABLE ganadores
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n'
(year,champion,runner_up,final_score);

