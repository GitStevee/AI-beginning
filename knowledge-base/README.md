# Knowledge Base (Agentic RAG)

Self-hosted RAG: Telegram-бот ищет по загруженным документам
и отвечает со ссылками на источники.

## Архитектура

Telegram -> Hermes (DeepSeek) -> skill knowledge-base
        -> Open Notebook API -> SurrealDB (vector search)
        -> LLM собирает ответ с цитатами

## Компоненты
- Open Notebook - self-hosted аналог NotebookLM (docker)
- SurrealDB - векторная БД (хранит embeddings чанков)
- qwen3-embedding-8b - модель эмбеддингов (текст -> вектор)
- Hermes skill - интеграция с Telegram-ботом

## Что сделано
- Развернул Open Notebook на VPS (приватность: данные не уходят с сервера)
- Загрузил документы (Боулби, 372 чанка)
- Написал skill с explicit activation ("используй knowledge-base")
- Интегрировал поиск через REST API Open Notebook

## Почему Open Notebook, а не NotebookLM
- Приватность: данные на моём сервере, не у Google
- Полный REST API: интеграция с агентом
- Выбор моделей: любой LLM/embeddings, не только Gemini
- Нет лимитов на документы (только железо)

## Trade-offs (честно)
- Нет генерации презентаций (есть у NotebookLM) -
  обошёл отдельным проектом presentation-maker
- UI проще, чем у NotebookLM
- Хостинг и обновления - моя ответственность

## Использование
В Telegram: "используй knowledge-base: что Боулби пишет
про тревогу при разлуке?"

## Tech stack
Docker, SurrealDB, Open Notebook REST API, Hermes, Python
