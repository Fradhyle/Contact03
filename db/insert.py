# insert.py
# Database에 값을 삽입하는 모듈

# Database 연결 모듈 import
import db.db_con as dbc

# 이 모듈을 실행할 경우 메인 모듈의 메인 함수 호출
if __name__ == "__main__":
    import main
    main.main()


# Database에 INSERT 명령어를 실행하는 클래스
class Insert:
    def __init__(self):
        self.conn = dbc.connect()
        self.value = {}
        self.cursor = self.conn.cursor()

    # CONTACTS 테이블에서 INSERT 실행
    def contact(self, value):
        self.value = value
        query = "INSERT INTO CONTACTS (CONTACT_SRL, CONTACT_NAME, PHONE, EMAIL, GROUP_SRL) " \
                "VALUES (CONTACT_SRL_SEQ.NEXTVAL, :contact_name, :phone, :email, :group_srl)"
        self.cursor.execute(query, self.value)
        self.cursor.close()
        db_status = dbc.disconnect(self.conn)
        return db_status

    # GROUPS 테이블에서 INSERT 실행
    def group(self, value):
        self.value = value
        query = "INSERT INTO GROUPS (GROUP_SRL, GROUP_NAME) VALUES (GROUP_SRL_SEQ.NEXTVAL, :group_name)"
        self.cursor.execute(query, self.value)
        self.cursor.close()
        db_status = dbc.disconnect(self.conn)
        return db_status
