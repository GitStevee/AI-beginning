---
name: excel-processor
description: "Process Excel files (.xlsx/.xls/.csv) by user request. Use when user asks to read, edit, merge, split, calculate, create tables, filter, or transform spreadsheet data."
version: 1.0.0
tags: [excel, data, spreadsheets, etl]
---

# Excel Processor

## When to Use
Any request involving Excel/spreadsheet files:
- "покажи содержимое файла"
- "объедини 2 файла"
- "раздели по дате"
- "добавь колонку с суммой"
- "удали пустые строки"
- "сделай сводную таблицу"
- "экспортируй в CSV"
- "посчитай среднее по группам"
- "отфильтруй где цена > 1000"

## Libraries (MANDATORY)
Use pandas (main) + openpyxl (formatting) + xlrd (old .xls) + xlsxwriter (charts).
If missing: pip3 install --break-system-packages pandas openpyxl xlrd xlsxwriter

## Core Operations

### READ (always first - show structure before editing)
df = pd.read_excel("file.xlsx", sheet_name=None)  # all sheets -> dict
df = pd.read_excel("file.xlsx", sheet_name="Лист1")
print("Shape:", df.shape, "Columns:", list(df.columns))
print(df.head(5)); print(df.dtypes)

### MODIFY
df['new_col'] = df['price'] * df['qty']           # add column
df = df[df['price'] > 1000]                       # filter
df = df.dropna()                                  # drop empty
df = df.rename(columns={'old': 'new'})            # rename

### MERGE
merged = pd.merge(df1, df2, on='product_id', how='left')

### SPLIT
for value, group in df.groupby('category'):
    group.to_excel(f"output_{value}.xlsx", index=False)

### AGGREGATIONS
summary = df.groupby('category').agg({'price': ['sum','mean','count']})
pivot = pd.pivot_table(df, values='amount', index='month',
                       columns='category', aggfunc='sum', fill_value=0)

### CREATE FROM SCRATCH
df = pd.DataFrame({'Name': ['A','B'], 'Value': [10, 20]})
df.to_excel("new.xlsx", index=False, sheet_name="Data")

### SAVE (ALWAYS backup before overwrite!)
shutil.copy("file.xlsx", f"file_backup_{date.today()}.xlsx")  # FIRST
df.to_excel("file.xlsx", index=False, sheet_name="Лист1")

## RULES (mandatory)
1. ALWAYS read file first - show structure (sheets, columns, row count, sample)
2. ALWAYS backup before overwrite
3. Ask before destructive ops - deleting columns/rows that have data
4. Preserve encoding (utf-8 for CSV)
5. Show result after each op - sample of modified data
6. Handle large files: pd.read_excel(big, chunksize=10000)
7. Date parsing: pd.to_datetime(df['date'], errors='coerce')
8. Russian column names work as-is

## Output Format
After each operation report: what was done, rows before/after, columns list,
first 3 rows sample, file saved path+size. If destructive - what removed.

## Pitfalls
- NEVER use xlsxwriter to edit existing file (overwrites)
- NEVER forget index=False in to_excel
- NEVER trust column types - check df.dtypes before math
- On mixed types: pd.to_numeric(errors='coerce')
## HARD TRIGGERS (when you see ANY of these words, THIS SKILL IS MANDATORY)
excel, xlsx, xls, таблица, таблицу, лист, свод, pivot, pandas, openpyxl,
соедини файлы, объедини файлы, раздели файл, excel файл, spreadsheet

When any trigger word appears in user request:
1. Load this skill IN FULL
2. Follow ALL rules strictly (backup, show structure, report format)
3. NEVER improvise your own pandas workflow - use Core Operations section

## SELF-CHECK BEFORE RESPONDING
Before sending answer, verify:
- [ ] Backup created before any overwrite?
- [ ] Structure (shape, columns, dtypes) shown BEFORE edit?
- [ ] "rows before / after" reported?
- [ ] Sample of result data shown (not just text summary)?
- [ ] File path + size mentioned?

If ANY unchecked - revise answer before sending.
