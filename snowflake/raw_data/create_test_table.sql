CREATE or replace TABLE dev.raw_data.today_data AS
SELECT *
FROM raw_data.test_data TD
WHERE TS = (SELECT MAX(TS) FROM raw_data.test_data)
;

CREATE or replace TABLE dev.raw_data.yesterday_data AS
SELECT *
FROM raw_data.test_data TD
WHERE TS = DATEADD(DAY, -1, (SELECT MAX(TS) FROM raw_data.test_data))
;

-- 한달전이 휴일인 경우 마지막 평일 기준으로 금액 책정
CREATE or replace TABLE dev.raw_data.month_ago_data AS
SELECT *
FROM raw_data.test_data
WHERE 
    TS = DATEADD(MONTH, -1, (SELECT MAX(TS) FROM raw_data.test_data))
    OR ( 
        NOT EXISTS (
            SELECT 1
            FROM raw_data.test_data
            WHERE TS = DATEADD(MONTH, -1, (SELECT MAX(TS) FROM raw_data.test_data))
        )
        AND TS = DATEADD(DAY, -1, DATEADD(MONTH, -1, (SELECT MAX(TS) FROM raw_data.test_data)))
    )
    OR (
        NOT EXISTS (
            SELECT 1
            FROM raw_data.test_data
            WHERE TS IN (DATEADD(MONTH, -1, (SELECT MAX(TS) FROM raw_data.test_data)), DATEADD(DAY, -1, DATEADD(MONTH, -1, (SELECT MAX(TS) FROM raw_data.test_data))))
        )
        AND TS = DATEADD(DAY, -2, DATEADD(MONTH, -1, (SELECT MAX(TS) FROM raw_data.test_data)))
    );

SELECT * FROM raw_data.month_ago_data;
