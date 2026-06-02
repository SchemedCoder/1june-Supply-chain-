-- ==========================================
-- SILVER LAYER DATA QUALITY
-- ==========================================

SELECT COUNT(*)
FROM silver_orders;

SELECT COUNT(*)
FROM silver_shipments;

SELECT COUNT(*)
FROM silver_inventory;

SELECT COUNT(*)
FROM silver_vendors;

-- Late Arriving Records

SELECT *
FROM silver_shipments
WHERE is_late_arrival = TRUE;

-- Inventory Quality

SELECT *
FROM silver_inventory
WHERE stock_quantity < 0;

-- Vendor Ratings

SELECT
vendor_id,
vendor_name,
vendor_rating
FROM silver_vendors
ORDER BY vendor_rating DESC;

-- Shipment Delay Summary

SELECT
AVG(delivery_delay_days) avg_delay,
MAX(delivery_delay_days) max_delay,
MIN(delivery_delay_days) min_delay
FROM silver_shipments;
