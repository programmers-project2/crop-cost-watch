--S3 버킷에서 데이터 가져오기

COPY INTO dev.raw_data.test_data
from 's3://버킷주소/파일이름'
credentials=(AWS_KEY_ID='ABC...HIJ' AWS_SECRET_KEY='123ABC...789XYZ')
FILE_FORMAT = (type = 'CSV' skip_header=1)