# menu_controller.py
# 메인 메뉴로 받은 명령을 처리하는 컨트롤러 모듈

# 정규 표현식 모듈 import
import re
# 데이터 전송 모듈 import
import data_transporter as dt

# 이 모듈을 실행할 경우 메인 모듈의 메인 함수 호출
if __name__ == "__main__":
    import main
    main.main()


# 연락처 목록 보기
def list_contacts():
    # 데이터 전송 모듈의 검색 클래스 호출
    dt_find = dt.Find()
    # 데이터 전송 모듈로부터 연락처 목록 딕셔너리 반환
    contacts_list = dt_find.contact()
    # 연락처 목록 딕셔너리 반환
    return contacts_list


# 구분 목록 보기
def list_groups():
    # 데이터 전송 모듈의 검색 클래스 호출
    dt_find = dt.Find()
    # 데이터 전송 모듈로부터 구분 목록 딕셔너리 반환
    groups_list = dt_find.group()
    # 구분 목록 딕셔너리 반환
    return groups_list


# 연락처 추가
def add_contact():
    # 데이터 전송 모듈에서 추가 클래스 호출
    dt_add = dt.Add()
    # 추가할 이름 입력
    contact_name = input("이름을 입력하세요: ")
    while True:
        # 전화번호 중복을 확인하기 위해 연락처 목록을 불러옴
        contacts_list = list_contacts()
        # 불러온 연락처 목록에서 휴대전화 목록만 추출
        phone_list = contacts_list["phone"]
        # 전화번호 입력
        phone_input = input("전화번호를 입력하세요('-' 제외): ")
        # 전화번호를 너무 짧거나 너무 길게 입력한 경우
        if len(phone_input) <= 9 or len(phone_input) >= 12:
            print("전화번호를 잘못 입력하였습니다.")
            continue
        # 전화번호 확인을 위한 정규표현식 패턴 선언
        pattern = re.compile("\d{9,12}")
        # 입력한 값이 정규표현식 패턴과 일치하는지 확인
        regex_result = pattern.search(phone_input)
        # 입력한 값이 정규표현식 패턴과 일치하는 경우
        if regex_result:
            # 패턴과 일치한 값을 추출
            phone = regex_result.group()
        # 입력한 값이 정규표현식 패턴과 일치하지 않는 경우
        else:
            print("잘못 입력하였습니다. 다시 입력하세요.")
            continue
        # 정규표현식을 이용하여 추출한 값이 기존 전화번호 목록에 있는지 확인
        if phone in phone_list:
            print("이미 존재하는 전화번호입니다. 다시 입력하세요.")
            continue
        # 위 검사를 모두 통과한 경우
        else:
            break
    while True:
        # 이메일 주소 입력
        email_input = input("이메일 주소를 입력하세요: ")
        # 이메일 형식에 맞는지 확인하기 위하여 정규표현식 패턴 선언
        pattern = re.compile("\S+@\S+[.]\S+")
        # 입력한 값이 정규표현식 패턴과 일치하는지 확인
        regex_result = pattern.search(email_input)
        # 입력한 값이 정규표현식 패턴과 일치하는 경우
        if regex_result:
            # 패턴과 일치한 값을 추출
            email = regex_result.group()
            break
        # 입력한 값이 정규표현식 패턴과 일치하지 않는 경우
        else:
            print("잘못 입력하였습니다. 다시 입력하세요.")
            continue
    # 구분 입력 단계 시작
    print("현재 등록된 구분은 다음과 같습니다.")
    # 현재 등록된 구분 목록 불러오기
    groups_list = list_groups()
    # 등록된 구분명 목록만 추출
    group_name_list = groups_list["group_name"]
    # 구분명 목록 출력
    list_number = 1
    for group_name in group_name_list:
        print(list_number, end=". ")
        print(group_name)
        list_number += 1
    while True:
        # 구분명 입력
        group_name = input("위 목록에서 구분을 선택하여 입력하세요: ")
        # 연락처에 입력할 구분 순번 저장 변수 초기화
        group_srl = 0
        # 입력한 구분명이 불러온 구분명 목록에 있는 경우
        if group_name in group_name_list:
            # 구분 순번을 정확히 가져오기 위해 GROUPS 테이블에서 재검색 필요
            # 데이터 전송 모듈의 검색 클래스 호출
            dt_find = dt.Find()
            # 구분명 검색 후 결과값 반환
            groups_list = dt_find.group(group_name)
            # 반환된 딕셔너리에서 구분 순번 목록만 추출하여 해당 값을 정수값으로 대입
            group_srl = int(groups_list["group_srl"][0])
            break
        # 구분명을 잘못 입력한 경우
        else:
            print("존재하지 않는 구분을 입력하셨습니다. 다시 입력하세요.")
            continue
    # 데이터 전송 모듈의 추가 클래스에서 연락처 추가 함수 호출
    # 정상적으로 처리된 경우 반환된 Database 상태값을 대입
    db_status = dt_add.contact(contact_name, phone, email, group_srl)
    # Database에서 정상적으로 처리된 경우
    if db_status == 0:
        # 새로 입력된 연락처 반환
        return {"contact_name": contact_name, "phone": phone, "email": email, "group_name": group_name}
    # Database에서 정상적으로 처리되지 않은 경우
    else:
        return 0


