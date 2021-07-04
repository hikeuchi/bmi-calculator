from dataclasses import dataclass


def _calculate_bmi(weight, height) -> float:
    return round(weight / (height ** 2))


def _get_bmi_result(bmi: float) -> str:
    if bmi < 18.5:
        result = "痩せ型"
    elif (bmi >= 18.5) and (bmi < 25):
        result = "標準体型"
    elif (bmi >= 25) and (bmi < 30):
        result = "肥満(軽)"
    else:
        result = "肥満(重)"
    
    return result


@dataclass
class Person():
    weight: float  # 体重(kg)
    height: float  # 身長（m）

    @classmethod
    def create(cls, weight: float, height: float) -> 'Person':
        height_meter = float(height) / 100
        return Person(
            weight=weight,
            height=height_meter
        )

    @property
    def bmi(self) -> float:
        return _calculate_bmi(weight=self.weight, height=self.height)

    def print_bmi_result(self) -> None:
        print("BMI: " + str(self.bmi))
        print("判定: " + _get_bmi_result(self.bmi))


def main():
    person = Person.create(weight=50, height=160)
    person.print_bmi_result()


if __name__ == "__main__":
    main()
