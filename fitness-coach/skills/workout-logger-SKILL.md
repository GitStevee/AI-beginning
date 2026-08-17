---
name: workout-logger
description: Log workouts to CSV and generate progress charts (weight, e1RM, volume, frequency)
version: 1.0.0
tags: [fitness, logging, analytics]
---

# Workout Logger & Analytics

## When to Use
- User logs workout data (sets/reps/weight/RPE)
- User asks about progress, charts, frequency, volume, past workouts

## Data Location
Workouts: ~/fitness/workouts.csv
Charts: ~/fitness/charts/<exercise>_progress.png

## Logging Workflow
For EACH exercise in user message, run via terminal:

python3 ~/fitness/log_workout.py <exercise> <sets> <reps> <weight> <rpe>

Rules:
- If RPE is a range (7-8), average it (7.5)
- If RPE missing, use 0
- Multiple exercises = run command for each
- Confirm what was logged with a short line
- Never invent numbers

## Exercise Name Mapping
Map Russian names to English keys:
- жим лёжа → bench_press
- присед → squat
- становая тяга → deadlift
- румынская тяга → rdl
- тяга штанги в наклоне → barbell_row
- тяга верхнего блока → lat_pulldown
- подтягивания с весом → weighted_pull_up
- подтягивания → pull_up
- жим стоя → overhead_press
- жим гантелей сидя → seated_db_press
- жим гантелей наклон → incline_db_press
- разгибания на блоке → tricep_pushdown
- молотки → hammer_curl
- жим ногами → leg_press
- сгибание ног → leg_curl
- икры стоя → calf_raise
- выпады → lunges

## Analytics
When user asks for progress/chart/summary, run via terminal:

python3 ~/fitness/plot_progress.py <exercise>

Script prints text summary and saves PNG to ~/fitness/charts/.
Send the PNG to user via Telegram. If image sending fails, send text summary.

## Listing Exercises
When user asks what exercises exist:

python3 -c "import csv; print(sorted(set(r['exercise'] for r in csv.DictReader(open('/root/fitness/workouts.csv')))))"

## Rules
- Metric units (kg)
- Respond in Russian
