# update.py
# Database의 값을 수정하는 모듈

# Database 연결 모듈 import
import db.db_con as dbc

# 이 모듈을 실행할 경우 메인 모듈의 메인 함수 호출
if __name__ == "__main__":
    import main
    main.main()


# Database에 UPDATE 명령어를 실행하는 클래스
class Update:
    def __init__(self):
        self.conn = dbc.connect()
        self.cursor = self.conn.cursor()
        self.value = {}

    # 연락처 이름 수정
    def contact_name(self, value):
        self.value = value
        query = "UPDATE CONTACTS SET CONTACT_NAME = :new_contact_name WHERE CONTACT_SRL = :contact_srl"
        self.cursor.execute(query, self.value)
        self.cursor.close()
        db_status = dbc.disconnect(self.conn)
        return db_status

    # 연락처 전화번호 수정
    def phone(self, value):
        self.value = value
        query = "UPDATE CONTACTS SET PHONE = :new_phone WHERE CONTACT_SRL = :contact_srl"
        self.cursor.execute(query, self.value)
        self.cursor.close()
        db_status = dbc.disconnect(self.conn)
        return db_status

    # 연락처 이메일 주소 수정
    def email(self, value):
        self.value = value
        query = "UPDATE CONTACTS SET EMAIL = :new_email WHERE CONTACT_SRL = :contact_srl"
        self.cursor.execute(query, self.value)
        self.cursor.close()
        db_status = dbc.disconnect(self.conn)
        return db_status

    # 연락처 구분 수정
    def contact_group_srl(self, value):
        self.value = value
        query = "UPDATE CONTACTS SET GROUP_SRL = :new_group_srl WHERE CONTACT_SRL = :contact_srl"
        self.cursor.execute(query, self.value)
        self.cursor.close()
        db_status = dbc.disconnect(self.conn)
        return db_status

    # 구분명 수정
    def group_name(self, value):
        self.value = value
        query = "UPDATE GROUPS SET GROUP_NAME = :new_group_name WHERE GROUP_SRL = :group_srl"
        self.cursor.execute(query, self.value)
        self.cursor.close()
        db_status = dbc.disconnect(self.conn)
        return db_status
