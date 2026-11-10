USE sakila;
-- aggregate function returning one average value for the whole film table
SELECT AVG(rental_rate) FROM film;

-- scalar function returning a rounded rate value for every individual row
SELECT title, rental_rate, ROUND(rental_rate) AS rounded_rate
FROM film;

-- cast rental datetime into separate date and time components
SELECT rental_id,
       rental_date,
       CAST(rental_date AS DATE) AS rental_day,
       CAST(rental_date AS TIME) AS rental_time
FROM rental
LIMIT 10;

-- convert rental rate to text and cast duration and rate to decimal and integer formats
SELECT title,
       CONVERT(rental_rate, CHAR) AS rate_as_text,
       CAST(rental_duration AS DECIMAL(5,2)) AS duration_decimal,
       CAST(rental_rate AS SIGNED) AS rate_as_integer
FROM film
LIMIT 10;

-- convert film id numbers from base 10 to binary and hexadecimal bases
SELECT film_id,
       CONV(film_id, 10, 2)AS binary_id,
       CONV(film_id, 10, 16) AS hex_id
FROM film
WHERE film_id IN (10, 255);

-- combine names into formatted full and directory strings and lowercase email addresses
SELECT customer_id,
       CONCAT_WS(' ', first_name, last_name)  AS full_name,
       CONCAT_WS(', ', last_name, first_name) AS directory_name,
       LOWER(email) AS clean_email
FROM customer
LIMIT 10;

-- extract substrings, lowercase titles, replace spaces with underscores, and reverse film titles
SELECT title,
       SUBSTRING(title, 1, 3)AS first_three,
       LOWER(title) AS lower_title,
       REPLACE(title, ' ', '_') AS file_name,
       REVERSE(title) AS backwards
FROM film
LIMIT 10;

-- test string trimming, string insertion, string comparison, and number formatting on literals
SELECT TRIM('   Sakila   ') AS trimmed,
       INSERT('ACADEMY DINOSAUR', 1, 7, 'MUSEUM') AS inserted,
       STRCMP('ALIEN', 'ZORRO')AS compare_1,
       STRCMP('ACE', 'ACE') AS compare_2,
       FORMAT(1234567.891, 2) AS formatted;

-- nest string functions to format customer first names into proper case
SELECT first_name,
       CONCAT(UPPER(SUBSTRING(first_name, 1, 1)), LOWER(SUBSTRING(first_name, 2))) AS proper_first
FROM customer
LIMIT 10;

-- extract date parts, weekdays, day numbers, and quarters from rental dates
SELECT rental_id,
       rental_date,
       DATE(rental_date) AS rental_day,
       DAYNAME(rental_date) AS weekday,
       DAYOFWEEK(rental_date) AS weekday_number,
       DAYOFYEAR(rental_date) AS day_of_year,
       QUARTER(rental_date) AS quarter
FROM rental
LIMIT 10;

-- calculate days kept and due dates by joining rental, inventory, and film tables
SELECT r.rental_id, r.rental_date, r.return_date,
       DATEDIFF(r.return_date, r.rental_date) AS days_kept,
       f.rental_duration,
       DATE_ADD(r.rental_date, INTERVAL f.rental_duration DAY) AS due_date
FROM rental r
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f ON f.film_id = i.film_id
LIMIT 10;

-- format payment dates and calculate dates one month earlier
SELECT payment_id,
       payment_date,
       DATE_FORMAT(payment_date, '%M %d, %Y') AS report_date,
       DATE_FORMAT(payment_date, '%m/%d/%Y %h:%i %p') AS us_format,
       DATE_SUB(payment_date, INTERVAL 1 MONTH) AS one_month_earlier
FROM payment
LIMIT 10;

-- display current date, current time, and current timestamp
SELECT CURDATE(), CURTIME(), CURRENT_TIMESTAMP;
-- replace null return dates with a descriptive not returned label
SELECT rental_id,
       rental_date,
       IFNULL(return_date, 'Not returned') AS return_status
FROM rental
WHERE return_date IS NULL;

-- count total rentals and use isnull with sum to count unreturned items
SELECT COUNT(*) AS total_rentals, SUM(ISNULL(return_date)) AS not_returned
FROM rental;

-- use coalesce to fall back to language id when original language id is null
SELECT title,
       original_language_id, language_id,
       COALESCE(original_language_id, language_id) AS display_language
FROM film
LIMIT 10;

-- use nullif to turn specific standard rates into nulls for counting non standard films
SELECT COUNT(*) AS all_films,
       COUNT(NULLIF(rental_rate, 0.99)) AS films_not_099
FROM film;

-- compare various rounding, ceiling, floor, and truncation functions on break-even ratios
SELECT title,
       replacement_cost,
       rental_rate,
       replacement_cost / rental_rate AS raw_ratio,
       ROUND(replacement_cost / rental_rate, 2) AS rounded,
       CEILING(replacement_cost / rental_rate) AS rentals_to_break_even,
       FLOOR(replacement_cost / rental_rate) AS floored,
       TRUNCATE(replacement_cost / rental_rate, 1) AS truncated
