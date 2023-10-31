# database_hw7_2019038011_윤석현

import pymysql

# conn = pymysql.connect(host='192.168.34.132', port=4567, user='shyun', password='1234', db='madang', charset='utf8')

db = pymysql.connect(host='192.168.34.132', port=4567, user='shyun', password='1234', db='madang', charset='utf8')


# 데이터 삽입
def insert_data(cursor):
    bookid = int(input("삽입할 책의 ID를 입력하세요: "))
    bookname = input("삽입할 책의 이름을 입력하세요: ")
    publisher = input("삽입할 책의 출판사를 입력하세요: ")
    price = int(input("삽입할 책의 가격을 입력하세요: "))

    query = "INSERT INTO Book (bookid, bookname, publisher, price) VALUES (%s, %s, %s, %s)"
    values = (bookid, bookname, publisher, price)
    cursor.execute(query, values)
    db.commit()
    print("데이터가 성공적으로 삽입되었습니다.")


# 데이터 삭제
def delete_data(cursor):
    bookid = int(input("삭제할 책의 ID를 입력하세요: "))

    query = "DELETE FROM Book WHERE bookid = %s"
    values = (bookid,)
    cursor.execute(query, values)
    db.commit()
    print("데이터가 성공적으로 삭제되었습니다.")


# 데이터 검색
def search_data(cursor):
    bookname = input("검색할 책의 이름을 입력하세요: ")

    query = "SELECT * FROM Book WHERE bookname = %s"
    values = (bookname,)
    cursor.execute(query, values)
    results = cursor.fetchall()
    for row in results:
        print(row)

actions = ('삽입', '삭제', '검색', '종료')



try:
    with db.cursor() as cursor:
        while True:
            action = input("1. 데이터 삽입, 2. 데이터 삭제, 3. 데이터 검색 4. 종료 중 원하는 작업을 입력해주세요(ex: 삽입)\n")
            print(action + " 입력하셨습니다.")
            if action == '삽입':
                insert_data(cursor)

            elif action == '삭제':
                delete_data(cursor)

            elif action == '검색':
                search_data(cursor)

            elif action == '종료':
                print('정상적으로 종료되었습니다.')
                break

            else:
                print('잘못 입력하셨습니다.'+ str(actions) + '중에 입력해주세요')

finally:
    db.close()
