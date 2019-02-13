import pymysql

db = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = '123', db = 'wap', charset = 'utf8')
with db.cursor() as cursor:

    sql = '''
                CREATE TABLE writing(
                        PRIMARY KEY(id) NOT NULL,
                        brand VARCHAR(10) NOT NULL,
                        brand key INT NOT NULL,
                        pruduct name VARCHAR(10) NOT NULL,
                        price INT NOT NULL,
                        deadline INT NOT NULL,
                        password INT NOT NULL,
                        type INT NOT NULL,
                        start period NULL,
                        contents VARCHAR(20) NULL
                                            
                );
                
                
            '''

    cursor.execute(sql) # 실행하기
    db.commit()         # DB에 Complete
    db.close()          # DB 연결 닫기