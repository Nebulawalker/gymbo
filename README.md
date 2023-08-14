# Тестовый проект
Тестовое задание для демонстрация навыков работы с Django, DRF, Postgres.

## Реализованные API
1. /api/v1/pages - выводятся название блока и ссылка на страницу. Блоки не выводятся, выводится только название и ссылка на страницу.
2. /api/v1/page/<slug:slug> - На странице выводятся блоки и счетчики показа блоков.


## Для запонения базы данных тестовыми данными
```sh
python manage.py loaddata --app pages dump.json
```