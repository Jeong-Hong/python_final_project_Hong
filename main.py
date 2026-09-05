from models.specialized_books import PaperBook, EBook
from models.base_book import Book

books = {}  # 개별 도서 상세정보 관리
registered_isbns = set()    # 중복 등록 방지용 ISBN 목록

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

    try:
        user_input = int(input("메뉴를 선택하세요 : "))

    except ValueError:
        print("숫자만 입력하세요\n")
        continue

    if user_input == 5:
        break
    elif user_input == 1:
        name = input("책 이름을 입력하세요 : ")
        writer = input("저자를 입력하세요 : ")
        ISBN = input("ISBN을 입력하세요 : ")
        if not ISBN.strip():
            print("ISBN을 입력하세요 : ")
            continue
        if ISBN in registered_isbns:
            print("이미 등록된 ISBN 입니다.")
            continue
        try:
            book_type = int(input("종류를 선택하세요 : 1.단행본 / 2. E북"))
        except ValueError:
            print("숫자만 입력하세요 : ")
            continue
        if book_type == 1:
            pages = input("총 페이지를 입력하세요 : ")
            book = PaperBook(name,writer,ISBN,pages)
        else:
            source = input("총 용량을 입력하세요 : ")
            book = EBook(name,writer,ISBN,source)

        books[ISBN] = book
        registered_isbns.add(ISBN)

    elif user_input == 2:
        if not books:
            print("등록된 책이 없습니다.")
            continue
        for value in books.values():
            print(value)

    elif user_input == 3:
        input_ISBN = input("ISBN을 입력하세요 :")
        if input_ISBN in books:
            print(books[input_ISBN])
        else:
            print("등록되지 않은 책입니다.")
        
    elif user_input == 4:
        input_ISBN = input("ISBN을 입력하세요 :")
        if input_ISBN not in books:
            print("등록되지 않은 책입니다.")
            continue

        book = books[input_ISBN]

        if book.get_status():
            confirm = input("대여 가능한 도서입니다. 대여하시겠습니까? (y/n) : ").strip()
            if confirm in ['y','yes','예']:
                book.rent()
                print("대여처리 되었습니다")
            else:
                print("대여가 취소되었습니다.\n")      
        
        else:
            confirm = input("현재 대여 중인 도서입니다. 반납하시겠습니까? (y/n) : ").strip()
            if confirm in ['y','yes','예']:
                book.return_book()
                print(f"'{book.name}'이(가) 반납 처리되었습니다.\n")            
            else:
                print("반납이 취소되었습니다.\n")
            
    else:
        print("메뉴에 없는 번호 입니다.\n")