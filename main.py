from fractions import Fraction
import sys
available_types=["Szórás/eloszlás","Kiválasztás"]
class basicMath:
    def factorial(n:int)->int:
        if n<0: return -1
        if n == 0: return 1
        return n * basicMath.factorial(n-1)
    def NCR(n:int,r:int):
        return int(basicMath.factorial(n) /  ( basicMath.factorial(r) * basicMath.factorial( (n - r) ) ))

class dis:
    def get_E(self,input_dict: dict) -> float:
        input_dict = self.process_fraction(input_dict)
        E_ = 0.0
        for k, v in input_dict.items():
            E_ += int(k) * float(v)
        return (E_)

    def get_Epow(self,input_dict: dict) -> float:
        input_dict = self.process_fraction(input_dict)
        E_pow = 0.0
        for k, v in input_dict.items():
            E_pow += (int(k) ** 2) * float(v)

        return E_pow

    def get_D(self,input_dict: dict) -> float:
        E_ = self.get_E(input_dict) ** 2
        E_pow = self.get_Epow(input_dict)
        return ((E_pow - E_) ** 0.5)

    def get_fraction(self,input_number: float) -> str:
        return str(Fraction(str(input_number)).limit_denominator(1000))

    def process_fraction(self,input_dict: dict) -> dict:
        return_dict = {}
        for k, v in input_dict.items():
            if ("/" in v):
                hold = v.split("/")
                return_dict[k] = int(hold[0]) / int(hold[1])
            else:
                return_dict[k] = v
        return return_dict
    def check_rule(self,input_dict:dict) ->bool:
        input_dict = self.process_fraction(input_dict)
        return sum(input_dict.values()) == 1
    def main(self):
        raw_input_dict = {}
        print("Add meg az első számot: ", end="")
        while (ipt := input()) != "":
            raw_input_dict[ipt] = input(f"\033[92m\tAdd meg \033[31m{ipt}\033[92m esélyét(ha tört /-rel válaszd el): \033[0m")
            print("Add meg a következő számot(vagy hagyd üresen és enter): ",end="")
        results = {
             "E_simple": self.get_E(raw_input_dict),
             "E_powered": self.get_Epow(raw_input_dict),
             "D_": self.get_D(raw_input_dict)
        }
        if not self.check_rule(raw_input_dict):
            print("A valószínűségeg összege nem 1!", file=sys.stderr)
        print(
            f"\033[33mA megadott feladathoz az eloszlás: E(x)= \033[92m{results['E_simple']}\033[33m\nA szórás pedig: D(x)= \033[92m{results['D_']}\n\033[0m")
        print(
            f"\033[33mTört alakok az alábbiak:\nE(x)= \033[92m{self.get_fraction(results['E_simple'])}\033[33m\nE2(x)= \033[92m{self.get_fraction(results['E_powered'])}\033[33m\nD(x)= \033[92m{self.get_fraction(results['D_'])}\033[0m")

class select:
    def probability(self,basket:dict,selected:int,positive:int,who:str,type:int)->int:
        all_count = sum(basket.values())
        all_prob = basicMath.NCR(all_count,selected)
        lst = list(basket.items())
        lst.sort(key=lambda x: x[0] == who, reverse=True)
        if(type == 1): #pontosan
            return (basicMath.NCR(lst[0][1],positive) * basicMath.NCR(lst[1][1],selected-positive)) / all_prob
        elif(type == 2):#legfeljebb
            num = 0
            for i in range(positive+1):
                num += basicMath.NCR(lst[0][1],i) * basicMath.NCR(lst[1][1],selected-i)
            return num/all_prob
        elif(type == 3):#legalább
            num = 0
            for i in range(positive,selected+1):
                num += basicMath.NCR(lst[0][1],i) * basicMath.NCR(lst[1][1],selected-i)
            return num/all_prob
    def main(self):
        # kosarak bekérése miböl lehet választani x fió x lány stb
        # mi kell teljesuljon? X,Y
        # legfeljebb,pontosan legalább
        input_basket = {}
        print("Add meg az első kosarár nevét(pl fiú/lány/piros stb): ", end="")
        for i in range(2):
            ipt = input()
            input_basket[ipt] = int(input(f"\033[92m\tAdd meg \033[31m{ipt}\033[92m darabszámát: \033[0m"))
            if i != 1:
                print("Add meg a következő kosarat: ", end="")
        selected_count = int(input("Összesen hányat választunk ki: "))
        type = int(input("Pontosan[1] / Legfeljebb[2] / Legalább[3]: "))
        positive = int(input("Mennyi a kedvező érték? (hány x-et kell kiválasztani): "))
        for v in input_basket.keys():
            print(f"\033[91m[{v}]\033[0m")
        who = input(f"Kit választunk ki? (nevet ird be):")
        print(f"\033[33mA megadott feladat valószínűsége kerekítve: \033[92m{round(self.probability(input_basket, selected_count, positive, who, type),3)}\033[0m")

def main():
    for i,v in enumerate(available_types, start=1):
        print(f"[{i}] : {v}")
    chosen_type = input("Add meg milyen tipusú a feladat: ")
    try:
        if(chosen_type == "1"):
            dis().main()
        elif(chosen_type == "2"):
            select().main()
        else:
            raise ValueError("Nincs ilyen típus!")
    except ValueError as e:
        print(e, file=sys.stderr)
if __name__ == '__main__':
    main()