# 연락처 수정
def modify_contact():
    # 데이터 전송 모듈에서 수정 클래스 호출
    dt_mod = dt.Modify()
    # 검색어 입력
    keyword = input("수정하려는 연락처의 이름을 입력하세요: ")
    # 데이터 전송 모듈에서 검색 클래스 호출
    dt_find = dt.Find()
    # 입력한 값으로 연락처 목록에서 이름 검색
    result = dt_find.contact(keyword)
    # 연락처 목록이 있는 경우
    contact_srl_list = result["contact_srl"]
    if contact_srl_list:
        # 결과값 딕셔너리에 저장된 값을 리스트에 대입
        contact_name_list = result["contact_name"]
        phone_list = result["phone"]
        email_list = result["email"]
        group_name_list = result["group_name"]
        # PK를 이용하여 검색된 연락처 개수 확인
        list_length = len(contact_srl_list)
        selection = 0
        # 검색된 연락처가 1개인 경우
        if list_length == 1:
            selection = 1
        # 검색된 연락처가 2개 이상인 경우
        elif list_length > 1:
            list_number = 1
            i = 0
            # 검색된 연락처 개수 출력
            print(f"총 {list_length}개의 연락처를 발견하였습니다.")
            # 검색된 연락처 순차 출력
            for _ in contact_srl_list:
                print(list_number, end=".\n")
                print("이름:", contact_name_list[i])
                print("전화번호:", phone_list[i])
                print("이메일 주소:", email_list[i])
                print("구분:", group_name_list[i])
                print()
                list_number += 1
                i += 1
            while True:
                try:
                    # 번호 선택 입력
                    selection = int(input("어떤 연락처를 수정하시겠습니까? "))
                except ValueError:
                    print("잘못 입력하였습니다.")
                    continue
                else:
                    break
        # 올바른 인덱스 지정을 위한 -1 처리
        selection -= 1
        # 해당 인덱스의 값 대입
        contact_srl = contact_srl_list[selection]
        contact_name = contact_name_list[selection]
        phone = phone_list[selection]
        email = email_list[selection]
        group_name = group_name_list[selection]
        # 선택 확인
        print("이름:", contact_name)
        print("전화번호:", phone)
        print("이메일 주소:", email)
        print("구분:", group_name)
        while True:
            try:
                selection = int(input("이 연락처를 수정하시겠습니까?\n"
                                      "1. 예\n"
                                      "2. 아니오\n"))
            # 잘못된 값을 입력한 경우
            except ValueError:
                print("잘못 입력하였습니다.")
                continue
            # 수정하기로 선택한 경우
            if selection == 1:
                while True:
                    try:
                        # 선택할 항목 선택
                        selection = int(input("어떤 정보를 수정하시겠습니까?\n"
                                              "1. 이름\n"
                                              "2. 전화번호\n"
                                              "3. 이메일 주소\n"
                                              "4. 구분\n"))
                    # 잘못된 값을 입력한 경우
                    except ValueError:
                        print("잘못 입력하였습니다.")
                        continue
                    # 이름을 수정하기로 선택한 경우
                    if selection == 1:
                        new_contact_name = input("변경할 새 연락처 이름을 입력하세요: ")
                        result = dt_mod.contact_name(new_contact_name, contact_srl)
                        print(result)
                        if result == 0:
                            return {"contact_name": contact_name, "phone": phone, "new_contact_name": new_contact_name}
                    # 전화번호를 수정하기로 선택한 경우
                    elif selection == 2:
                        while True:
                            # 전화번호 중복을 확인하기 위해 연락처 목록을 불러옴
                            contacts_list = list_contacts()
                            # 불러온 연락처 목록에서 휴대전화 목록만 추출
                            phone_list = contacts_list["phone"]
                            # 전화번호 입력
                            new_phone_input = input("변경할 새 연락처 전화번호을 입력하세요: ")
                            # 전화번호를 너무 짧거나 너무 길게 입력한 경우
                            if len(new_phone_input) <= 9 or len(new_phone_input) >= 12:
                                print("전화번호를 잘못 입력하였습니다.")
                                continue
                            # 전화번호 확인을 위한 정규표현식 패턴 선언
                            pattern = re.compile("\d{9,12}")
                            # 입력한 값이 정규표현식 패턴과 일치하는지 확인
                            regex_result = pattern.search(new_phone_input)
                            # 입력한 값이 정규표현식 패턴과 일치하는 경우
                            if regex_result:
                                # 패턴과 일치한 값을 추출
                                new_phone = regex_result.group()
                            # 입력한 값이 정규표현식 패턴과 일치하지 않는 경우
                            else:
                                print("잘못 입력하였습니다. 다시 입력하세요.")
                                continue
                            # 정규표현식을 이용하여 추출한 값이 기존 전화번호 목록에 있는지 확인
                            if new_phone in phone_list:
                                print("이미 존재하는 전화번호입니다. 다시 입력하세요.")
                                continue
                            # 위 검사를 모두 통과한 경우
                            else:
                                break
                        # 데이터 전송 모듈의 수정 클래스에서 전화번호 수정 함수 호출
                        db_status = dt_mod.phone(new_phone, contact_srl)
                        # Database에서 정상적으로 처리된 경우
                        if db_status == 0:
                            # 수정한 연락처의 이름, 전화번호, 새 전화번호 반환
                            return {"contact_name": contact_name, "phone": phone, "new_phone": new_phone}
                    # 이메일 주소를 수정하기로 선택한 경우
                    elif selection == 3:
                        while True:
                            # 이메일 주소 입력
                            new_email_input = input("변경할 새 연락처 이메일을 입력하세요: ")
                            # 이메일 형식에 맞는지 확인하기 위하여 정규표현식 패턴 선언
                            pattern = re.compile("\S+@\S+[.]\S+")
                            # 입력한 값이 정규표현식 패턴과 일치하는지 확인
                            regex_result = pattern.search(new_email_input)
                            # 입력한 값이 정규표현식 패턴과 일치하는 경우
                            if regex_result:
                                # 패턴과 일치한 값을 추출
                                new_email = regex_result.group()
                                break
                            # 입력한 값이 정규표현식 패턴과 일치하지 않는 경우
                            else:
                                print("잘못된 이메일 주소입니다. 다시 입력하세요.")
                                continue
                        # 데이터 전송 모듈의 수정 클래스에서 이메일 수정 함수 호출
                        result = dt_mod.email(new_email, contact_srl)
                        if result == 0:
                            # 수정한 연락처의 이름, 전화번호, 새 이메일 주소 반환
                            return {"contact_name": contact_name, "phone": phone, "new_email": new_email}
                    # 구분을 수정하기로 선택한 경우
                    elif selection == 4:
                        # 구분 수정 단계 시작
                        print("현재 등록된 구분은 다음과 같습니다.")
                        # 현재 등록된 구분 목록 불러오기
                        groups_list = list_groups()
                        # 등록된 구분명 목록만 추출
                        group_name_list = groups_list["group_name"]
                        # 구분명 목록 출력
                        list_number = 1
                        # 구분명 목록 순차 출력
                        for group_name in group_name_list:
                            print(list_number, end=". ")
                            print(group_name)
                            list_number += 1
                        while True:
                            # 구분명 입력
                            new_group_name = input("위 목록 중 하나의 구분명을 입력하세요: ")
                            if new_group_name in group_name_list:
                                # 입력한 구분명을 구분명 테이블에서 다시 확인
                                groups_list = dt_find.group(new_group_name)
                                # 확인 후 해당 구분명의 순번 대입
                                new_group_srl = int(groups_list["group_srl"][0])
                                break
                            else:
                                print("잘못 입력하였습니다.")
                                continue
                        # 데이터 전송 모듈의 구분 수정 기능 호출, 처리 후 결과값 대입
                        result = dt_mod.contact_group_srl(new_group_srl, contact_srl)
                        # 정상 처리된 경우
                        if result == 0:
                            # 수정한 연락처 이름, 전화번호, 수정된 구분명 반환
                            return {"contact_name": contact_name, "phone": phone, "new_group_name": new_group_name}
                    # 수정할 항목 선택을 잘못 입력한 경우
                    else:
                        print("잘못 입력하였습니다.")
                        continue
            # 수정하지 않기로 선택한 경우
            elif selection == 2:
                return 2
            # 선택을 잘못 입력한 경우
            else:
                print("잘못 입력하였습니다.")
                continue
    # 검색한 결과가 없는 경우
    else:
        return -1


