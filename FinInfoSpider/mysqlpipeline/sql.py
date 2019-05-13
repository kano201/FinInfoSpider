import pymysql.connections


MYSQL_HOSTS = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '********'
MYSQL_PORT = '3306'
MYSQL_DB = 'finance_information'

cnx = pymysql.connect(user=MYSQL_USER, password=MYSQL_PASSWORD,host=MYSQL_HOSTS, database=MYSQL_DB, charset='utf8mb4')
cur = cnx.cursor()


class SQL_OP:
    @classmethod
    def select_name(cls, tablename, date):
        sql = "SELECT EXISTS(SELECT 1 FROM "
        sql += tablename
        sql += " WHERE 日期=%(date)s)"
        value = {
            'date': date
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]

    @classmethod
    def select_table(cls):
        sql = 'SELECT table_name FROM information_schema.TABLES WHERE table_schema=\'finance_information\''
        cur.execute(sql)
        return cur.fetchall()

    # 以每一个上市公司的名称作为表名进行数据存储
    @classmethod
    def makeTable(cls, tableName, titles):
        sql = "CREATE TABLE IF NOT EXISTS %s (日期 date"
        for title in titles:
            if title == '净资产收益率-摊薄':
                title = '净资产收益率——摊薄'
            sql += "," + title + " varchar(50)"
        sql += ")"

        sql = sql % (tableName)
        # print(sql)
        cur.execute(sql)

    # 对数据集中的数据进行插入，插入操作在执行后一定要进行commit操作才会保存
    @classmethod
    def insert(cls, tablename, datas):
        sql = "INSERT INTO "
        sql += tablename
        sql += " VALUES ("
        first_flag = True
        for data in datas:
            if first_flag:
                sql += "\'" + data + "\'"
                first_flag = False
            else:
                sql += ',' + "\'" + data + "\'"
        sql += ')'
        # sql = sql % (tablename)

        cur.execute(sql)
        cnx.commit()



    # def __init__(self, **kwargs):
    #     MYSQL_HOSTS = kwargs.get('MYSQL_HOSTS', '127.0.0.1')
    #     MYSQL_USER = kwargs.get('MYSQL_USER', 'root')
    #     MYSQL_PASSWORD = kwargs.get('MYSQL_PASSWORD', 'yili_19960824@')
    #     MYSQL_PORT = kwargs.get('MYSQL_PORT', '3306')
    #     MYSQL_DB = kwargs.get('MYSQL_DB', 'finance_information')
    #
    #     self.cnx = pymysql.connect(user=MYSQL_USER, password=MYSQL_PASSWORD,
    #                                host=MYSQL_HOSTS, database=MYSQL_DB, charset='utf8mb4')
    #     self.cur = self.cnx.cursor()





