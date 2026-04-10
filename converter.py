def main():
    print("--- Микросервис Конвертации (v1.0) ---")
    try:
        # Принимаем запрос (сумму)
        usd_amount = float(input("Введите сумму в USD для конвертации: "))
        
        # Проводим работу (логика конвертации)
        exchange_rate = 92.5
        rub_result = usd_amount * exchange_rate
        
        # Возвращаем ответ
        print(f"Результат: {usd_amount} USD = {rub_result:.2f} RUB")
    except ValueError:
        print("Ошибка: Пожалуйста, введите числовое значение.")

if __name__ == "__main__":
    main()