# 연락처 삭제
def delete_contact():
    # 데이터 전송 모듈에서 검색 클래스 호출
    data_find = dt.Find()
    # 검색어 입력
    keyword = input("삭제하려는 연락처의 이름을 입력하세요: ")
    # 입력한 값으로 연락처 목록에서 이름 검색
    result = data_find.contact(keyword)
    # 연락처 목록이 있는 경우
    contact_srl_list = result["contact_srl"]
    if contact_srl_list:
        # 결과값 딕셔너리에 저장된 값을 리스트에 대입
        contact_name_list = result["contact_name"]
        phone_list = result["phone"]
        email_list = result["email"]
        group_name_list = result["group_name"]
        # PK를 이용하여 검색된 연락처 개수 확인
        list_length = len(contact_srl_list)
        selection = 0
        if list_length == 1:
            selection = 1
        elif list_length > 1:
            list_number = 1
            i = 0
            print(f"총 {list_length}개의 연락처를 발견하였습니다.")
            for _ in contact_srl_list:
                print(list_number, end=".\n")
                print("이름:", contact_name_list[i])
                print("전화번호:", phone_list[i])
                print("이메일 주소:", email_list[i])
                print("구분:", group_name_list[i])
                list_number += 1
                i += 1
            selection = 0
            while True:
                try:
                    selection = int(input("어떤 연락처를 삭제하시겠습니까? "))
                except ValueError:
                    print("잘못 입력하였습니다.")
                    continue
                else:
                    break
        selection -= 1
        contact_srl = contact_srl_list[selection]
        contact_name = contact_name_list[selection]
        phone = phone_list[selection]
        email = email_list[selection]
        group_name = group_name_list[selection]
        print("이름:", contact_name)
        print("전화번호:", phone)
        print("이메일 주소:", email)
        print("구분:", group_name)
        while True:
            try:
                selection = int(input("이 연락처를 삭제하시겠습니까?\n"
                                      "1. 예\n"
                                      "2. 아니오\n"))
            except ValueError:
                print("잘못 입력하였습니다.")
                continue
            if selection == 1:
                dt_del = dt.Delete()
                result = dt_del.contact(contact_srl, contact_name)
                if result == 0:
                    return {"contact_name": contact_name, "phone": phone}
            elif selection == 2:
                return 2
            else:
                print("잘못 입력하였습니다.")
                continue
    else:
        return -1


