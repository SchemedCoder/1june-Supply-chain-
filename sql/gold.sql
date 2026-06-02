-- ==========================================
-- INVENTORY SNAPSHOT
-- ==========================================

SELECT *
FROM gold_inventory_snapshot
LIMIT 20;

-- ==========================================
-- VENDOR PERFORMANCE
-- ==========================================

SELECT *
FROM gold_vendor_performance
ORDER BY avg_delay DESC
LIMIT 20;

-- ==========================================
-- TOP SHIPPING VENDORS
-- ==========================================

SELECT
vendor_id,
shipment_count
FROM gold_vendor_performance
ORDER BY shipment_count DESC
LIMIT 10;

-- ==========================================
-- INVENTORY BY WAREHOUSE
-- ==========================================

SELECT
warehouse_id,
SUM(current_stock) total_stock
FROM gold_inventory_snapshot
GROUP BY warehouse_id
ORDER BY total_stock DESC;

-- ==========================================
-- PRODUCT AVAILABILITY
-- ==========================================

SELECT
product_id,
SUM(current_stock) available_stock
FROM gold_inventory_snapshot
GROUP BY product_id
ORDER BY available_stock DESC;
