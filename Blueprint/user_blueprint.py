from flask import Blueprint, render_template, request, session
from Database import user_dao


# Blueprint 객체 생성.
user_blue = Blueprint('user', __name__)


# 로그인.
@user_blue.route('/user_login')
def uesr_login() :
    # 파라미터 데이터 추출.
    login_fail = request.args.get('login_fail')

    # 응답 결과 랜더링.
    html = render_template('user/user_login.html', login_fail=login_fail)
    return html


# 회원 가입.
@user_blue.route('/user_join')
def user_join() :
    # 응답 결과 랜더링.
    html = render_template('user/user_join.html')
    return html


# 정보수정.
@user_blue.route('/user_modify')
def user_modify() :

    # 세션에 저장된 사용자 인덱스 번호를 가져옴.
    login_user_idx = session.get('login_user_idx')

    # 만약 로그인을 하지 않았다면 로그인 페이지로 강제 이동.
    if login_user_idx == None :
        return '''
                <script>
                alert('로그인을 해주세요')
                location.href = 'user_login'
                </script>
            '''

    # 로그인한 사용자 정보를 가져옴.
    login_user_data = user_dao.selectUserDataOne(login_user_idx)
    # print(login_user_data)


    # 응답 결과 랜더링.
    html = render_template('user/user_modify.html', login_user_data=login_user_data)
    return html 



# 회원가입 처리.
@user_blue.route('/user_join_pro', methods=["POST"])
def user_join_pro() :
    # 브라우저가 전달한 데이터 추출.
    # print(request.form)
    user_name = request.form.get('user_name')
    user_id   = request.form.get('user_id')
    user_pw   = request.form.get('user_pw')

    # 한글 안깨짐.
    # print(user_name)
    # print(user_id)
    # print(user_pw)
    
    # 데이터 베이스에 저장.
    user_dao.insertUserData(user_name, user_id, user_pw)
    return '''
            <script>
                alert('가입 완료')
                location.href = 'user_login'
            </script>
        '''


# 아이디 중복 확인.
@user_blue.route('/check_join_id')
def check_join_id() :
    # 브라우저가 보낸 아이디를 추출.
    new_id = request.args.get('new_id')
    # 중복 확인.
    result = user_dao.checkInputUserid(new_id)
    return f'{result}'


# 로그인 처리.
@user_blue.route('/user_login_pro', methods=['post'])
def user_login_pro() :
    # 브라우저가 전달할 데이터를 추출.
    user_id = request.form.get('user_id')
    user_pw = request.form.get('user_pw')
    # print(user_id)
    # print(user_pw)
    
    # 사용자 존재 여부 확인.
    result = user_dao.check_login_user(user_id, user_pw)
    # print(result)

    # 로그인 실패
    if result == None :
        return ''' 
                <script>
                    alert('아이디와 비밀번호를 다시 확인해주세요')
                    location.href = 'user_login?login_fail=true'
                </script>
                '''
    else :
        # 세션에 로그인한 사용자의 번호를 담아줌.
        session['login_user_idx'] = result[0]

        return ''' 
                <script>
                    alert('로그인에 성공하셨습니다')
                    location.href = 'main'
                </script>
                '''

# 사용자 정보 수정 처리.
@user_blue.route('/user_modify_pro', methods=['post'])
def user_modify_pro() :

    # 파라미터 데이터 추출.
    user_pw = request.form.get('user_pw')
    # print(user_pw)

    # 세션에서 로그인한 인덱스를 가져옴.
    login_user_idx = session.get('login_user_idx')
    # print(login_user_idx)

    # 사용자 정보 업데이트.
    user_dao.updateUserData(login_user_idx, user_pw)
   
    return ''' 
                <script>
                    alert('사용자 정보가 수정되었습니다.')
                    location.href = 'user_modify'
                </script>
                '''

# 로그아웃.
@user_blue.route('/user_logout')
def user_logout() :
    # 세션 영역에서 login_user_idx를 제거.
    del session['login_user_idx']

    return ''' 
                <script>
                    alert('로그아웃 되었습니다.')
                    location.href = 'main'
                </script>
                '''
