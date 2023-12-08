import parsing
import pandas as pd
from datetime import datetime
import load

if __name__ == "__main__":

    current_date_str = datetime.now().strftime('%Y-%m-%d')
    df_parmeters = pd.read_excel("parameter_values.xlsx")

    choice = int(input("데이터 수집 종류 입력(1: 과거부터 금일까지, 2: 금일만)>> "))
    if choice == 1:
        csv_file_path = "dataset.csv"
        parser = parsing.Parser(csv_filename=csv_file_path)
        for i in range(len(df_parmeters)):
            itemcategorycode = df_parmeters.iloc[i]['itemcategorycode']
            itemcode = df_parmeters.iloc[i]['itemcode']
            kindcode = df_parmeters.iloc[i]['kindcode']
            params = {
                'action': 'periodProductList',
                'p_productclscode': '02',
                'p_startday': '2023-01-01',
                'p_endday': current_date_str,
                'p_itemcategorycode': f'{itemcategorycode}',
                'p_itemcode': f'{itemcode}',
                'p_kindcode': f'{kindcode:02d}',
                'p_productrankcode': '',
                'p_convert_kg_yn': 'N',
                'p_cert_key': 'd09ee58b-a48f-4eda-b5db-4a6d6a8ac25a',
                'p_cert_id': 'lb948',
                'p_returntype': 'xml'
            }
            parser.convert_xml_to_csv(params)
        load.upload_to_s3(file_path = csv_file_path)

    elif choice == 2:
        csv_file_path = f"dataset({current_date_str}).csv"
        parser = parsing.Parser(csv_filename = csv_file_path)
        for i in range(len(df_parmeters)):
            itemcategorycode = df_parmeters.iloc[i]['itemcategorycode']
            itemcode = df_parmeters.iloc[i]['itemcode']
            kindcode = df_parmeters.iloc[i]['kindcode']
            params = {
                'action': 'periodProductList',
                'p_productclscode': '02',
                'p_startday': current_date_str,
                'p_endday': current_date_str,
                'p_itemcategorycode': f'{itemcategorycode}',
                'p_itemcode': f'{itemcode}',
                'p_kindcode': f'{kindcode:02d}',
                'p_productrankcode': '',
                'p_convert_kg_yn': 'N',
                'p_cert_key': 'd09ee58b-a48f-4eda-b5db-4a6d6a8ac25a',
                'p_cert_id': 'lb948',
                'p_returntype': 'xml'
            }
            parser.convert_xml_to_csv(params)
        load.upload_to_s3(file_path = csv_file_path)
    
    else:
        print("입력값 오류")
        exit()