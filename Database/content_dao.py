from Database import Connector

# 게시글 정보를 추가하는 함수.
def insertContentData(content_subject, content_writer_idx, 
                        content_text, content_file, content_board_idx) :
    # 쿼리문 작성.
    sql = '''
            insert into content_table
            (content_subject, content_date, content_writer_idx, 
            content_text, content_file, content_board_idx)
            values (%s, sysdate(), %s, %s, %s, %s)
          '''
    # 데이터 베이스 접속.
    conn = Connector.get_connection()
    cursor = conn.cursor()

    # %s에 대입할 값을 지정.
    #for idx in range(756) : + str(idx)
    data = (content_subject , content_writer_idx, 
            content_text, content_file, content_board_idx)

    # 쿼리문 실행.
    cursor.execute(sql, data)
    conn.commit()

    # 데이터 베이스 접속 해제.
    conn.close()


# 모든 글 정보를 반환하는 함수.
def selectContentDataAll(content_board_idx, page) :
    # page 번호에 따른 시작 위치 계산.
    start = (page - 1) * 10

    # 쿼리문 작성.
    # limit 시작위치, 개수 : 시작 위치는 0부터 시작하며, 시작 위치에서 부터 개수만큼의 row만 가져오는 키워드.
    # 페이지 구분할 때 사용.
    sql = '''
            SELECT a1.content_idx, a1.content_subject, 
                   a2.user_name, a1.content_date
            FROM content_table a1, user_table a2
            WHERE a1.content_writer_idx = a2.user_idx
            AND a1.content_board_idx = %s
            ORDER BY a1.content_idx desc
            limit %s, 10
          '''
    # 데이터 베이스 접속.
    conn = Connector.get_connection()
    cursor = conn.cursor()

    # %s에 대입할 값을 지정.
    data = (content_board_idx, start)
    # 쿼리문 실행.
    cursor.execute(sql, data)
    result = cursor.fetchall()

    # 데이터 베이스 접속 해제.
    conn.close()

    return result


# 하나의 게시글만 가져오는 함수.
def selectContentDataOne(content_idx) :
    # 쿼리문 작성.
    sql = '''
            SELECT a2.user_name, a1.content_date, a1.content_subject,
                   a1.content_text, a1.content_file, a1.content_writer_idx
            FROM content_table a1, user_table a2
            WHERE a1.content_writer_idx = a2.user_idx
            AND a1.content_idx = %s;
          '''
    # 데이터 베이스 접속.
    conn = Connector.get_connection()
    cursor = conn.cursor()
    # %s에 지정될 값 설정.
    data = (content_idx)
    # 쿼리 실행.
    cursor.execute(sql, data)
    result = cursor.fetchone()
    # 데이터 베이스 접속 해제.
    conn.close()

    return result


# 게시글 정보를 수정하는 함수.
def updateContentData(content_subject, content_text,
                       content_file, content_idx) : 
    # 쿼리문 작성.
    # 첨부 이미지가 있을 경우와 없을 경우로 나눔.
    
    sql = '''
            update content_table
            set content_subject = %s, content_text = %s
            where content_idx = %s
          '''
    # 데이터베이스 접속.
    conn = Connector.get_connection()
    cursor = conn.cursor()
    # %s에 지정될 값 설정.
    data = (content_subject, content_text, content_idx)
    # 쿼리 실행.
    cursor.execute(sql, data)

    # 첨부파일이 있다면..
    if content_file != None :
          sql2 = '''
                  update content_table
                  set content_file = %s
                  where content_idx = %s
                  '''
          data2 = (content_file, content_idx)
          cursor.execute(sql2, data2)

    conn.commit()
    # 데이터 베이스 접속 종료.
    conn.close()


# 글 하나를 삭제하는 함수.
def deleteContentData(content_idx) :
    # 쿼리문 작성
    sql = '''
            delete from content_table
            where content_idx = %s
          '''
    # 데이터베이스 접속
    conn = Connector.get_connection()
    cursor = conn.cursor()
    # %s에 지정될 값 설정
    data = (content_idx)
    # 쿼리문 실행
    cursor.execute(sql, data)
    conn.commit()
    # 데이터 베이스 접속 종료
    conn.close()

# 방금 작성한 글의 번호(글 번호가 가장 큰 것)을 가져옴.
def getMaxConetentIdx(board_idx) :
    # 쿼리문
    sql = '''
            select max(content_idx)
            from content_table
            where content_board_idx = %s
          '''
    # 데이터베이스 접속
    conn = Connector.get_connection()
    cursor = conn.cursor()
    # %s에 지정될 값 설정
    data = (board_idx)
    # 쿼리문 실행
    cursor.execute(sql, data)
    result = cursor.fetchone()
    # 데이터 베이스 접속 종료
    conn.close()
    return result[0]

# 전체 글의 개수를 가져오는 함수.
def getContentCnt(content_board_idx) :
  # 쿼리문 작성.
  sql = '''
          select count(*) from content_table
          where content_board_idx = %s
        '''
  # 데이터 베이스 접속.
  conn = Connector.get_connection()
  cursor = conn.cursor()
  # %s에 지정될 값 설정.
  data = (content_board_idx)
  
  # 쿼리문 실행.
  cursor.execute(sql, data)
  result = cursor.fetchone()
  # 데이터 베이스 접속 종료
  conn.close()
  return result[0]
  