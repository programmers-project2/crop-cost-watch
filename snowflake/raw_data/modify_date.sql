UPDATE dev.raw_data.test_data
SET TS = TO_DATE(TS, 'YYYY/MM/DD')
WHERE TS LIKE '%/%'
;

SELECT * 
FROM dev.raw_data.test_data
ORDER BY TS DESC
;
