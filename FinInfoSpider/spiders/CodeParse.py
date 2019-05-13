from bs4 import BeautifulSoup
import requests
import re

class getStockCode:
    def get(self):
        url = 'http://www.cgedt.com/stockcode/hushi.asp'

        response = requests.get(url)

        BS = BeautifulSoup(response.content, 'lxml')
        Parse_List = BS.find('div', id='stockcodelist').find('ul').find_all('li')
        ID_List = {}
        for content in Parse_List:
            Name = re.findall(r'(.+?)\(', content.text)
            Code = re.findall(r'\((.+?)\)', content.text)
            ID = {Code[0]: Name[0]}
            ID_List.update(ID)
        return ID_List


