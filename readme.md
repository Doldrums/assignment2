### Task 1
````
+--------------------------------------------------------------------------------------------------------------------------------+
|QUERY PLAN                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------+
|Sort  (cost=8.45..8.46 rows=1 width=35) (actual time=0.026..0.026 rows=1 loops=1)                                               |
|  Sort Key: customer_name                                                                                                       |
|  Sort Method: quicksort  Memory: 25kB                                                                                          |
|  ->  Index Scan using customer_id_idx on customers  (cost=0.42..8.44 rows=1 width=35) (actual time=0.021..0.021 rows=1 loops=1)|
|        Index Cond: (customer_id = 1000)                                                                                        |
|Planning Time: 0.069 ms                                                                                                         |
|Execution Time: 0.039 ms                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------+

+--------------------------------------------------------------------------------------------------------------------------------+
|QUERY PLAN                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------+
|Sort  (cost=8.45..8.46 rows=1 width=35) (actual time=0.692..0.692 rows=1 loops=1)                                               |
|  Sort Key: customer_name                                                                                                       |
|  Sort Method: quicksort  Memory: 25kB                                                                                          |
|  ->  Index Scan using customer_id_idx on customers  (cost=0.42..8.44 rows=1 width=35) (actual time=0.671..0.672 rows=1 loops=1)|
|        Index Cond: (customer_id = 2000)                                                                                        |
|Planning Time: 0.093 ms                                                                                                         |
|Execution Time: 0.708 ms                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------+

+--------------------------------------------------------------------------------------------------------------------------------+
|QUERY PLAN                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------+
|Sort  (cost=8.45..8.46 rows=1 width=35) (actual time=0.803..0.804 rows=1 loops=1)                                               |
|  Sort Key: customer_name                                                                                                       |
|  Sort Method: quicksort  Memory: 25kB                                                                                          |
|  ->  Index Scan using customer_id_idx on customers  (cost=0.42..8.44 rows=1 width=35) (actual time=0.796..0.798 rows=1 loops=1)|
|        Index Cond: (customer_id = 3000)                                                                                        |
|Planning Time: 0.069 ms                                                                                                         |
|Execution Time: 0.817 ms                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------+

+--------------------------------------------------------------------------------------------------------------------------------+
|QUERY PLAN                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------+
|Sort  (cost=8.45..8.46 rows=1 width=35) (actual time=0.020..0.021 rows=1 loops=1)                                               |
|  Sort Key: customer_name                                                                                                       |
|  Sort Method: quicksort  Memory: 25kB                                                                                          |
|  ->  Index Scan using customer_id_idx on customers  (cost=0.42..8.44 rows=1 width=35) (actual time=0.013..0.013 rows=1 loops=1)|
|        Index Cond: (customer_id = 4000)                                                                                        |
|Planning Time: 0.070 ms                                                                                                         |
|Execution Time: 0.049 ms                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------+


EXPLAIN ANALYZE
SELECT * FROM customers WHERE customer_id = 1000 ORDER BY customer_name;
SELECT * FROM customers WHERE customer_id = 2000 ORDER BY customer_name;
SELECT * FROM customers WHERE customer_id = 3000 ORDER BY customer_name;
SELECT * FROM customers WHERE customer_id = 4000 ORDER BY customer_name;


CREATE INDEX customer_id_idx ON customers USING btree (customer_id);
CREATE INDEX customer_name_idx ON customers USING hash (customer_name);
CREATE INDEX customer_address_idx ON customers USING brin (customer_address);
CREATE INDEX customer_review_idx ON customers USING GIN (customer_review);




+--------------------------------------------------------------------------------------------------------------------------------+
|QUERY PLAN                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------+
|Sort  (cost=8.45..8.46 rows=1 width=35) (actual time=0.026..0.026 rows=1 loops=1)                                               |
|  Sort Key: customer_name                                                                                                       |
|  Sort Method: quicksort  Memory: 25kB                                                                                          |
|  ->  Index Scan using customer_id_idx on customers  (cost=0.42..8.44 rows=1 width=35) (actual time=0.021..0.021 rows=1 loops=1)|
|        Index Cond: (customer_id = 1000)                                                                                        |
|Planning Time: 0.069 ms                                                                                                         |
|Execution Time: 0.039 ms                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------+

+--------------------------------------------------------------------------------------------------------------------------------+
|QUERY PLAN                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------+
|Sort  (cost=8.45..8.46 rows=1 width=35) (actual time=0.692..0.692 rows=1 loops=1)                                               |
|  Sort Key: customer_name                                                                                                       |
|  Sort Method: quicksort  Memory: 25kB                                                                                          |
|  ->  Index Scan using customer_id_idx on customers  (cost=0.42..8.44 rows=1 width=35) (actual time=0.671..0.672 rows=1 loops=1)|
|        Index Cond: (customer_id = 2000)                                                                                        |
|Planning Time: 0.093 ms                                                                                                         |
|Execution Time: 0.708 ms                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------+

+--------------------------------------------------------------------------------------------------------------------------------+
|QUERY PLAN                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------+
|Sort  (cost=8.45..8.46 rows=1 width=35) (actual time=0.803..0.804 rows=1 loops=1)                                               |
|  Sort Key: customer_name                                                                                                       |
|  Sort Method: quicksort  Memory: 25kB                                                                                          |
|  ->  Index Scan using customer_id_idx on customers  (cost=0.42..8.44 rows=1 width=35) (actual time=0.796..0.798 rows=1 loops=1)|
|        Index Cond: (customer_id = 3000)                                                                                        |
|Planning Time: 0.069 ms                                                                                                         |
|Execution Time: 0.817 ms                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------+

+--------------------------------------------------------------------------------------------------------------------------------+
|QUERY PLAN                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------+
|Sort  (cost=8.45..8.46 rows=1 width=35) (actual time=0.020..0.021 rows=1 loops=1)                                               |
|  Sort Key: customer_name                                                                                                       |
|  Sort Method: quicksort  Memory: 25kB                                                                                          |
|  ->  Index Scan using customer_id_idx on customers  (cost=0.42..8.44 rows=1 width=35) (actual time=0.013..0.013 rows=1 loops=1)|
|        Index Cond: (customer_id = 4000)                                                                                        |
|Planning Time: 0.070 ms                                                                                                         |
|Execution Time: 0.049 ms                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------+
````