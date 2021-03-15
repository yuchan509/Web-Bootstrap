from Database import Connector, user_dao, board_dao, content_dao

# 데이터 베이스 접속 테스트.
# conn = Connector.get_connection()
# print(conn)
# print('연결 성공')
# conn.close()
# print('연결 종료')


# 사용자 정보 저장 테스트
# user_dao.insertUserData('홍길동', 'abcs', '1234')
# user_dao.insertUserData('김길동', 'aaaa', '1234')
# user_dao.insertUserData('최길동', 'bbbb', '1234') 
# print('저장완료')


# 모든 사용자 정보를 가져오는 테스트.
# result = user_dao.selectUserDataAll()
# print(result)


# 사용자 한명의 정보를 가져오는 테스트.
# result = user_dao.selectUserDataOne(1)
# print(result)


# 사용자 한명의 정보를 수정하는 테스트.
# user_dao.updateUserData(1, '9999')


# 사용자 한명의 정보를 삭제하는 테스트.
# user_dao.deleteUserData(1)


# 게시판 정보 추가 테스트.
# board_dao.insertUserData('테스트 게시판')


# 게시판 정보를 모두 가져오는 테스트.
# result = board_dao.selectBoardDataAll()
# print(result)


# 게시판 정보를 하나 가져오는 테스트.
# result = board_dao.selectBoardDatOne(1)
# print(result)


# 게시판 정보를 수정하는 테스트.
# board_dao.updateBoardData('변경된 게시판', 1)


# 게시판 정보를 삭제하는 테스트.
#board_dao.deleteUserData(1)


# 게시글 정보를 저장하는 테스트.
# content_dao.insertContentData('테스트 제목', 17, '테스트 내용', 'aaa.jpg', 2)


# 게시글 전부를 가져오는 테스트.
# result = content_dao.selectContentDataAll()
# print(result)


# 하나의 게시글 정보를 가져오는 테스트.
# result = content_dao.selectContentDataOne(1)
# print(result)

# 게시글을 수정하는 테스트
# content_dao.updateContentData('수정된제목', 2, '수정된내용', 'bbb.jpg', 2, 2)

# 게시글을 삭제하는 테스트.
# ontent_dao.deleteContentData(2)
