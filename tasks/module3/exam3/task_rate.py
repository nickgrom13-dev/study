from datetime import datetime
import requests

def get_exchange_rates() -> dict|None:
    """ Функция для получения и обработки данных о курсах валют """

    # Адрес веб-сервиса с курсами валют
    url = "https://www.cbr-xml-daily.ru/daily_json.js"

    try:
        # Получаем данные из веб-сервиса
        response = requests.get(url)

        # Преобразуем данные ответа в формат JSON
        exchange_data = response.json()

        # Получим дату курса
        date_rate = exchange_data['Date']

        # Получаем курсы валют (доллара и евро)
        usd_rate = exchange_data['Valute']['USD']['Value']
        eur_rate = exchange_data['Valute']['EUR']['Value']

        # Рассчитаем разницу между долларом и евро
        difference = usd_rate / eur_rate

        return {
            'date_rate': date_rate,
            'usd_rate': usd_rate,
            'eur_rate': eur_rate,
            'difference': difference
        }

    except Exception as e:
        print(f"Ошибка выполнения/обработки запроса: {e}")

def main():
    result = get_exchange_rates()
    if result:
        print("=" * 50)
        print("КУРСЫ ВАЛЮТ ЦЕНТРАЛЬНОГО БАНКА РОССИИ")
        print("=" * 50)
        # Преобразование даты из JSON
        parsed_date = datetime.fromisoformat(result['date_rate'])
        print(f"Дата курса: {parsed_date.strftime('%d.%m.%Y %H:%M:%S')}")
        print(f"Курс доллара (USD): {result['usd_rate']} RUB")
        print(f"Курс евро (EUR): {result['eur_rate']} RUB")
        print("-" * 50)
        print("РАСЧЕТ РАЗНИЦЫ МЕЖДУ КУРСАМИ:")
        compare = 'больше' if result['difference'] > 1 else 'меньше'
        print(f"Курс доллара (USD) {compare} курса евро (EUR) в {result['difference']:.4f} раз")

if __name__ == "__main__":
    main()
