# import pymysql.connections
#
#
# class SQL_OP:
#
#     def __init__(self, **kwargs):
#         MYSQL_HOSTS = kwargs.get('MYSQL_HOSTS', '127.0.0.1')
#         MYSQL_USER = kwargs.get('MYSQL_USER', 'root')
#         MYSQL_PASSWORD = kwargs.get('MYSQL_PASSWORD', 'yili_19960824@')
#         MYSQL_PORT = kwargs.get('MYSQL_PORT', '3306')
#         MYSQL_DB = kwargs.get('MYSQL_DB', 'finance_information')
#
#         self.cnx = pymysql.connect(user=MYSQL_USER, password=MYSQL_PASSWORD,
#                                    host=MYSQL_HOSTS, database=MYSQL_DB, charset='utf8mb4')
#         self.cur = self.cnx.cursor()
#
#     def makeTable(self, tableName, titles):
#         sql = "CREATE TABLE IF NOT EXISTS %s (日期 date"
#         for title in titles:
#             sql += "," + title + " varchar(50)"
#         sql += ")"
#
#         sql = sql % (tableName)
#         # print(sql.format(value))
#         self.cur.execute(sql)
#
#     def insert(self, data, name):
#         sql = "INSERT INTO test (日期, Name) VALUES (%(data)s, %(Name)s)"
#         value = {
#             'data': data,
#             'Name': name
#         }
#         self.cur.execute(sql, value)
#         self.cnx.commit()
#
#
# test = SQL_OP()
# titles = ['金钱', '涨幅']
# # test.makeTable('test1', titles)
# test.insert("2019-8-4", "nihao")
# test.cur.close()
# test.cnx.close()
