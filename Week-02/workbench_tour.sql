/*
Ex1C - Workbench Readiness check
Name: Arash    Date: 10-20-2026
Q1: It shows localhost as host name, 3306 as port number, and it log in as user root.
Q2: On the home screen next to mySQL connection, ther is a plus sign (+), to setp up a new connetion you need to click that and follwo through.
Q3: We will not be using SQL Additions tab. 
Q4: Login User:root		Port:3306		MySQL Server Version:8.0.46
Q5:MANAGEMENT:Servers Status, Cline ConnectionsPRIMARYPRIMARY
Q6:actor_id is a smallint UN datatype, the letter Al stands for Auto Increment and PK stands fro Primary key
Q7:film_actor colums: actor_id, fild_id, last_updated, and it has 2 Foreign Key: fk_film_actor_actor points to actor table and fk_film_actor_film which points to film.
Q8:The program run which resulted in 3 fileds and 30 records.
Q9:1000 rows were returned, and we can see that in the Result Grid window
Q10:SELECT * FROM actr LIMIT 0, 1000 failed and other did not.
Q11:Instead of showing a normal gri,it lists each actor one by one, which details on eahc line. It's usefull it you wnat to copy and paste one single record into your work, without messin wiht the whole table.
Q12:GUINESS appears at top, 
Q13:2 actor matched with one coming twice with differne id.
Q14:Data Tyepe:varchar and can hold up to 45 chracters.
*/
USE sakila;
SELECT *FROM actor;
SELECT * FROM sakila.film;
SELECT * FROM actor;
