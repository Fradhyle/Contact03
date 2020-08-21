# select.py
# Database에서 값을 조회하는 모듈

# Database 연결 모듈 import
import db.db_con as dbc

# 이 모듈을 실행할 경우 메인 모듈의 메인 함수 호출
if __name__ == "__main__":
    import main
    main.main()


# Database에 SELECT 명령어를 실행하는 클래스
class Select:
    def __init__(self):
        self.keyword = {}

    def contacts(self, keyword={}):
        conn = dbc.connect()
        cursor = conn.cursor()
        self.keyword = keyword
        if self.keyword:
            query = "SELECT a.CONTACT_SRL, a.CONTACT_NAME, a.PHONE, a.EMAIL, a.GROUP_SRL, b.GROUP_NAME " \
                    "FROM CONTACTS a, GROUPS b " \
                    "WHERE a.CONTACT_NAME = :keyword " \
                    "AND a.GROUP_SRL = b.GROUP_SRL " \
                    "ORDER BY a.CONTACT_SRL"
            cursor.execute(query, self.keyword)
        else:
            query = "SELECT a.CONTACT_SRL, a.CONTACT_NAME, a.PHONE, a.EMAIL, a.GROUP_SRL, b.GROUP_NAME " \
                    "FROM CONTACTS a, GROUPS b " \
                    "WHERE a.GROUP_SRL = b.GROUP_SRL " \
                    "ORDER BY a.CONTACT_SRL"
            cursor.execute(query)
        contact_srl = []
        contact_name = []
        phone = []
        email = []
        group_srl = []
        group_name = []
        for row in cursor:
            contact_srl.append(row[0])
            contact_name.append(row[1])
            phone.append(row[2])
            email.append(row[3])
            group_srl.append(row[4])
            group_name.append(row[5])
        cursor.close()
        db_status = dbc.disconnect(conn)
        if db_status == 0:
            return {"contact_srl": contact_srl, "contact_name": contact_name, "phone": phone, "email": email,
                         "group_srl": group_srl, "group_name": group_name}

    def groups(self, keyword={}):
        conn = dbc.connect()
        cursor = conn.cursor()
        self.keyword = keyword
        if self.keyword:
            query = "SELECT GROUP_SRL, GROUP_NAME FROM GROUPS WHERE GROUP_NAME = :keyword ORDER BY GROUP_SRL"
            cursor.execute(query, self.keyword)
        else:
            query = "SELECT GROUP_SRL, GROUP_NAME FROM GROUPS ORDER BY GROUP_SRL"
            cursor.execute(query)
        group_srl = []
        group_name = []
        for row in cursor:
            group_srl.append(row[0])
            group_name.append(row[1])
        cursor.close()
        db_status = dbc.disconnect(conn)
        if db_status == 0:
            return {"group_srl": group_srl, "group_name": group_name}
