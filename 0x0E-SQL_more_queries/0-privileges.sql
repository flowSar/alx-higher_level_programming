-- listing granted permession for users 

SELECT * 
FROM mysql.user 
WHERE user IN ('user_0d_1', 'user_0d_2');
