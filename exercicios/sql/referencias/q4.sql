-- Q4: top-N per group with a window function
WITH ranked AS (
    SELECT
        policy_id,
        id AS claim_id,
        amount_usd,
        ROW_NUMBER() OVER (PARTITION BY policy_id ORDER BY amount_usd DESC, id DESC) AS rn
    FROM claims
)
SELECT policy_id, claim_id, amount_usd
FROM ranked
WHERE rn <= 2
ORDER BY policy_id, amount_usd DESC, claim_id DESC;
