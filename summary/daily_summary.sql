CREATE or replace TABLE dev.analytics.daily_summary AS

WITH 
current_day_price AS (
    SELECT
        TS current_ts,
        ITEM,
        VARIETY,
        ROUND(AVG(PRICE)) current_price
    FROM dev.raw_data.test_data
    WHERE TS != (SELECT MIN(TS) FROM dev.raw_data.test_data)
    GROUP BY 1, 2, 3
    ORDER BY 1 DESC
),
previous_day_price AS (
    SELECT
        TS previous_ts,
        ITEM,
        VARIETY,
        ROUND(AVG(PRICE)) previous_price
    FROM dev.raw_data.test_data
    WHERE TS != (SELECT MAX(TS) FROM dev.raw_data.test_data)
    GROUP BY 1, 2, 3
    ORDER BY 1 DESC
)

SELECT
    COALESCE(P1.previous_ts, P2.previous_ts, P3.previous_ts) AS previous_ts,
    CP.current_ts,
    CP.ITEM,
    CP.VARIETY,
    CP.current_price,
    COALESCE(P1.previous_price, P2.previous_price, P3.previous_price) AS previous_price,
    ROUND(CP.current_price - COALESCE(P1.previous_price, P2.previous_price, P3.previous_price)) AS price_fluctuation,
    ROUND((CP.current_price - COALESCE(P1.previous_price, P2.previous_price, P3.previous_price))/CP.current_price*100, 2) AS price_fluctuation_rate
FROM
    current_day_price CP
LEFT JOIN previous_day_price P1 
    ON CP.ITEM = P1.ITEM 
        AND CP.VARIETY = P1.VARIETY 
        AND P1.previous_ts = DATEADD(DAY, -1, CP.current_ts)
LEFT JOIN previous_day_price P2 
    ON CP.ITEM = P2.ITEM 
        AND CP.VARIETY = P2.VARIETY 
        AND P2.previous_ts = DATEADD(DAY, -2, CP.current_ts)
LEFT JOIN previous_day_price P3 
    ON CP.ITEM = P3.ITEM 
        AND CP.VARIETY = P3.VARIETY 
        AND P3.previous_ts = DATEADD(DAY, -3, CP.current_ts)
ORDER BY CP.current_ts
;

DELETE FROM dev.analytics.daily_summary
WHERE
    previous_ts IS NULL
    OR current_ts IS NULL
;

SELECT *
FROM dev.analytics.daily_summary
;
