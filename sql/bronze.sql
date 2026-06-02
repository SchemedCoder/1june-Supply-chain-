-- ==========================================
-- BRONZE LAYER VALIDATION
-- ==========================================

SELECT COUNT(*) AS total_orders
FROM bronze_orders;

SELECT COUNT(*) AS total_shipments
FROM bronze_shipments;

SELECT COUNT(*) AS total_inventory
FROM bronze_inventory;

SELECT COUNT(*) AS total_vendors
FROM bronze_vendors;

-- Duplicate Orders

SELECT
order_id,
COUNT(*) cnt
FROM bronze_orders
GROUP BY order_id
HAVING COUNT(*) > 1;

-- Invalid Inventory

SELECT *
FROM bronze_inventory
WHERE stock_quantity < 0;

-- Missing Vendor IDs

SELECT *
FROM bronze_shipments
WHERE vendor_id IS NULL;

-- Shipment Status Distribution

SELECT
status,
COUNT(*) total
FROM bronze_shipments
GROUP BY status
ORDER BY total DESC;
