import json

def main():
    # Курсы валют для задачи №2 и №3
    rates = {"USD": 92.5, "EUR": 100.2}
    
    print("--- Микросервис Конвертации v1.2 (JSON) ---")
    currency = input("Выберите валюту (USD или EUR): ").upper()
    
    if currency in rates:
        try:
            amount_str = input(f"Введите сумму в {currency}: ")
            amount = float(amount_str)
            result_rub = amount * rates[currency]
            
            # Формируем JSON (Требование Issue #3)
            response = {
                "status": "success",
                "data": {
                    "from": currency,
                    "to": "RUB",
                    "amount": amount,
                    "result": round(result_rub, 2)
                }
            }
            print(json.dumps(response, indent=4, ensure_ascii=False))
            
        except ValueError:
            error_msg = {"status": "error", "message": "Нужно ввести число"}
            print(json.dumps(error_msg, indent=4, ensure_ascii=False))
    else:
        error_msg = {"status": "error", "message": "Валюта не поддерживается"}
        print(json.dumps(error_msg, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()