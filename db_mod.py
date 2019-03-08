import pymysql

db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='wap', charset='utf8')

try:
    with db.cursor() as cursor:
        sql = '''
                   CREATE TABLE post(
                        PRIMARY KEY(data_id) NOT NULL,
                        store VARCHAR(10) NOT NULL,
                        product VARCHAR(10) NOT NULL,
                        content VARCHAR(20) NOT NULL,
                        price INT NOT NULL,
                        startdate NULL,
                        enddate INT NOT NULL,
                        password INT NOT NULL
                        
                );

                    CREATE TABLE replies(
                        PRIMARY KEY(reply_id) NOT NULL, #댓글 키값
                        content VARCHAR(20) NOT NULL.
                        num INT NOT NULL
                );
              '''


        cursor.execute(sql)  # 실행하기
    db.commit()  # DB에 Complete
finally:
    db.close()  # DB 연결 닫기