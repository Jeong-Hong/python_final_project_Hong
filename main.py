from models.specialized_books import PaperBook, EBook
from models.base_book import AlreadyRentedError, AlreadyReturnError
from utils.helpers import get_valid_input, get_int_input

books = {}  # 개별 도서 상세정보 관리
registered_isbns = set()    # set[집합]을 사용하여 중복 등록 방지
while True:
    print(
        f"{'-'*20}\n"
        "1. 도서등록\n"
        "2. 전체 도서 조회\n"
        "3. 도서 검색\n"
        "4. 대여/반납 처리\n"
        "5. 종료\n"
        f"{'-'*20}"
    )

    user_input = get_int_input("메뉴를 선택하세요 : ")

    if user_input == 5:
        break
    elif user_input == 1:
        name = get_valid_input("책 이름을 입력하세요 : ")
        writer = get_valid_input("저자를 입력하세요 : ")
        ISBN = get_valid_input("ISBN을 입력하세요 : ")

        if ISBN in registered_isbns:
            print("이미 등록된 ISBN 입니다.")
            continue
        
        book_type = get_int_input("종류를 선택하세요 : 1.단행본 / 2. E북 : ")

        if book_type == 1:
            pages = get_int_input("총 페이지를 입력하세요 : ")
            book = PaperBook(name,writer,ISBN,pages)
        
        elif book_type == 2:
            source = get_int_input("총 용량을 입력하세요 : ")
            book = EBook(name,writer,ISBN,source)
        else:
            print("1번 또는 2번만 선택 가능합니다.\n")
            continue

        books[ISBN] = book
        registered_isbns.add(ISBN)

    elif user_input == 2:
        if not books:
            print("등록된 책이 없습니다.")
            continue
        for value in books.values():
            print(value)

    elif user_input == 3:
        input_ISBN = get_valid_input("ISBN을 입력하세요 :")
        if input_ISBN in books:
            print(books[input_ISBN])
        else:
            print("등록되지 않은 책입니다.")
        
    elif user_input == 4:
        input_ISBN = get_valid_input("ISBN을 입력하세요 :")
        if input_ISBN not in books:
            print("등록되지 않은 책입니다.")
            continue

        book = books[input_ISBN]

        if book.get_status():
            confirm = get_valid_input("대여 가능한 도서입니다. 대여하시겠습니까? (y/n) : ").strip()
            if confirm in ['y','yes','예']:
                try:
                    book.rent()
                    print("대여처리 되었습니다")
                except AlreadyRentedError as e:
                    print(f"[대여 실패] {e}\n")
            else:
                print("대여가 취소되었습니다.\n")      
        
        else:
            confirm = get_valid_input("현재 대여 중인 도서입니다. 반납하시겠습니까? (y/n) : ").strip()
            if confirm in ['y','yes','예']:
                try:
                    book.return_book()
                    print(f"'{book.name}'이(가) 반납 처리되었습니다.\n")
                except AlreadyReturnError as e:
                    print(f"[반납 실패] {e}\n")
            else:
                print("반납이 취소되었습니다.\n")
            
    else:
        print("메뉴에 없는 번호 입니다.\n")