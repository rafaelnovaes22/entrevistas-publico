-- Q2: ROW_NUMBER to pick the most recent record per client
WITH ranked AS (
    SELECT
        c.name AS client,
        q.premium_usd,
        q.quoted_at,
        ROW_NUMBER() OVER (PARTITION BY c.id ORDER BY q.quoted_at DESC, q.id DESC) AS rn
    FROM quotes q
    JOIN submissions s ON s.id = q.submission_id
    JOIN clients c ON c.id = s.client_id
)
SELECT client, premium_usd, quoted_at
FROM ranked
WHERE rn = 1
ORDER BY client;
