USE sakila;
 -- We want to find how many film belongs to a specific catgory in this case Action.
SELECT COUNT(*)
FROM film f
JOIN film_category fc on f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name ='Action';

 -- count number of unique categoris in a c table.
 SELECT COUNT(DISTINCT category_id)
 FROM film_category;
 
 -- total sum of rentasl from rental table.alter
SELECT SUM(inventory_id) AS 'Sum of Rentals'
FROM rental;

-- total amount paid per customer
SELECT customer_id, SUM(amount)
FROM payment
GROUP BY customer_id
LIMIT  5;

-- otal amount paid per customer and also the avergae
SELECT AVG(amount) AS 'Average ', SUM(amount) 'Total'
FROM payment;

-- avg film lenght
SELECT AVG(lengtH)
FROM film
LIMIT 10;

-- ROUND the avg film lenght
SELECT ROUND(AVG(lengtH), 2)
FROM film;

-- average amount paid per customer
SELECT customer_id, AVG(amount)
FROM payment
GROUP BY customer_id
LIMIT  5;

-- find the earlist relaste date.
SELECT MIN(release_year)
FROM film;

-- finding the minimum rental rate fro each fc
SELECT fc.category_id , MIN(f.rental_rate) AS 'Min Rental Rate'
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
GROUP BY fc.category_id
LIMIT 10;

-- average result was a bit strange to me so needed to see it.
SELECT  rental_rate
FROM film;

-- find the hight payment amount in payments table
SELECT MAX(amount) AS 'Highest Payment'
FROM payment;

-- find the 10 hight payment amount per customer in customer order.
SELECT customer_id, MAX(amount) AS 'Highest Payment Per Customer'
FROM payment
GROUP BY customer_id
LIMIT 10;

-- find how many rental each customer has made
SELECT customer_id, COUNT(*) AS rental_count
FROM rental
GROUP BY customer_id
LIMIT 10;

-- order of operations with group by and order by
select customer_id, count(*) as rental_count
from rental
group by customer_id
order by rental_count desc;                              

-- using multiple columns in group by for subgroups
select r.customer_id, i.film_id, count(*) as rental_count
from rental r
join inventory i on r.inventory_id = i.inventory_id
group by r.customer_id, i.film_id;

-- filtering grouped data with having example 1 total spent over 100
select customer_id, sum(amount) as total_spent
from payment
group by customer_id
having total_spent > 100;                             

-- filtering grouped data with having example 2 rental count over 5
select customer_id, count(*) as rental_count
from rental
group by customer_id
having rental_count > 5;

-- multiple conditions in the having clause
select r.customer_id, count(*) as rental_count, sum(p.amount) as total_spent
from rental r
join payment p on r.rental_id = p.rental_id
group by r.customer_id
having rental_count > 5 and total_spent > 100;

-- still need to undestand the filtering concpect more in depth but the aggregate functions make alot ore sense when using it like this.