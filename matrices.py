import utils


class matrix_creation():
    def input_matrix_row(popup: str, cols: int) -> bool:
        while True:
            try:
                matrix_row = utils.validated_and_convert_input_list(popup, int)
                if (len(matrix_row) == cols):
                    return matrix_row
                else:
                    operation = "Több" if len(matrix_row) > cols else "Kevesebb"
                    raise ValueError()
            except ValueError:
                print(f"A megadott sor {operation} oszlopot tartalmaz.")
        # return True if len(matrix) == cols else False

    def create_new_matrix(name: str):
        matrix = []
        rows = utils.validated_input(f"Add meg [{name}] mátrix sorainak számát: ", int)
        cols = utils.validated_input(f"Add meg [{name}] mátrix oszlopainak számát: ", int)
        for i in range(rows):
            matrix.append(matrix_creation.input_matrix_row(f"Add meg [{name}] mátrix {i + 1}. sorát: ", cols))
        return matrix

class matrix_utils():
    def get_which_to_slove_single(popup,matrixes):
        if(len(matrixes) == 1):
            return next(iter(matrixes))
        while True:
            try:
                user_input = input(popup)
                if(user_input == "-"):
                    return -1
                elif(user_input in matrixes):
                    return user_input
                else:
                    raise ValueError()
            except ValueError:
                print(f"{utils.colorise_text('red')}Nincs ilyen mátrix. Próbáld meg újra!{utils.colorise_text()}")
class matrix_solution():
    def transposition(matrixes: dict, chosen_matrix_char) -> dict:
        if chosen_matrix_char == -1:
            for k, matrix in matrixes.items():
                matrixes[k] = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
            return matrixes
        else:
            matrix = matrixes[chosen_matrix_char]
            matrixes[chosen_matrix_char] = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
            return matrixes

    def gauss_elimination(matrix:list[list])->list[list]:
        rows = len(matrix)

        # Forward elimination
        for i in range(rows - 1):
            print(matrix[i][i])
            if matrix[i][i] == 0:
                for j in range(i + 1, rows):
                    if matrix[j][i] != 0:
                        matrix[i], matrix[j] = matrix[j], matrix[i]
                        break
            if matrix[i][i] == 0:
                return None
            for j in range(i + 1, rows):
                factor = matrix[j][i] / matrix[i][i]
                for k in range(i, rows):
                    matrix[j][k] -= factor * matrix[i][k]

        return matrix
def start_slove_matrix_task():
    matrixes = {}
    current_matrix_name = 'Z'
    for _ in range(utils.validated_input("Add meg hány mátrixot szeretnél létrehozni: ", int)):
        current_matrix_name = utils.get_next_character(current_matrix_name)
        matrixes[current_matrix_name] = matrix_creation.create_new_matrix(current_matrix_name)
        print()
    matrix_operations = ["Transponálás","Skalár szorzás","Mátrix szorzás","Determinás"]
    for i,v in enumerate(matrix_operations, start=1):
        print(f"[{i}] : {v}")
    chosen_type = utils.get_task_index("Add meg milyen tipusú a feladat: ",int,len(matrix_operations))
    tasks = {
        0: matrix_solution.transposition
    }
    matrix_keys = ""
    for v in matrixes.keys():
        matrix_keys += v+", "
    print(tasks[chosen_type](matrixes,matrix_utils.get_which_to_slove_single(f"Add meg melyik mátrixot szeretnéd transzponálni! \n\t[{matrix_keys}-]Betű vagy - ha az összeset: ",matrixes)))