# 구분 추가
def add_group():
    dt_add = dt.Add()
    groups_list = list_groups()
    group_name_list = groups_list["group_name"]
    while True:
        value = input("추가할 구분명을 입력하세요: ")
        if value in group_name_list:
            print("이미 존재하는 구분명입니다. 다시 입력하세요.")
            continue
        else:
            break
    db_status = dt_add.group(value)
    if db_status == 0:
        return {"group_name": value}


# 구분 수정
def modify_group():
    # 구분명 검색 및 중복을 확인하기 위해 모든 구분명 불러오기
    groups_list = list_groups()
    group_name_list = groups_list["group_name"]
    old_group_name = input("변경하고자 하는 구분명을 입력하세요: ")
    # 데이터 전송 모듈에서 검색 클래스 호출
    dt_find = dt.Find()
    # 입력한 검색어가 존재하는지 확인
    result = dt_find.group(old_group_name)
    # 입력한 검색어가 존재하는 경우
    if old_group_name in group_name_list:
        while True:
            # 새 구분명 입력
            new_group_name = input("변경할 새 구분명을 입력하세요: ")
            # 입력한 새 구분명이 이미 구분명 목록에 존재하는 경우(기존 값 포함)
            if new_group_name in group_name_list:
                print("이미 존재하는 구분명입니다. 다시 입력하세요.")
                continue
            else:
                try:
                    # 구분명 수정 최종 확인
                    selection = int(input(f"구분명 '{old_group_name}'을/를 '{new_group_name}(으)로 수정하시겠습니까?\n"
                                          "1. 예\n"
                                          "2. 아니오\n"))
                # 잘못 입력한 경우 예외 처리
                except ValueError:
                    print("잘못 입력하였습니다.")
                    continue
            # 변경을 선택한 경우
            if selection == 1:
                group_srl = result["group_srl"][0]
                # 데이터 전송 모듈의 수정 클래스 호출
                dt_mod = dt.Modify()
                # 그룹 수정 메소드 실행
                db_status = dt_mod.group_name(new_group_name, group_srl)
                # 정상 처리된 경우
                if db_status == 0:
                    # 이전 구분명, 변경된 구분명 반환
                    return {"old_group_name": old_group_name, "new_group_name": new_group_name}
            # 변경하지 않기로 선택한 경우
            elif selection == 2:
                return 0
            # 잘못 입력한 경우
            else:
                print("잘못 입력하였습니다.")
                continue
    # 결과가 없는 경우
    else:
        return -1


