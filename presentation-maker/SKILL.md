---
name: presentation-maker
description: Creates PPTX presentations. ACTIVATES with keyword 'Гэндальф' / 'Гендальф' / 'в стиле компании' — then uses branded ~/presentations/make_pptx.py pipeline. Otherwise bot chooses its own approach (pptxgenjs etc).
version: 1.2.0
tags: [presentations, pptx, work, gendalf]
---

# Presentation Maker

## Activation rules

1. If user mentions "Гэндальф" / "Гендальф" / "в стиле компании" / "фирменный стиль Гэндальф":
   → USE THIS SKILL PIPELINE (sections "GENDALF pipeline" below)
   This uses the branded ~/presentations/make_pptx.py with teal/orange 1C-GENDALF style.

2. If user asks for presentation WITHOUT style mention:
   → Let other tools handle it (pptxgenjs etc). Do not force this skill.

3. If user asks for a different brand style (Apple, Google, custom):
   → Build that style yourself, do not use GENDALF pipeline.

## GENDALF pipeline (only when rule 1 triggered)

Brand: 1C-GENDALF
- Teal primary: #127A8D
- Orange accent: #F07C1D
- Dark gradient: #0B3C46 → #127A8D
- Font: Segoe UI (with Light weight for subtitles)
- Available photos: ~/presentations/img/{seminar,team,office}.png

### Steps
1. Get source content:
   - Link: web extract
   - PDF/file: save to ~/presentations/src/, then:
     pdftotext ~/presentations/src/FILE.pdf -
   - Plain text: use as is
2. Build JSON strictly per schema below, save to ~/presentations/job.json
3. Run:
   python3 ~/presentations/make_pptx.py ~/presentations/job.json ~/presentations/result.pptx
4. Send the .pptx file back to user in Telegram (native file send).
5. Briefly list slide structure and ask about changes.

### JSON schema
{
  "title": "...",
  "subtitle": "...",
  "author": "ГК ГЭНДАЛЬФ",
  "date": "ДД.ММ.ГГГГ",
  "slides": [...],
  "final": {"title": "...", "contacts": "1c-gendalf.ru | Ростов-на-Дону"}
}

Slide types:
- bullets: {"type":"bullets","title":"...","items":["..."]} (3-6 items)
- stats: {"type":"stats","title":"...","stats":[{"value":"180","label":"..."}]} (2-3, REAL numbers only)
- bento: {"type":"bento","title":"...","cards":[{"title":"...","text":"..."}]} (2-4 cards)
- table: {"type":"table","title":"...","header":["A","B"],"rows":[["1","2"]]}
- section: {"type":"section","title":"Название раздела"}
- image: {"type":"image","title":"...","caption":"...","image":"/root/presentations/img/seminar.png"}
- chart: {"type":"chart","title":"...","image":"/path.png"}

### Rules
- NEVER invent facts/numbers - only from source
- 5-12 slides; title first, final last
- items/cards = short phrases
- Language: Russian
- If source is thin - ask user what to emphasize