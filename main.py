# main.py

# 메뉴 조작 모듈 import
import menu_controller as menu


# 메인 메뉴 함수
def main():
    # 메인 메뉴 텍스트
    menu_text = ("===============================\n"
                 "      연락처 관리 프로그램\n"
                 "===============================\n"
                 "1. 연락처 추가\n"
                 "2. 연락처 목록 보기\n"
                 "3. 연락처 정보 수정\n"
                 "4. 연락처 삭제\n"
                 "5. 구분 추가\n"
                 "6. 구분 목록 보기\n"
                 "7. 구분 수정\n"
                 "8. 구분 삭제\n"
                 "9. 종료")
    # 메인 메뉴 텍스트 출력
    print(menu_text)
    # 메뉴 선택
    while True:
        try:
            # 메뉴 선택값 받기
            selection = int(input("위 메뉴 중 하나를 선택하세요: "))
        # 숫자가 아닌 값을 입력했을 경우 예외 처리
        except ValueError:
            print("잘못 입력하였습니다. 다시 입력하세요.")
            continue
        # 연락처 추가
        if selection == 1:
            print("\n새 연락처를 추가합니다.")
            # 연락처 추가 기능 컨트롤러 호출
            # 해당 기능 실행 후 결과가 반환됨
            result = menu.add_contact()
            # 연락처 추가 기능에서 0을 반환한 경우
            if result == 0:
                print("오류가 발생하였습니다. 메인 메뉴로 돌아갑니다.")
                print()
                main()
            # 정상적으로 추가된 경우
            else:
                # 반환된 딕셔너리에서 입력한 연락처 각 항목 대입
                new_contact_name = result["contact_name"]
                new_contact_phone = result["phone"]
                new_contact_email = result["email"]
                new_contact_group = result["group_name"]
                # 결과 출력 후 메인 메뉴 복귀
                print()
                print("아래와 같이 새 연락처를 추가하였습니다.")
                print("이름:", new_contact_name)
                print("전화번호:", new_contact_phone)
                print("이메일 주소:", new_contact_email)
                print("구분:", new_contact_group)
                print()
                main()
        # 연락처 목록 보기
        elif selection == 2:
            print("\n현재 등록된 연락처 목록입니다.")
            # 연락처 목록 컨트롤러 호출
            contacts_list = menu.list_contacts()
            # 반환된 딕셔너리에서 각 항목 대입
            contact_name_list = contacts_list["contact_name"]
            phone_list = contacts_list["phone"]
            email_list = contacts_list["email"]
            group_name_list = contacts_list["group_name"]
            # 중복되지 않는 값을 이용하여 연락처 개수 확인
            contacts_length = len(phone_list)
            # 연락처 개수 출력
            print(f"총 {contacts_length}개의 연락처가 등록되어 있습니다.")
            # 연락처 목록 출력
            list_number = 1
            i = 0
            for _ in phone_list:
                print(list_number, end=".\n")
                print("이름:", contact_name_list[i])
                print("전화번호:", phone_list[i])
                print("이메일 주소:", email_list[i])
                print("구분:", group_name_list[i])
                print()
                list_number += 1
                i += 1
            # 메인 메뉴 복귀
            main()
        # 연락처 정보 수정
        elif selection == 3:
            print("연락처를 수정합니다.")
            # 연락처 수정 컨트롤러 호출, 처리 후 결과값 대입
            result = menu.modify_contact()
            # -1을 반환한 경우 (연락처 없음)
            if result == -1:
                print("입력한 이름으로 검색된 연락처가 없습니다. 메인 메뉴로 돌아갑니다.")
            # 2를 반환한 경우 (연락처 수정하지 않음)
            elif result == 2:
                print("수정하지 않기로 선택하였습니다. 메인 메뉴로 돌아갑니다.")
            # 연락처를 수정한 경우
            # 이름을 수정한 경우
            elif "new_contact_name" in result.keys():
                # 반환받은 딕셔너리에서 대상 연락처 이름, 전화번호, 변경된 이름 대입
                contact_name = result["contact_name"]
                phone = result["phone"]
                new_contact_name = result["new_contact_name"]
                # 결과 출력
                print(f"{contact_name}({phone})의 이름을 {new_contact_name}(으)로 수정하였습니다.")
            # 전화번호를 수정한 경우
            elif "new_phone" in result.keys():
                # 반환받은 딕셔너리에서 대상 연락처 이름, 전화번호, 변경된 전화번호 대입
                contact_name = result["contact_name"]
                phone = result["phone"]
                new_phone = result["new_phone"]
                # 결과 출력
                print(f"{contact_name}({phone})의 전화번호를 {new_phone}(으)로 수정하였습니다.")
            # 이메일을 수정한 경우
            elif "new_email" in result.keys():
                # 반환받은 딕셔너리에서 대상 연락처 이름, 전화번호, 변경된 이메일 주소 대입
                contact_name = result["contact_name"]
                phone = result["phone"]
                new_email = result["new_email"]
                # 결과 출력
                print(f"{contact_name}({phone})의 이메일 주소를 {new_email}(으)로 수정하였습니다.")
            # 구분을 수정한 경우
            elif "new_group_name" in result.keys():
                # 반환받은 딕셔너리에서 대상 연락처 이름, 전화번호, 변경된 구분명 대입
                contact_name = result["contact_name"]
                phone = result["phone"]
                new_group_name = result["new_group_name"]
                # 결과 출력
                print(f"{contact_name}({phone})의 구분을 {new_group_name}(으)로 수정하였습니다.")
            print()
            # 메인 메뉴 복귀
            main()
        # 연락처 삭제
        elif selection == 4:
            print("연락처를 삭제합니다.")
            # 연락처 삭제 컨트롤러 호출, 처리 후 결과값 대입
            result = menu.delete_contact()
            # -1을 반환받은 경우
            if result == -1:
                # 해당 연락처 없음
                print("입력하신 검색어로 연락처를 찾을 수 없었습니다. 메인 메뉴로 복귀합니다.")
            # 2를 반환받은 경우
            elif result == 2:
                # 삭제하지 않기로 선택함
                print("삭제하지 않기로 하였습니다. 메인 메뉴로 돌아갑니다.")
            # 삭제한 경우
            else:
                # 반환받은 딕셔너리에서 삭제된 연락처의 이름과 전화번호 대입
                contact_name = result["contact_name"]
                phone = result["phone"]
                # 결과 출력
                print(f"{contact_name}({phone})의 연락처를 삭제하였습니다.")
            print()
            # 메인 메뉴 복귀
            main()
        # 구분 추가
        elif selection == 5:
            print("\n구분을 추가합니다.")
            # 구분 변경 컨트롤러 호출
            result = menu.add_group()
            group_name = result["group_name"]
            # 성공적으로 처리된 경우
            if group_name:
                print(f"구분 '{group_name}'을/를 추가하였습니다.")
                print()
            else:
                print("오류가 발생하여 추가되지 않았습니다. 메인 메뉴로 복귀합니다.")
            print()
            main()
        # 구분 목록 보기
        elif selection == 6:
            # 구분 목록 출력 컨트롤러 호출, 처리 후 결과값 대입
            groups_list = menu.list_groups()
            # 반환받은 딕셔너리에서 구분명만 대입
            group_name_list = groups_list["group_name"]
            # 구분명 길이 확인 후 구분 개수 출력
            groups_list_length = len(group_name_list)
            print(f"총 {groups_list_length}개의 구분이 등록되어 있습니다.")
            # 구분명 순차 출력
            list_number = 1
            for group_name in group_name_list:
                print(list_number, end=". ")
                print(group_name)
                list_number += 1
            print()
            # 메인 메뉴 복귀
            main()
        # 구분 수정
        elif selection == 7:
            print("\n구분을 수정합니다.")
            # 구분명 수정 컨트롤러 호출, 처리 후 결과값 대입
            result = menu.modify_group()
            # -1을 받환받은 경우 (해당 구분명 없음)
            if result == -1:
                print("입력한 검색어로 구분명을 찾을 수 없었습니다. 메인 메뉴로 돌아갑니다.")
            # 0을 반환받은 경우 (구분명 수정 안 함)
            elif result == 0:
                print("구분명을 수정하지 않았습니다. 메인 메뉴로 돌아갑니다.")
            # 구분명이 수정된 경우
            else:
                # 반환받은 딕셔너리에서 이전 구분명, 변경한 구분명 대입
                old_group_name = result["old_group_name"]
                new_group_name = result["new_group_name"]
                # 결과 출력
                print(f"구분명 '{old_group_name}'을/를 '{new_group_name}(으)로 수정하였습니다.")
            print()
            # 메인 메뉴 복귀
            main()
        # 구분 삭제
        elif selection == 8:
            print("\n구분을 삭제합니다.")
            # 구분 삭제 컨트롤러 호출
            result = menu.delete_group()
            # 0을 받환받은 경우 (사용중인 구분명)
            if result == 0:
                print("이 구분은 현재 사용중입니다. 삭제할 수 없습니다. 메인 메뉴로 복귀합니다.")
            # 2를 반환받은 경우 (삭제하지 않기로 선택)
            elif result == 2:
                print("구분을 삭제하지 않았습니다.")
            # -1을 반환받은 경우 (해당 구분명 없음)
            elif result == -1:
                print("입력하신 검색어의 구분명을 찾을 수 없었습니다. 메인 메뉴로 돌아갑니다.")
            else:
                print(f"구분명 '{result}'을/를 삭제하였습니다.")
            print()
            # 메인 메뉴 복귀
            main()
        # 프로그램 종료
        elif selection == 9:
            print("\n프로그램을 종료합니다.")
            exit()
        # 메뉴에 없는 숫자값을 입력한 경우
        else:
            print("잘못 입력하였습니다. 다시 입력하세요.")
            continue


# 메인 메뉴 실행
main()
