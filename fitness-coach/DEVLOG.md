# Фитнес-коуч: журнал разработки

## 2026-08-12 -> 08-17: эволюция трекера тренировок

Ветки развития:
- 8/12 training-log: первый skill, журнал в XLSX (привычный формат)
- 8/16 training-journal: добавлена рекалибровка весов от RPE
- 8/17 training-log-and-calibration: финальная XLSX-версия, связка с rp-periodization
- 8/13 workout-logger: миграция XLSX -> CSV + графики matplotlib

Почему в итоге CSV, а не XLSX:
- CSV = plain text: проще скриптам, git и агенту
- Меньше зависимостей (не нужен openpyxl)
- Графики matplotlib строятся прямо из CSV
- XLSX оставлен как архив (zhurnal_trenirovok.xlsx)

Текущая архитектура:
workout-logger (CSV + аналитика) + rp-periodization (математика/капы) + fitness-coach (коучинг)

## 2026-08-17: консолидация данных
Выяснилось: бот параллельно писал тренировки в XLSX через свои skills
(training-log family, эволюция от 8/12 до 8/17), а CSV-пайплайн стоял
в стороне. Данные размазались по двум форматам.
Решение:
- merge_xlsx.py - миграция 2 пропущенных тренировок (8/15, 8/16) из
  XLSX в CSV с агрегацией подходов по (дата, упражнение), пропуск
  разминок (RPE="-"), обработка varied-весов отдельными строками
- XLSX сохранён как бэкап (xlsx_backup_DATE.xlsx)
- Старые XLSX-skills убраны в ~/.hermes/skills_archive/
- Добавлен HARD CONSTRAINT в USER.md + явный description у
  workout-logger для гарантии что бот пишет в CSV
