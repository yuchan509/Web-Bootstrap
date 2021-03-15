from Database import Connector

# 게시판 정보 저장.
def insertUserData(board_name) :
    # 쿼리문 작성.
    sql = '''
            insert into board_table
            (board_name)
            values (%s)
          '''
    # 데이터 베이스 접속.
    conn = Connector.get_connection()
    cursor = conn.cursor()

    # %s에 대입할 값을 지정.
    data = (board_name)

    # 쿼리문 실행.
    cursor.execute(sql, data)
    conn.commit()

    # 데이터 베이스 접속 해제.
    conn.close()


# 게시판 데이터 전체를 가져오는 함수.
def selectBoardDataAll() :
    # 쿼리문 작성.
    sql = '''
            select * from board_table
            order by board_idx
          '''
    # 데이터 베이스 접속.
    conn = Connector.get_connection()
    cursor = conn.cursor()

    # %s에 대입할 값을 지정.
    # 쿼리문 실행.
    cursor.execute(sql)
    result = cursor.fetchall()

    # 데이터 베이스 접속 해제.
    conn.close()
    return result


# 게시판 데이터 하나를 가져오는 함수.
def selectBoardDatOne(board_idx) :
    # 쿼리문.
    sql = '''
            select * from board_table
            where board_idx = %s
           '''
    # 데이터 베이스 접속.
    conn = Connector.get_connection()
    cursor = conn.cursor()

    # %s에 대입할 값을 지정.(없음)
    data = (board_idx)

    # 쿼리문 실행.
    cursor.execute(sql, data)
    result = cursor.fetchone()

    # 데이터 베이스 접속 해제.
    conn.close()

    return result

# 게시판 정보를 수정하는 함수.
def updateBoardData(board_name, board_idx) :
    # 쿼리문 작성.
    sql = '''
            update board_table
            set board_name = %s
            where board_idx = %s
          '''

    # 데이터 베이스 접속.
    conn = Connector.get_connection()
    cursor = conn.cursor()

    # %s에 대입할 값을 지정.
    data = (board_name, board_idx)

    # 쿼리문 실행.
    cursor.execute(sql, data)
    conn.commit()

    # 데이터 베이스 접속 해제.
    conn.close()


# 회원 정보 삭제 함수.
def deleteUserData(board_idx) :
    # 쿼리문 작성.
    sql = '''
            delete from board_table
            where board_idx = %s
          '''
    # 데이터 베이스 접속.
    conn = Connector.get_connection()
    cursor = conn.cursor()

    # %s에 대입할 값을 지정.
    data = (board_idx)

    # 쿼리문 실행.
    cursor.execute(sql, data)
    conn.commit()

    # 데이터 베이스 접속 해제.
    conn.close()

