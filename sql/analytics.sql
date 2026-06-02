-- ==========================================
-- INVENTORY RISK REPORT
-- ==========================================

SELECT *
FROM analytics_inventory_risk
ORDER BY current_stock;

-- ==========================================
-- TOP DELAYED VENDORS
-- ==========================================

SELECT *
FROM analytics_vendor_scorecard
LIMIT 20;

-- ==========================================
-- DELAYED SHIPMENTS
-- ==========================================

SELECT *
FROM analytics_delivery_delays
ORDER BY delivery_delay_days DESC;

-- ==========================================
-- LATE ARRIVING DATA AUDIT
-- ==========================================

SELECT *
FROM analytics_late_arrivals;

-- ==========================================
-- HIGH RISK WAREHOUSES
-- ==========================================

SELECT
warehouse_id,
COUNT(*) risky_products
FROM analytics_inventory_risk
GROUP BY warehouse_id
ORDER BY risky_products DESC;

-- ==========================================
-- DELIVERY PERFORMANCE KPI
-- ==========================================

SELECT
COUNT(*) total_shipments,
AVG(delivery_delay_days) avg_delay,
MAX(delivery_delay_days) worst_delay
FROM analytics_delivery_delays;

-- ==========================================
-- STOCKOUT CANDIDATES
-- ==========================================

SELECT
warehouse_id,
product_id,
current_stock
FROM analytics_inventory_risk
WHERE current_stock < 25
ORDER BY current_stock;
