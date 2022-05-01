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



### Task 2

````

EXPLAIN ANALYZE
SELECT *
FROM purchases_products_list
         JOIN products ON products.product_id = purchases_products_list.product_id
         JOIN sales ON products.product_type = sales.sale_type;



EXPLAIN ANALYZE
SELECT *
FROM purchases_products_list
         JOIN products ON products.product_id = purchases_products_list.product_id
         JOIN sales ON products.product_type = sales.sale_type;

+-----------------------------------------------------------------------------------------------------------------------------+
|QUERY PLAN                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------+
|Hash Join  (cost=24.18..67.33 rows=2040 width=2092) (actual time=0.048..0.049 rows=0 loops=1)                                |
|  Hash Cond: (purchases_products_list.product_id = products.product_id)                                                      |
|  ->  Seq Scan on purchases_products_list  (cost=0.00..30.40 rows=2040 width=12) (actual time=0.005..0.005 rows=1 loops=1)   |
|  ->  Hash  (cost=23.55..23.55 rows=50 width=2080) (actual time=0.029..0.030 rows=0 loops=1)                                 |
|        Buckets: 1024  Batches: 1  Memory Usage: 8kB                                                                         |
|        ->  Hash Join  (cost=11.12..23.55 rows=50 width=2080) (actual time=0.028..0.029 rows=0 loops=1)                      |
|              Hash Cond: ((sales.sale_type)::text = (products.product_type)::text)                                           |
|              ->  Seq Scan on sales  (cost=0.00..11.40 rows=140 width=524) (actual time=0.003..0.004 rows=9 loops=1)         |
|              ->  Hash  (cost=10.50..10.50 rows=50 width=1556) (actual time=0.011..0.011 rows=9 loops=1)                     |
|                    Buckets: 1024  Batches: 1  Memory Usage: 9kB                                                             |
|                    ->  Seq Scan on products  (cost=0.00..10.50 rows=50 width=1556) (actual time=0.002..0.004 rows=9 loops=1)|
|Planning Time: 0.696 ms                                                                                                      |
|Execution Time: 0.234 ms                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------------------------------------------------------------+
|QUERY PLAN                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------+
|Hash Join  (cost=24.18..67.33 rows=2040 width=2092) (actual time=0.038..0.040 rows=0 loops=1)                                |
|  Hash Cond: (purchases_products_list.product_id = products.product_id)                                                      |
|  ->  Seq Scan on purchases_products_list  (cost=0.00..30.40 rows=2040 width=12) (actual time=0.007..0.007 rows=1 loops=1)   |
|  ->  Hash  (cost=23.55..23.55 rows=50 width=2080) (actual time=0.020..0.021 rows=0 loops=1)                                 |
|        Buckets: 1024  Batches: 1  Memory Usage: 8kB                                                                         |
|        ->  Hash Join  (cost=11.12..23.55 rows=50 width=2080) (actual time=0.020..0.021 rows=0 loops=1)                      |
|              Hash Cond: ((sales.sale_type)::text = (products.product_type)::text)                                           |
|              ->  Seq Scan on sales  (cost=0.00..11.40 rows=140 width=524) (actual time=0.003..0.003 rows=9 loops=1)         |
|              ->  Hash  (cost=10.50..10.50 rows=50 width=1556) (actual time=0.008..0.008 rows=9 loops=1)                     |
|                    Buckets: 1024  Batches: 1  Memory Usage: 9kB                                                             |
|                    ->  Seq Scan on products  (cost=0.00..10.50 rows=50 width=1556) (actual time=0.003..0.004 rows=9 loops=1)|
|Planning Time: 0.136 ms                                                                                                      |
|Execution Time: 0.077 ms                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------+


CREATE INDEX product_type_idx ON products USING hash (product_type);
CREATE INDEX sale_type_idx ON sales USING hash (sale_type);

+--------------------------------------------------------------------------------------------------------------------------+
|QUERY PLAN                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------+
|Hash Join  (cost=2.53..41.50 rows=2040 width=2092) (actual time=0.037..0.038 rows=0 loops=1)                              |
|  Hash Cond: (purchases_products_list.product_id = products.product_id)                                                   |
|  ->  Seq Scan on purchases_products_list  (cost=0.00..30.40 rows=2040 width=12) (actual time=0.005..0.005 rows=1 loops=1)|
|  ->  Hash  (cost=2.42..2.42 rows=9 width=2080) (actual time=0.023..0.024 rows=0 loops=1)                                 |
|        Buckets: 1024  Batches: 1  Memory Usage: 8kB                                                                      |
|        ->  Hash Join  (cost=1.20..2.42 rows=9 width=2080) (actual time=0.023..0.024 rows=0 loops=1)                      |
|              Hash Cond: ((products.product_type)::text = (sales.sale_type)::text)                                        |
|              ->  Seq Scan on products  (cost=0.00..1.09 rows=9 width=1556) (actual time=0.003..0.004 rows=9 loops=1)     |
|              ->  Hash  (cost=1.09..1.09 rows=9 width=524) (actual time=0.010..0.010 rows=9 loops=1)                      |
|                    Buckets: 1024  Batches: 1  Memory Usage: 9kB                                                          |
|                    ->  Seq Scan on sales  (cost=0.00..1.09 rows=9 width=524) (actual time=0.002..0.004 rows=9 loops=1)   |
|Planning Time: 0.367 ms                                                                                                   |
|Execution Time: 0.589 ms                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------+

+--------------------------------------------------------------------------------------------------------------------------+
|QUERY PLAN                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------+
|Hash Join  (cost=2.53..41.50 rows=2040 width=2092) (actual time=0.042..0.043 rows=0 loops=1)                              |
|  Hash Cond: (purchases_products_list.product_id = products.product_id)                                                   |
|  ->  Seq Scan on purchases_products_list  (cost=0.00..30.40 rows=2040 width=12) (actual time=0.007..0.007 rows=1 loops=1)|
|  ->  Hash  (cost=2.42..2.42 rows=9 width=2080) (actual time=0.026..0.027 rows=0 loops=1)                                 |
|        Buckets: 1024  Batches: 1  Memory Usage: 8kB                                                                      |
|        ->  Hash Join  (cost=1.20..2.42 rows=9 width=2080) (actual time=0.026..0.027 rows=0 loops=1)                      |
|              Hash Cond: ((products.product_type)::text = (sales.sale_type)::text)                                        |
|              ->  Seq Scan on products  (cost=0.00..1.09 rows=9 width=1556) (actual time=0.004..0.005 rows=9 loops=1)     |
|              ->  Hash  (cost=1.09..1.09 rows=9 width=524) (actual time=0.012..0.012 rows=9 loops=1)                      |
|                    Buckets: 1024  Batches: 1  Memory Usage: 9kB                                                          |
|                    ->  Seq Scan on sales  (cost=0.00..1.09 rows=9 width=524) (actual time=0.002..0.003 rows=9 loops=1)   |
|Planning Time: 0.170 ms                                                                                                   |
|Execution Time: 0.336 ms                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------+
```

### Task 3
