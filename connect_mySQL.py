import pymysql
import random

def select_conn_answerDB(line: str):
    conn = pymysql.connect(host='127.0.0.1:3306', unix_socket='/var/run/mysqld/mysqld.sock', user='admin', passwd='password', db='answerDB')
    cur = conn.cursor()
    cur.execute(f"select * from answer where question = '{line}'")
    # for r in cur:
    #     print(r)
    cur.close()
    conn.close()
    answer = [i[2] for i in cur]
    if len(answer) > 0:
        return random.choice(answer)
    else:
        conn = pymysql.connect(host='127.0.0.1:3306', unix_socket='/var/run/mysqld/mysqld.sock', user='admin', passwd='password', db='answerDB')
        cur = conn.cursor()
        cur.execute(f"insert into unknowquestion(question) value ('{line}')")
        conn.commit()
        cur.close()
        conn.close()

        return "Я не знаю что ответить, но я записал эту фразу для разбора на будущее"


# def insert_conn_answerDB(line: str):
#     conn = pymysql.connect(host='127.0.0.1:3306', unix_socket='/var/run/mysqld/mysqld.sock', user='admin', passwd='password', db='answerDB')
#     cur = conn.cursor()
#     cur.execute()
#     conn.commit()
#     cur.close()
#     conn.close()
#
