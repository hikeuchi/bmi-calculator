class User():

    def __init__(self, weight, height_cm):
        self.weight = weight
        height_m = float(height_cm) / 100
        self.height = height_m

    def print_bmi_result(self):
        print(f'BMI: {self._calculate_bmi()}')
        print(f'判定: {self._get_bmi_result()}')
        print(f'適正体重: {self._calculate_recommended_weight()}')

    def _calculate_bmi(self):
        return round(self.weight / (self.height ** 2), 1)  # 小数点以下1位で丸める

    def _get_bmi_result(self):
        bmi = self._calculate_bmi()
        if bmi < 18.5:
            result = "痩せ型"
        elif (bmi >= 18.5) and (bmi < 25):
            result = "標準体型"
        elif (bmi >= 25) and (bmi < 30):
            result = "肥満(軽)"
        else:
            result = "肥満(重)"
        
        return result

    def _calculate_recommended_weight(self):
        recommended_weight = (self.height ** 2) * 22
        recommended_weight = round(recommended_weight, 1)  # 小数点以下1位で丸める

        return recommended_weight


def main():
    pass


if __name__ == "__main__":
    main()