FROM film
LIMIT 10;

-- calculate difference and absolute distance from average rental rate using subqueries
SELECT title,
       rental_rate,
       ROUND(rental_rate - (SELECT AVG(rental_rate) FROM film), 2)
           AS diff_from_avg,
       ABS(ROUND(rental_rate - (SELECT AVG(rental_rate) FROM film), 2))
           AS distance_from_avg
FROM film
LIMIT 10;

-- group films by even or odd film IDs using mod
SELECT MOD(film_id, 2) AS even_or_odd, COUNT(*) AS films
FROM film
GROUP BY MOD(film_id, 2);

--  enforce a price minimum using greatest
SELECT title, rental_rate,
       GREATEST(rental_rate, 2.99) AS price_with_2_99_minimum
FROM film
LIMIT 10;

-- evaluate least, power, square root, and pi functions
SELECT LEAST(4.99, 2.99, 0.99), POW(2, 10), SQRT(144), ROUND(PI(), 4);

-- retrieve five random film titles
SELECT title FROM film ORDER BY RAND() LIMIT 5;

-- format customer names as last name comma first name and lowercase emails sorted by last name
SELECT customer_id, CONCAT_WS(', ', last_name, first_name) AS directory_name, LOWER(email) AS clean_email
FROM customer
ORDER BY last_name;

-- count rentals grouped by month name to find the busiest month
SELECT DATE_FORMAT(rental_date, '%M') AS rental_month, COUNT(*) AS rental_count
FROM rental
GROUP BY rental_month
ORDER BY rental_count DESC;

-- check due date against return date for rental id 1 to see if it was on time
SELECT r.rental_id, r.rental_date, r.return_date, DATE_ADD(r.rental_date, INTERVAL f.rental_duration DAY) AS due_date
FROM rental r
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f ON f.film_id = i.film_id
WHERE r.rental_id = 1;

-- list return status for every rental using ifnull and count how many are unreturned
SELECT IFNULL(return_date, 'Not returned') AS return_status, COUNT(*) AS count
FROM rental
GROUP BY return_status;

-- calculate required rentals to break even using ceiling for each film title
SELECT f.title, CEILING(f.replacement_cost / f.rental_rate) AS rentals_needed
FROM film f
WHERE f.title = 'ACADEMY DINOSAUR';

-- list every customer name in proper case and lower case email sorted by last name
SELECT CONCAT(UPPER(SUBSTRING(first_name, 1, 1)), LOWER(SUBSTRING(first_name, 2)), ' ', 
              UPPER(SUBSTRING(last_name, 1, 1)), LOWER(SUBSTRING(last_name, 2))) AS proper_name,
       LOWER(email) AS clean_email
FROM customer
ORDER BY last_name
LIMIT 10;

-- count how many rentals were kept longer than the film rental duration
SELECT COUNT(*) AS late_rentals
FROM rental r
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f ON f.film_id = i.film_id
WHERE DATEDIFF(r.return_date, r.rental_date) > f.rental_duration;

-- count rentals by weekday name to find the busiest weekday
SELECT DAYNAME(rental_date) AS weekday, COUNT(*) AS rental_count
FROM rental
GROUP BY weekday
ORDER BY rental_count DESC;

-- show total payments grouped by year and quarter formatted with two decimal places
SELECT YEAR(payment_date) AS payment_year, QUARTER(payment_date) AS payment_quarter, FORMAT(SUM(amount), 2) AS total_revenue
FROM payment
GROUP BY payment_year, payment_quarter
ORDER BY SUM(amount) DESC;

-- independent practice p5: count films needing more than the average break-even rental count using a subquery
SELECT COUNT(*) AS films_above_avg
FROM (SELECT replacement_cost / rental_rate AS ratio FROM film ) sub
WHERE ratio > (SELECT AVG(replacement_cost / rental_rate) FROM film);

-- calculate days outstanding as of 2006-02-14 for unreturned rentals and find the maximum
SELECT COUNT(*) AS unreturned_count, MAX(DATEDIFF('2006-02-14', rental_date)) AS max_days_out
FROM rental
WHERE return_date IS NULL;

-- independent practice p7: create a custom product code for film id 2 using upper case title prefix rate and id joined by dashes
SELECT CONCAT_WS('-', UPPER(SUBSTRING(title, 1, 3)), rental_rate, film_id) AS product_code
FROM film
WHERE film_id = 2;

-- count distinct customers who made a payment over 10 dollars in q3 of 2005 using a subquery
SELECT COUNT(DISTINCT customer_id) AS customer_count
FROM payment
WHERE amount > 10 
  AND QUARTER(payment_date) = 3 
  AND YEAR(payment_date) = 2005;

-- count how many rentals were kept longer than the overall average keep duration using a subquery
SELECT COUNT(*) AS kept_longer_than_avg
FROM rental
WHERE DATEDIFF(return_date, rental_date) > (
    SELECT AVG(DATEDIFF(return_date, rental_date)) 
    FROM rental 
    WHERE return_date IS NOT NULL
);