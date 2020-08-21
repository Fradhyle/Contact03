# db_con.py
# Database 연결 모듈

# Oracle Database 연결을 위한 모듈 import
import cx_Oracle

# 이 모듈을 실행할 경우 메인 모듈의 메인 함수 호출
if __name__ == "__main__":
    import main
    main.main()


# Database 연결 후 연결 정보 반환하는 함수
def connect():
    connection = cx_Oracle.connect("ora_user/1234@pc.pdmnu.com:1521/xe")
    return connection


# Database Commit 실행 후 연결을 종료하는 함수
def disconnect(connection):
    # Database Commit 실행
    connection.commit()
    # Database 연결 종료
    connection.close()
    try:
        # Database 연결 확인, 연결이 종료된 경우 오류 발생
        connection.ping()
    # Database 연결이 종료되었을 경우 발생하는 오류 처리
    except connection.DatabaseError:
        # 정상 종료 상태 반환
        return 0
