class AlreadyRentedError(Exception):
    pass

class AlreadyReturnError(Exception):
    pass

class Book:
    def __init__(self,name,writer,isbn,status=True):
        self.name = name
        self.writer = writer
        self.__isbn = isbn
        self.__status = status

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def rent(self):
        if self.__status == True:
            self.__status = False
        else:
            raise AlreadyRentedError("이미 대여중 입니다.")

    def return_book(self):
        if self.__status == False:
            self.__status = True
        else:
            raise AlreadyReturnError("이미 반납 되었습니다.")

    def __str__(self):
        return f"이름: {self.name}, 저자: {self.writer}, ISBN: {self.__isbn}, 상태: {self.__status}"