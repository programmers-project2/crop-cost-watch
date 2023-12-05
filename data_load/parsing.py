import requests
import csv
import xml.etree.ElementTree as ET

class Parser:
    '''
    XML 데이터를 API로 받아와서 CSV 파일로 저장하는 클래스.
    '''

    def __init__(self, base_api_url="http://www.kamis.or.kr/service/price/xml.do", csv_filename="dataset.csv"):
        '''
        Parameters:
        - base_api_url: 기본 API URL
        - csv_filename: 저장할 CSV 파일의 이름
        '''
        self.base_api_url = base_api_url
        self.csv_filename = csv_filename
        with open(self.csv_filename, 'w', newline='', encoding='utf-16') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["품목", "품종", "지역", "날짜", "가격", "상호명"])

    def fetch_xml_data(self, params):
        '''
        API로부터 동적으로 매개변수를 설정하여 XML 데이터를 받아오는 메서드.
        Parameters:
        - params: API 호출에 사용할 매개변수 딕셔너리
        '''
        try:
            response = requests.get(self.base_api_url, params=params)
            response.raise_for_status()  # HTTP 오류 발생 시 예외 발생
            return response.text
            
        except requests.RequestException as e:
            print(f"API 호출 중 에러 발생: {e}")
            return None

    def parse_xml_to_csv(self, xml_data):
        '''
        XML 데이터를 파싱하고 CSV 파일로 저장하는 메서드.
        Parameters:
        - xml_data: XML 형식의 데이터
        추출할 내용:
        - "품목", "품종", "지역", "날짜", "가격", "상호명"
        '''
        try:
            root = ET.fromstring(xml_data)
            data = []
            for item_element in root.findall('.//data/item'):
                itemname = item_element.find('itemname').text
                kindname = item_element.find('kindname').text
                countyname = item_element.find('countyname').text
                yyyy = item_element.find('yyyy').text
                regday = item_element.find('regday').text
                price = item_element.find('price').text
                marketname = item_element.find('marketname').text
                if itemname and price != '-':
                    itemname = itemname.strip()
                    kindname = kindname.strip()
                    countyname = countyname.strip()
                    yyyy = yyyy.strip()
                    regday = regday.strip()
                    price = int(price.strip().replace(',', ''))
                    marketname = marketname.strip()
                else:
                    continue
                data.append([itemname, kindname, countyname, yyyy+"/"+regday, price, marketname])
            
            with open(self.csv_filename, 'a', newline='', encoding='utf-16') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerows(data)
                
            print(f"Data successfully saved to {self.csv_filename}")

        except ET.ParseError as e:
            print(f"XML 파싱 중 에러 발생: {e}")

    def convert_xml_to_csv(self, params):
        '''
        동적으로 매개변수를 설정하여 XML 데이터를 받아와서 CSV 파일로 변환하는 메서드.
        Parameters:
        - params: API 호출에 사용할 매개변수 딕셔너리
        '''
        xml_data = self.fetch_xml_data(params)
        if xml_data:
            self.parse_xml_to_csv(xml_data)
