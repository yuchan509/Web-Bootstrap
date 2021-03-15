from flask import Blueprint, render_template, session, request
from Database import board_dao, content_dao
import os, time

# 게시판 리스트 페이지.
board_blue = Blueprint('board', __name__)

# 게시글 리스트
@board_blue.route('/board_main')
def board_main() :
    # 파라미터 데이터 추출
    board_idx = request.args.get('board_idx')
    
    page = request.args.get('page')
    if page == None :
        page = '1'
    page = int(page)

    # 페이지 번호가 0이하면 무조건 1페이지를 의미.
    if page < 1 :
        page = 1

    # 전체 글의 개수를 가져옴.
    content_cnt = content_dao.getContentCnt(board_idx)
    # print(content_cnt)

    # 전체 글의 개수를 이용해 전체 페이지 수를 구함.
    pageCnt = content_cnt // 10

    if pageCnt % 10 > 0 :
        pageCnt += 1

    # 게시판 정보를 가져옴.
    board_data = board_dao.selectBoardDatOne(board_idx)
    # print(f'---------------- {board_data}')

    # 현재 게시판의 글 목록을 가져옴.
    content_list = content_dao.selectContentDataAll(board_idx, page)

    # 현재 페이지 번호를 이용하여 pagenation 시작값을 구함.
    start_page = ((page - 1) // 10 * 10) + 1

    # 전체 페이지 수를 이용하여 pagenation 종료값을 구함.
    end_page = start_page + 9
    if end_page > pageCnt :
        end_page = pageCnt

   # 현재 페이지 번호가 전체 페이지 개수보다 크면 전체 페이지 개수로 넣어줌.
    if page > pageCnt :
        page = pageCnt

    # 응답결과를 랜더링.
    html = render_template('board/board_main.html', board_data=board_data, content_list=content_list, 
                            board_idx=board_idx, start_page=start_page, end_page=end_page, pageCnt=pageCnt, 
                            page=page)
    return html



# 게시글 보는 페이지.
@board_blue.route('/board_read')
def board_read() :
    # 파라미터 데이터 추출.
    content_idx = request.args.get('content_idx')
    board_idx = request.args.get('board_idx')
    page = request.args.get('page')
    # print(content_idx)
    # print(board_idx)

    # 현재 글 정보를 가져옴.
    content_data = content_dao.selectContentDataOne(content_idx)
    # print(content_data)

    # 응답 결과 랜더링.
    html = render_template('board/board_read.html', content_data=content_data, 
                        board_idx=board_idx, page=page, content_idx=content_idx)
    return html


# 글 수정 페이지.
@board_blue.route('/board_modify')
def board_modify() :
    # 파라미터 데이터 추출.
    content_idx = request.args.get('content_idx')
    board_idx = request.args.get('board_idx')
    page = request.args.get('page')

    # 현재 글 정보를 가져옴.
    content_data = content_dao.selectContentDataOne(content_idx)

    # 응답 결과 랜더링.
    html = render_template('board/board_modify.html', content_data=content_data, content_idx=content_idx,
                            board_idx=board_idx, page=page)
    return html


# 글 작성 페이지.
@board_blue.route('/board_write')
def board_write() :
    # 파라미터 데이터 추출.
    board_idx = request.args.get('board_idx')
    # print(board_idx)

    # 응답 결과 랜더링.
    html = render_template('board/board_write.html', board_idx=board_idx)
    return html


# 글 작성 처리.
@board_blue.route('/board_write_pro', methods=['post'])
def board_write_pro() :

    # 데이터를 추출.
    content_subject = request.form.get('content_subject')
    content_writer_idx = session.get('login_user_idx')
    content_text = request.form.get('content_text')
    content_board_idx = request.form.get('content_board_idx')

    # print(content_subject)
    # print(content_writer_idx)
    # print(content_text)
    # print(content_board_idx)

    # 업로드 처리.
    # 첨부한 파일이 있을 경우.
    if request.files.get('content_file').filename != '' :
        # contetn_file로 넘어오는 파일 데이터를 추출.
        content_file = request.files.get('content_file')
        # 중복을 방지하기 위해 파일 이름에 시간을 붙여줌.
        file_name = str(int(time.time())) + content_file.filename
        # print(file_name)
        # 경로를 포함한 파일 경로 생성.
        path = os.getcwd() + '/static/upload/' + file_name
        # print(path)
        # 저장.
        content_file.save(path)
    

    # 첨부를 하지 않았을 경우.
    else :
        file_name = None
   
    # 데이터 베이스에 저장.
    content_dao.insertContentData(content_subject, content_writer_idx, content_text, file_name, content_board_idx)

    # 방금 작성한 글의 인덱스를 추출.
    now_content_idx = content_dao.getMaxConetentIdx(content_board_idx)
    # print(now_content_idx)
    
    return f'''
            <script>
                alert('작성되었습니다')
                location.href = 'board_read?content_idx={now_content_idx}&board_idx={content_board_idx}'
            </script>
           '''

# 삭제.
@board_blue.route('/board_delete')
def board_delete() :
    # 파라미터 데이터를 가져오기.
    content_idx = request.args.get('content_idx')
    board_idx = request.args.get('board_idx')
    page = request.args.get('page')

    # 삭제.
    content_dao.deleteContentData(content_idx)

    return f'''
            <script>
                alert('삭제되었습니다.')
                location.href = 'board_main?board_idx={board_idx}&page={page}'
            </script>
             '''
# 글 수정 처리.
@board_blue.route('/board_modify_pro', methods=['post'])
def board_modify_pro():

    # 데이터를 추출.
    content_subject = request.form.get('content_subject')
    content_text = request.form.get('content_text')
    content_idx = request.form.get('content_idx')
    board_idx = request.form.get('board_idx')
    page = request.form.get('page')
    # print(content_subject)
    # print(content_text)
    # print(content_idx)
    # print(board_idx)
    # print(page)
    
    # 업로드 처리.
    # 첨부한 파일이 있을 경우.
    if request.files.get('content_file').filename != '' :
        # contetn_file로 넘어오는 파일 데이터를 추출.
        content_file = request.files.get('content_file')
        # 중복을 방지하기 위해 파일 이름에 시간을 붙여줌.
        file_name = str(int(time.time())) + content_file.filename
        # print(file_name)
        # 경로를 포함한 파일 경로 생성.
        path = os.getcwd() + '/static/upload/' + file_name
        # print(path)
        # 저장.
        content_file.save(path)
    

    # 첨부를 하지 않았을 경우.
    else :
        file_name = None
    # print(file_name)

    # 수정 처리.
    content_dao.updateContentData(content_subject, content_text, file_name, content_idx)
    return f'''
            <script>
                alert('수정되었습니다.')
                location.href = 'board_read?content_idx={content_idx}'
                                + '&board_idx={board_idx}&page={page}'
            </script>
            '''