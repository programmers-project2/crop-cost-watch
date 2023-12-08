CREATE or replace TABLE dev.analytics.month_ago_summary AS
SELECT
    TD.REGION,
    TD.ITEM,
    TD.VARIETY,
    TD.PRICE TODAY_PRICE,
    MD.PRICE MONTH_AGO_PRICE,
    MD.PRICE-TD.PRICE PRICE_FLUCTUATION,
    ROUND((MD.PRICE-TD.PRICE)/MD.PRICE*100, 2) PRICE_FLUCTUATION_RATE
FROM dev.raw_data.today_data TD
LEFT JOIN raw_data.month_ago_data MD
    ON TD.ITEM = MD.ITEM and TD.REGION = MD.REGION and TD.VARIETY = MD.VARIETY
;

SELECT *
FROM dev.analytics.month_ago_summary
;
