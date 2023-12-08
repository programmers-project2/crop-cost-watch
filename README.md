# crop-cost-watch (농산물 가격 데이터를 이용한 물가 변동 조회)

<br>

## 소개
농산물 유통 가격 데이터를 시각화하여 물가 변동을 조회하는 서비스입니다. <br>
품목별 지난 달/일 기준으로 가격 등락률을 조회할 수 있으며, 월/일 별 총 농산물 평균 가격 등락률을 조회할 수 있습니다.

<br>

## 활용 기술 및 언어
<img src="https://github.com/programmers-project2/crop-cost-watch/assets/100893674/1acba839-50ed-4d26-95ca-317b3c65dcda" width=70%>

<br>

## 프로젝트 구조
![image](https://github.com/programmers-project2/crop-cost-watch/assets/100893674/27d19257-e4c9-4d18-bd37-e3a60929800a)

1. API(https://www.kamis.or.kr/customer/reference/openapi_list.do?action=detail&boardno=2)를 이용하여 (일별 품목별 도·소매 가격 정보) 데이터를 수집 및 정제한 후 이를 S3 버킷에 저장합니다.
2. Snowflake에서 Database, Schema, Table을 생성한 후, S3로부터 데이터를 적재(bulk update)합니다.
3. Snowflake에서 데이터를 전처리한 후 분석용 테이블(summary 테이블)을 생성합니다.
4. Superset 오픈 소스를 docker에서 실행하여 Snowflake와 연동한 후, 기존의 summary 테이블을 통해 차트 및 대시 보드를 생성합니다.

<br>

## 결과
![image](https://github.com/programmers-project2/crop-cost-watch/assets/100893674/37323855-2b51-4e3f-8802-797ed90ab000)
