from FinInfoSpider.items import FininfospiderItem
from .sql import SQL_OP
import sys

class jqkPipline(object):

    def process_item(self, item, spider):
        if isinstance(item, FininfospiderItem):
            name = item['name']
            titles = item['titles']
            SQL_OP.makeTable(name, titles)
            data_set = item['data_set']
            for datas in data_set:
                date = datas[0]
                ret = SQL_OP.select_name(name, date)
                if ret[0] == 1:
                    pass
                else:
                    SQL_OP.insert(name, datas)


        # if isinstance(item, FininfospiderItem):
        #     pos_id = item['pos_id']
        #     ret = sql.select_name(pos_id)
        #     if ret[0] == 1:
        #         print('已经存在了')
        #         pass
        #     else:
        #         postname = item['Postname']
        #         salary = item['Salary']
        #         location = item['Location']
        #         company = item['Company']
        #         companytype = item['Company_type']
        #         welfare = item['welfare']
        #         experience = item['Experience']
        #         education = item['Education']
        #         pos_id = item['pos_id']
        #         sql.insert(postname, salary, location, company, companytype, welfare, experience, education, pos_id)
        #         print('开始存储')
