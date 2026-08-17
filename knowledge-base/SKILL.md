---
name: knowledge-base
description: Search Open Notebook knowledge base (any uploaded documents, books, papers, work docs) via vector search
version: 2.0.0
tags: [rag, knowledge, documents, research, notebook]
---

# Knowledge Base Search (Open Notebook)

## When to Use

Use this skill ONLY when user explicitly asks to search the knowledge base, for example:
- "Используй knowledge-base..."
- "Найди в документах..."
- "Что в моей базе знаний про..."
- "Поиск по Open Notebook..."

Supports ANY uploaded documents: books, research papers, work docs, fitness, psychology, technical specs, contracts, anything.

## How to Search

Use the terminal tool to run this curl command. Replace QUERY with the user's question:

curl -s -X POST http://localhost:5055/api/search -H "Content-Type: application/json" -d '{"query": "QUERY", "type": "vector", "limit": 5, "search_sources": true, "search_notes": true, "minimum_score": 0.3}'

Example for "Что Боулби говорит про страх близости?":

curl -s -X POST http://localhost:5055/api/search -H "Content-Type: application/json" -d '{"query": "Что Боулби говорит про страх близости?", "type": "vector", "limit": 5, "search_sources": true, "search_notes": true, "minimum_score": 0.3}'

## How to Answer

Parse the JSON response. For each item in results array:
- title = source name (document/book)
- matches = relevant text chunks
- similarity = relevance score

Then answer:
- Use ONLY text from the returned chunks
- Quote exact phrases when appropriate
- Cite sources like [Source 1: title], [Source 2: title]
- If results is empty → "В моей базе знаний нет информации по этому вопросу"
- If curl fails → "Open Notebook недоступен" and inform user

## Important

- Always execute curl BEFORE answering
- Never make up citations not in the response
- Respond in Russian unless user writes in English
- If topic is ambiguous — search broader query first, then refine
