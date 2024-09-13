import requests

# API ключ и ID вашей поисковой системы (cx)
api_key = ''
cse_id = ''

# Функция для поиска
def google_search(query, num_results=100, start=1):
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': query,
        'num': min(num_results, 10),  # Максимум 10 результатов за запрос
        'start': start
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

# Пример использования
query = 'факты'
all_results = []
start_index = 1
max_results = 100  # Ограничиваем максимальное количество результатов

# Открываем файл для записи
with open('site.txt', 'w', encoding='utf-8') as file:
    while start_index <= max_results:  # Запрашиваем только до 100 результатов
        data = google_search(query, num_results=100, start=start_index)
        results = data.get('items', [])
        all_results.extend(results)
        
        if len(results) == 0:  # Если больше нет результатов
            break
        
        start_index += 10

    # Записываем результаты в файл
    for i, result in enumerate(all_results, start=1):
        file.write(f"{i}. {result['link']}\n")
