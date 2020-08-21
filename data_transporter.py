# data_transporter.py
# 컨트롤러에서 입력받은 값을 딕셔너리로 변환하여 Database 접근 모듈로 전달하는 모듈

# 이 모듈을 실행할 경우 메인 모듈의 메인 함수 호출
if __name__ == "__main__":
    import main
    main.main()


# insert 모듈에 값을 딕셔너리로 전달하는 클래스
class Add:
    def __init__(self):
        from db.insert import Insert
        self.db_in = Insert()
        self.value = {}

    # 연락처 추가
    def contact(self, contact_name, phone, email, group_srl):
        self.value = {"contact_name": contact_name, "phone": phone, "email": email, "group_srl": group_srl}
        db_status = self.db_in.contact(self.value)
        return db_status

    # 구분 추가
    def group(self, group_name):
        self.value = {"group_name": group_name}
        db_status = self.db_in.group(self.value)
        return db_status


# select 모듈에 값을 딕셔너리로 전달하는 클래스
class Find:
    def __init__(self):
        self.keyword = {}
        from db.select import Select
        self.db_sel = Select()

    # 연락처 검색
    def contact(self, keyword=0):
        # 검색어가 없는 경우 딕셔너리에 값을 추가하지 않음
        # select 모듈에서 빈 딕셔너리인 경우 모든 연락처를 가져오도록 하였음
        if keyword == 0:
            pass
        # 검색어가 입력된 경우 딕셔너리에 값을 추가함
        else:
            self.keyword = {"keyword": keyword}
        # select 모듈에서 처리한 내용을 받음
        # Database의 값을 딕셔너리로 받음
        contacts_list = self.db_sel.contacts(self.keyword)
        # 연락처 목록 반환
        return contacts_list

    # 구분 검색
    def group(self, keyword=0):
        # 검색어가 없는 경우 딕셔너리에 값을 추가하지 않음
        # select 모듈에서 빈 딕셔너리인 경우 모든 구분을 가져오도록 하였음
        if keyword == 0:
            pass
        # 검색어가 입력된 경우 딕셔너리에 값을 추가함
        else:
            self.keyword = {"keyword": keyword}
        # select 모듈에서 처리한 내용을 받음
        # Database의 값을 딕셔너리로 받음
        groups_list = self.db_sel.groups(self.keyword)
        # 구분 목록 반환
        return groups_list


# update 모듈에 값을 딕셔너리로 전달하는 클래스
class Modify:
    def __init__(self):
        from db.update import Update
        self.db_up = Update()
        self.change = {}

    # 연락처 이름 수정 메소드
    def contact_name(self, new_contact_name, contact_srl):
        self.change = {"new_contact_name": new_contact_name, "contact_srl": contact_srl}
        db_status = self.db_up.contact_name(self.change)
        return db_status

    # 연락처 전화번호 수정 메소드
    def phone(self, new_phone, contact_srl):
        self.change = {"new_phone": new_phone, "contact_srl": contact_srl}
        db_status = self.db_up.phone(self.change)
        return db_status

    # 연락처 이메일 수정 메소드
    def email(self, new_email, contact_srl):
        self.change = {"new_email": new_email, "contact_srl": contact_srl}
        db_status = self.db_up.email(self.change)
        return db_status

    # 연락처 구분 수정 메소드
    def contact_group_srl(self, new_group_srl, contact_srl):
        self.change = {"new_group_srl": new_group_srl, "contact_srl": contact_srl}
        db_status = self.db_up.contact_group_srl(self.change)
        return db_status

    # 구분 테이블의 구분명 수정 메소드
    def group_name(self, new_group_name, group_srl):
        self.change = {"new_group_name": new_group_name, "group_srl": group_srl}
        db_status = self.db_up.group_name(self.change)
        return db_status


# delete 모듈에 값을 딕셔너리로 전달하는 클래스
class Delete:
    def __init__(self):
        self.target = {}
        from db.delete import Delete
        self.db_del = Delete()

    # 연락처 삭제 메소드
    def contact(self, contact_srl, contact_name):
        self.target = {"contact_srl": contact_srl, "contact_name": contact_name}
        db_status = self.db_del.contact(self.target)
        return db_status

    # 구분 삭제 메소드
    def group(self, group_name):
        # 컨트롤러로부터 받은 구분명을 딕셔너리에 대입
        self.target = {"target": group_name}
        # db.delete 모듈에서 처리한 결과를 반환받음
        db_status = self.db_del.group(self.target)
        # 처리 결과 반환
        return db_status
