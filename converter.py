def main():
    # Курсы валют для задачи №2
    rates = {"USD": 92.5, "EUR": 100.2}

    print("--- Конвертер Валют v1.1 ---")
    currency = input("Выберите валюту (USD или EUR): ").upper()

    if currency in rates:
        try:
            amount = float(input(f"Введите сумму в {currency}: "))
            result = amount * rates[currency]
            print(f"Итог: {amount} {currency} = {result:.2f} RUB")
        except ValueError:
            print("Ошибка: введите число!")
    else:
        print("Ошибка: Данная валюта не поддерживается.")

if name == "main":
    main()