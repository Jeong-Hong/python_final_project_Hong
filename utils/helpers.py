def get_valid_input(prompt: str)-> str:
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("공백은 입력할 수 없습니다. 다시 입력해주세요.")

def get_int_input(prompt: str)-> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("숫자만 입력 가능합니다. 다시 입력해주세요.")