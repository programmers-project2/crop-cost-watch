import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_s3(file_path, object_name=None):
    """
    S3 버킷으로 파일 업로드
    - file_path: 업로드할 파일 경로
    - object_name: S3 버킷 내 파일 이름 (없을 경우 파일명 사용)
    - return: 성공 여부
    """
    # AWS 계정 정보 및 S3 버킷 정보 설정
    aws_access_key_id = 'AKIAY6I32O2YA2Q55VGU'
    aws_secret_access_key = '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'
    bucket_name = 'de-project2-bucket'

    # S3 클라이언트 생성
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    # S3에 업로드할 파일명 설정
    if object_name is None:
        object_name = file_path

    try:
        s3.upload_file(file_path, bucket_name, object_name)
        print(f"파일 {file_path}을(를) S3 버킷 {bucket_name}에 업로드했습니다.")
        return True
    except FileNotFoundError:
        print(f"파일 {file_path}을(를) 찾을 수 없습니다.")
        return False
    except NoCredentialsError:
        print("AWS 인증 정보가 잘못되었습니다.")
        return False
    except Exception as e:
        print(f"파일 업로드 중 오류 발생: {e}")
        return False