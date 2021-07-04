from dataclasses import dataclass


@dataclass
class Person():
    weight: int  # 体重(kg)
    height: float  # 身長（m）
    
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2))

    def print_bmi(self) -> None:
        bmi = round(self.weight / (self.height ** 2))
        if bmi < 18.5:
            result = "痩せ型"
        elif (bmi >= 18.5) and (bmi < 25):
            result = "標準体型"
        elif (bmi >= 25) and (bmi < 30):
            result = "肥満(軽)"
        else:
            result = "肥満(重)"
        print("BMI: " + str(bmi))
        print("判定: " + result)


def main():
    person = Person(weight=50, height=165)
    person.print_bmi()    


if __name__ == "__main__":
    main()