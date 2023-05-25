import sys
import probability as prb
import matrices as matrix
available_categories=["Valószínűség","Mátrixok","Lineáris algebra"]
def main():
    for i,v in enumerate(available_categories, start=1):
        print(f"[{i}] : {v}")
    chosen_category = "2" # input("Add meg a feladat kategóriáját: ")
    try:
        if(chosen_category == "1"):
            prb.start_solve_probability_task()
        elif(chosen_category == "2"):
            matrix.start_slove_matrix_task()
    except ValueError as e:
        print(e,file=sys.stderr)
if __name__ == '__main__':
    main()