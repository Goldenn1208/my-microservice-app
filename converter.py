mport json

def main():
    rates = {"USD": 92.5, "EUR": 100.2}
    
    print("--- Микросервис Конвертации v1.3 (Validation) ---")
    currency = input("Выберите валюту (USD или EUR): ").upper()
    
    if currency in rates:
        try:
            user_input = input(f"Введите сумму в {currency}: ")
            
            # ВАЛИДАЦИЯ (Issue #4)
            # 1. Проверяем, что введено число
            amount = float(user_input)
            
            # 2. Проверяем, что сумма не отрицательная
            if amount < 0:
                print(json.dumps({
                    "status": "error", 
                    "message": "Сумма не может быть отрицательной"
                }, indent=4, ensure_ascii=False))
                return

            result_rub = amount * rates[currency]
            
            response = {
                "status": "success",
                "data": {
                    "amount": amount,
                    "currency": currency,
                    "result_rub": round(result_rub, 2)
                }
            }
            print(json.dumps(response, indent=4, ensure_ascii=False))
            
        except ValueError:
            # Обработка случая, когда ввели буквы вместо цифр
            print(json.dumps({
                "status": "error", 
                "message": "Ошибка ввода: ожидалось число"
            }, indent=4, ensure_ascii=False))
    else:
        print(json.dumps({
            "status": "error", 
            "message": "Валюта не поддерживается"
        }, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    main()