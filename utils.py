import sys
def colorise_text(color: str = "default"):
    colors = {"red": "\033[91m", "green": "\033[92m", "gold": "\033[93;1m"}
    return colors.get(color, "\033[0m")

def validated_input(popup:str, data_type:type):
    while True:
        try:
            user_input = data_type(input(popup))
            return user_input
        except ValueError:
            print(f"{colorise_text('red')}Hibás bemet! Próbáld újra!{colorise_text()}")
def validated_and_convert_input_list(popup:str,data_type:type):
    while True:
        try:
            user_input = input(popup).split()
            created_list = []
            for v in user_input:
                v = data_type(v)
                created_list.append(v)
            return user_input
        except ValueError:
            print(f"{colorise_text('red')}Hibás bemeneti lista. Próbáld újra!{colorise_text()}")

def get_next_character(character):
    if character == 'Z':
        return 'A'
    else:
        return chr(ord(character) + 1)

def get_task_index(popup:str, data_type:type,available_piece:int)->int:
    while True:
        choice = validated_input(popup, data_type)
        try:
            if(0 < choice <= available_piece):
                return choice- 1
            else:
                raise ValueError()
        except ValueError:
            print(f"{colorise_text('red')}Hibás feladat szám! Próbáld újra!{colorise_text()}")