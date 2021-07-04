from person import Person


def main():
    # UIから入力する体での変数定義
    weight = 50  # 体重
    height = 160  # 身長(cm)

    person = Person(weight=weight, height_cm=height)
    person.print_bmi_result()


if __name__ == "__main__":
    main()