# 구분 삭제 함수
def delete_group():
    while True:
        # 연락처 목록 불러오기
        contacts_list = list_contacts()
        # 현재 사용중인 구분을 확인하기 위해 불러온 연락처 목록에서 구분 순번만 추출
        contacts_group_srl_list = contacts_list["group_srl"]
        keyword = input("삭제할 구분명을 입력하세요: ")
        # 데이터 전송 모듈의 검색 클래스 호출
        dt_find = dt.Find()
        # 입력한 검색어를 검색하여 반환받은 딕셔너리를 대입
        result = dt_find.group(keyword)
        group_srl_list = result["group_srl"]
        if group_srl_list:
            # 반환받은 딕셔너리에서 구분 순번 리스트 추출
            group_srl = result["group_srl"][0]
            # 검색하여 반환받은 구분 순번이 전체 연락처 목록의 구분 순번 목록에 있는지 확인
            if group_srl in contacts_group_srl_list:
                # 상태값 반환
                return 0
            # 검색하여 반환받은 딕셔너리에서 구분명 리스트 추출
            group_name = result["group_name"]
            # 검색하여 반환받은 딕셔너리에 구분명이 있는 경우
            if group_name:
                # 검색한 구분명 출력
                print("삭제할 구분명:", group_name[0])
                while True:
                    # 올바른 선택값을 입력하는지 확인
                    try:
                        selection = int(input("삭제하시겠습니까?\n"
                                              "1. 예\n"
                                              "2. 아니오\n"))
                    # 잘못된 선택값을 입력한 경우
                    except ValueError:
                        print("잘못 입력하셨습니다. 다시 입력하세요.")
                        continue
                    # 숫자값을 입력한 경우
                    else:
                        # 삭제하기로 선택한 경우
                        if selection == 1:
                            # 데이터 전송 모듈 중 Delete 클래스 호출
                            dt_del = dt.Delete()
                            # Delete 클래스에서 구분 삭제 메소드 호출
                            result = dt_del.group(group_name[0])
                            # 구분 삭제 메소드에서 반환받은 값이 0인 경우(Database 연결 정상 종료)
                            if result == 0:
                                # 삭제한 구분명을 반환
                                return group_name[0]
                        # 삭제하지 않기로 선택한 경우
                        elif selection == 2:
                            return 2
                        # 잘못된 숫자값을 입력한 경우
                        else:
                            print("잘못 입력하셨습니다. 다시 입력하세요.")
                            continue
        # 발견된 구분명이 없을 경우
        else:
            return -1
