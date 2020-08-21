# delete.py
# Database의 값을 삭제하는 모됼

# Database 연결 모듈 import
import db.db_con as dbc

# 이 모듈을 실행할 경우 메인 모듈의 메인 함수 호출
if __name__ == "__main__":
    import main
    main.main()


# Database에 DELETE 명령어를 실행하는 클래스
class Delete:
    def __init__(self):
        self.conn = dbc.connect()
        self.cursor = self.conn.cursor()
        self.target = {}

    # CONTACTS 테이블에서 DELETE 실행
    def contact(self, target):
        self.target = target
        query = "DELETE FROM CONTACTS WHERE CONTACT_SRL = :contact_srl AND CONTACT_NAME = :contact_name"
        self.cursor.execute(query, self.target)
        self.cursor.close()
        db_status = dbc.disconnect(self.conn)
        return db_status

    # GROUPS 테이블에서 DELETE 실행
    def group(self, target):
        self.target = target
        query = "DELETE FROM GROUPS WHERE GROUP_NAME = :target"
        self.cursor.execute(query, self.target)
        self.cursor.close()
        db_status = dbc.disconnect(self.conn)
        return db_status
