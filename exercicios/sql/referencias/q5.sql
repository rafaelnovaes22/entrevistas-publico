-- Q5: running total per client (windowed aggregate with an explicit frame)
SELECT
    c.name AS client,
    p.effective_date,
    p.premium_usd,
    SUM(p.premium_usd) OVER (
        PARTITION BY c.id
        ORDER BY p.effective_date, p.id
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_premium
FROM policies p
JOIN submissions s ON s.id = p.submission_id
JOIN clients c ON c.id = s.client_id
ORDER BY c.name, p.effective_date, p.id;
