from fractions import Fraction
import sys
available_types=["Szórás/eloszlás"]

fos = {
    "-1":"2/5",
    "-2":"1/5",
    "1":"2/5"
}
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
            raw_input_dict[ipt] = input(f"Add meg {ipt} esélyét(ha tört /-rel válaszd el): ")
            print("Add meg a következő számot(vagy hagyd üresen és enter): ",end="")
        results = {
             "E_simple": self.get_E(raw_input_dict),
             "E_powered": self.get_Epow(raw_input_dict),
             "D_": self.get_D(raw_input_dict)
        }
        if not self.check_rule(raw_input_dict):
            print("A valószínűségeg összege nem 1!", file=sys.stderr)
        print(
            f"A megadott feladathoz az eloszlás: E(x)= {results['E_simple']}\nA szórás pedig: D(x)= {results['D_']}\n")
        print(
            f"Tört alakok az alábbiak:\nE(x)= {self.get_fraction(results['E_simple'])}\nE2(x)= {self.get_fraction(results['E_powered'])}\nD(x)= {self.get_fraction(results['D_'])}")


def main():
    for i,v in enumerate(available_types, start=1):
        print(f"[{i}] : {v}")
    chosen_type = input("Add meg milyen tipusú a feladat: ")
    try:
        if(chosen_type == "1"):
            dis().main()
        else:
            raise ValueError("Nincs ilyen típus!")
    except ValueError as e:
        print(e, file=sys.stderr)
if __name__ == '__main__':
    main()