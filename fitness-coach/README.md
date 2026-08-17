# Fitness Coach - AI Fitness Ecosystem

Замкнутый цикл: программа -> тренировка -> запись -> аналитика -> корректировка.

## Архитектура

Telegram -> Hermes (DeepSeek)
   |- rp-periodization  - генерация программ (evidence-based)
   |- workout-logger    - запись тренировок в CSV
   |- fitness-coach     - советы и корректировки
   |- scripts:
       |- log_workout.py    - запись в CSV
       |- plot_progress.py  - графики прогресса

## Замкнутый цикл (closed feedback loop)
1. rp-periodization генерирует программу (volume caps, RPE, %1RM)
2. Пользователь тренируется и пишет в Telegram
3. workout-logger пишет в workouts.csv (единый источник правды)
4. plot_progress строит графики (вес, e1RM по Эпли, объём, частота)
5. fitness-coach анализирует и корректирует программу

## rp-periodization (v4.3.1)
Evidence-based периодизация по принципам Renaissance Periodization:
- Режимы CUT/MAINTAIN/BULK с жёсткими volume caps (sets/muscle/week)
- Recovery override: сон <6ч или дефицит >500 ккал -> caps -20%
- Расчёт рабочих весов: %1RM -> повторы -> кг, RPE/RIR
- Mandatory self-check: таблицы объёма по мышцам ДО вывода программы
- Периодизация: гипертрофия 4-6 нед, сила 3-5 нед, deload каждые 5-6 нед

## Data layer
- workouts.csv - единый источник правды (date, exercise, sets, reps, weight, rpe)
- log_workout.py - запись тренировки
- plot_progress.py - графики: вес, e1RM (Эпли), объём, частота

## Skills layer (fitness-coach/skills/)
- rp-periodization-SKILL.md - генерация программ
- workout-logger-SKILL.md - запись и аналитика
- fitness-coach-SKILL.md - коучинг

## Tech stack
Python 3.12, matplotlib, Hermes skills, Telegram

## Использование
"Запиши: жим лёжа 4x8 @ 105кг RPE 8"
"Составь программу на дефицит, 3 дня в неделю"
"Покажи прогресс в жиме лёжа"
