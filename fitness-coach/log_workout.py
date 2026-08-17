import sys, csv, os
from datetime import date

CSV_PATH = os.path.expanduser("~/fitness/workouts.csv")
HEADER = ["date", "exercise", "sets", "reps", "weight", "rpe"]

def main():
    if len(sys.argv) < 6:
        print("Usage: log_workout.py <exercise> <sets> <reps> <weight> <rpe> [date]")
        sys.exit(1)
    exercise = sys.argv[1].lower().replace(" ", "_")
    sets = int(sys.argv[2])
    reps = int(sys.argv[3])
    weight = float(sys.argv[4])
    rpe = float(sys.argv[5])
    d = sys.argv[6] if len(sys.argv) > 6 else date.today().isoformat()

    new_file = not os.path.exists(CSV_PATH)
    with open(CSV_PATH, "a", newline="") as f:
        w = csv.writer(f)
        if new_file:
            w.writerow(HEADER)
        w.writerow([d, exercise, sets, reps, weight, rpe])
    print(f"Logged: {d} {exercise} {sets}x{reps} @ {weight}kg RPE {rpe}")

main()
