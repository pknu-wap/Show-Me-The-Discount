import pymysql

db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='wap', charset='utf8')

try:
    with db.cursor() as cursor:
        sql = '''
                   CREATE TABLE post(
                        PRIMARY KEY(Data_Id) NOT NULL,
                        Store VARCHAR(10) NOT NULL,
                        Product VARCHAR(10) NOT NULL,
                        Content VARCHAR(20) NOT NULL,
                        Price INT NOT NULL,
                        Start_Date NULL,
                        End_Date VARCHAR(10) NOT NULL,
                        Password INT NOT NULL
                        
                );

                    CREATE TABLE replies(
                        PRIMARY KEY(Reply_Id) NOT NULL,
                        Reply VARCHAR(20) NOT NULL.
                        Num INT NOT NULL
                );
              '''


        cursor.execute(sql)  # 실행하기
    db.commit()  # DB에 Complete
finally:
    db.close()  # DB 연결 닫기