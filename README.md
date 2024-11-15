# cian_parsing
В приведенном коде используется библиотека cianparser для парсинга данных с сайта Cian.ru, платформы для поиска недвижимости. Вот разбор работы этого кода:

Импорт библиотеки:

```python
import cianparser
```
Здесь импортируется модуль cianparser, который содержит необходимые классы и функции для взаимодействия с сайтом Cian.ru.

Создание экземпляра парсера:

```python

moscow_parser = cianparser.CianParser(location='Москва')
```
Создается объект moscow_parser класса CianParser, который будет использоваться для парсинга информации о недвижимости в Москве. Параметр location='Москва' указывает на то, что парсер будет искать квартиры именно в Москве.

Получение данных:

```python
data = moscow_parser.get_flats(deal_type='rent_long', rooms=(1, 2, 'studio'), with_saving_csv=True, additional_settings={"start_page": 1, "end_page": 5})
```
В этой строке вызывается метод get_flats для получения информации о квартирах по следующим параметрам:
```python
deal_type='rent_long': указывает, что нужно искать квартиры для длительной аренды.
rooms=(1, 2, 'studio'): фильтруются квартиры с 1 и 2 комнатами, а также студии.
with_saving_csv=True: параметр, который заставляет парсер сохранять результаты в CSV файл (это может быть полезно для дальнейшей обработки или анализа).
additional_settings={"start_page": 1, "end_page": 5}: дополнительные параметры, которые указывают, что нужно парсить страницы с 1 по 5 включительно.
```
Вывод данных:

```python
Копировать код
print(data)
```
После выполнения парсинга результат сохраняется в переменную data и выводится на экран. Это может быть как сам список найденных объектов недвижимости, так и данные, полученные в формате CSV, в зависимости от настроек.
