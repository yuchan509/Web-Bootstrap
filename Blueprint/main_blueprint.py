from flask import Blueprint, render_template, session
from Database import board_dao, content_dao

# Blueprint 객체 생성.
main_blue = Blueprint('main', __name__)

# main을 요청하면 호출되는 함수.
@main_blue.route('/main')
def main() :
    # 게시판 이름 정보를 가져옴.
    board_data = board_dao.selectBoardDataAll()
    # print(board_data)
    
    # 각 게시판별 상위글 5개를 담을 리스트.
    content_List = []
    for board_idx, board_name in board_data :
        a = content_dao.selectContentDataAll(board_idx, 1)
        # print(a[:5])
        content_List.append(a[:5])
    # print(content_List)


    # html 데이터를 랜더링.
    html = render_template('main/main.html', board_data=board_data, content_List=content_List)
    return html