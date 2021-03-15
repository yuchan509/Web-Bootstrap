from flask import Flask, redirect

# Blueprint
from Blueprint.main_blueprint import main_blue
from Blueprint.board_blueprint import board_blue
from Blueprint.user_blueprint import user_blue

# server 역할을 할 객체 생성.
# template_folder : 랜더링할 html 문서가 있는 곳.(기본 - templates)
app = Flask(__name__, template_folder='Views', static_folder='static/upload')

# 세션 영역 사용을 위한 암호화 키를 설정.
app.secret_key = 'adf45d48vs1fslfpkf67qxdfr2ta'

# Blueprint 등록.
app.register_blueprint(main_blue)
app.register_blueprint(board_blue)
app.register_blueprint(user_blue)

# 주소만 입력하고 들어왔을 경우 호출될 부분.
@ app.route('/')
def index() :
    # 브라우저에게 main을 요청하라는 응답 결과를 전달.
    return redirect('main')

# server 가동.
# port=80 : 요청할 때 포트번호를 생략하고 요청 가능.
# debug=True : 코드를 수정할 때마다 서버 재가동.(실제 고객 이용시 제거.) 
app.run(port=80, debug=True) 