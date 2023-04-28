SELECT CAR_ID,
    (CASE WHEN CAR_ID IN (SELECT CAR_ID 
                          FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
                          WHERE STR_TO_DATE('20221016', '%Y%m%d') BETWEEN START_DATE and END_DATE)
    THEN '대여중'
    ELSE '대여 가능'
    END) AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC