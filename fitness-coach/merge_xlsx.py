"""Миграция тренировок из XLSX журнала в CSV"""
import openpyxl
import csv
from collections import defaultdict

XLSX = "/root/zhurnal_trenirovok.xlsx"
CSV_PATH = "/root/fitness/workouts.csv"

# Маппинг русских названий -> английские коды (как в plot_progress.py)
NAME_MAP = {
    "Жим лёжа": "bench_press",
    "Подтягивания с весом": "weighted_pull_up",
    "Тяга штанги в наклоне": "barbell_row",
    "Жим гантелей сидя": "seated_db_press",
    "Разгибания на блоке": "tricep_pushdown",
    "Приседания": "squat",
    "Румынская тяга": "romanian_deadlift",
    "Жим ногами": "leg_press",
    "Сгибание ног": "leg_curl",
    "Икры стоя": "calf_raise",
    "Икры стоя (смит)": "calf_raise",
    "Тяга верхнего блока": "lat_pulldown",
    "Жим стоя": "overhead_press",
    "Молотки": "hammer_curl",
}

wb = openpyxl.load_workbook(XLSX)
ws = wb["Журнал"]

# Собираем все валидные строки (пропускаем разминки)
entries = []  # (date, exercise_code, weight, reps, rpe)
for row in ws.iter_rows(min_row=5, values_only=True):
    date, day, exercise, weight, reps, rpe, *_ = row
    if not date or not exercise or not weight or not reps:
        continue
    if str(rpe).strip() in ("-", ""):
        continue  # разминка
    code = NAME_MAP.get(str(exercise).strip())
    if not code:
        print(f"Unknown exercise: {exercise}")
        continue
    try:
        entries.append((str(date)[:10], code, float(weight), int(reps), float(rpe) if rpe else None))
    except ValueError:
        continue

# Группируем по (дата, упражнение) — одинаковые подходы сворачиваем
grouped = defaultdict(list)
for e in entries:
    grouped[(e[0], e[1])].append(e)

print(f"Найдено уникальных (дата, упражнение): {len(grouped)}")

# Читаем существующий CSV
existing = set()
with open(CSV_PATH, encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # header
    for row in reader:
        if row:
            existing.add((row[0], row[1]))  # (date, exercise)

# Долить новые
new_rows = []
for (date, ex), sets in sorted(grouped.items()):
    if (date, ex) in existing:
        print(f"Skip (already in CSV): {date} {ex}")
        continue
    # Все подходы одинаковый вес/reps/rpe?
    weights = {s[2] for s in sets}
    reps = {s[3] for s in sets}
    rpes = {s[4] for s in sets if s[4] is not None}
    if len(weights) == 1 and len(reps) == 1:
        rpe = rpes.pop() if rpes else 8.0
        new_rows.append([date, ex, len(sets), list(reps)[0], list(weights)[0], rpe])
        print(f"Add: {date} {ex} {len(sets)}x{list(reps)[0]} @{list(weights)[0]}kg RPE {rpe}")
    else:
        # Разные веса/reps — пишем как несколько строк (plot_progress справится)
        for s in sets:
            rpe = s[4] if s[4] else 8.0
            new_rows.append([date, ex, 1, s[3], s[2], rpe])
            print(f"Add (varied): {date} {ex} 1x{s[3]} @{s[2]}kg RPE {rpe}")

# Записываем
if new_rows:
    with open(CSV_PATH, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for r in new_rows:
            writer.writerow(r)
    print(f"\nЗаписано строк: {len(new_rows)}")
else:
    print("\nНечего добавлять")

# Бэкап XLSX
import shutil, datetime
backup = f"/root/fitness/xlsx_backup_{datetime.date.today()}.xlsx"
shutil.copy(XLSX, backup)
print(f"XLSX сохранён как {backup}")