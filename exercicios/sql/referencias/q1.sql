-- Q1: JOIN + GROUP BY + HAVING + conditional aggregation
SELECT
    ca.name AS carrier,
    COUNT(*) AS total_submissions,
    SUM(CASE WHEN s.status = 'bound' THEN 1 ELSE 0 END) AS bound,
    ROUND(100.0 * SUM(CASE WHEN s.status = 'bound' THEN 1 ELSE 0 END) / COUNT(*), 1) AS conversion_pct
FROM submissions s
JOIN carriers ca ON ca.id = s.carrier_id
WHERE s.submitted_at >= '2026-01-01' AND s.submitted_at < '2027-01-01'
GROUP BY ca.id, ca.name
HAVING COUNT(*) >= 3
ORDER BY conversion_pct DESC, ca.name;
