if __name__ == "__main__":
    while True:
        try:
            number = int(input("\nВведите число: "))
        except ValueError as e: 
            print("\nНекорректный ввод.")
        else:
            ending = ""
            last_digit = number % 10
            if last_digit in [0, 2, 3, 4]: ending = "а"
            elif 5 <= last_digit : ending = "ов"
            print(f"{number} компьютер{ending}")