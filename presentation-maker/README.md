# Presentation Maker

Генератор корпоративных PPTX-презентаций из любого источника (ссылка, PDF, текст).

## Что делает
- Извлекает контент из URL или PDF
- Строит JSON-структуру презентации
- Генерирует PPTX в фирменном стиле (teal #127A8D + orange #F07C1D)
- Отправляет файл в Telegram

## Tech stack
- Python 3.12
- python-pptx (генерация PPTX)
- Hermes MCP (интеграция с ботом)
- pdftotext (извлечение из PDF)

## Установка

bash
pip install python-pptx
apt install -y poppler-utils


## Использование

bash
python3 make_pptx.py input.json output.pptx


## Слайды
- `title` — титульный слайд с градиентом
- `bullets` — список пунктов
- `stats` — крупные KPI-числа
- `bento` — карточки с мини-контентом
- `table` — таблицы
- `image` — фото на весь слайд
- `section` — разделитель секций
- `chart` — matplotlib-графики

## Интеграция
Работает как Hermes-skill: бот принимает ссылку/PDF и возвращает PPTX.
