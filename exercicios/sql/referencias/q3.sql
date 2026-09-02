-- Q3: LEFT JOIN ... IS NULL (anti-join)
SELECT
    p.id AS policy_id,
    c.name AS client,
    p.premium_usd
FROM policies p
JOIN submissions s ON s.id = p.submission_id
JOIN clients c ON c.id = s.client_id
LEFT JOIN claims cl ON cl.policy_id = p.id
WHERE cl.id IS NULL
ORDER BY p.id;
