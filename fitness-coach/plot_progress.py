import sys, csv, os
from datetime import datetime
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

CSV_PATH = os.path.expanduser("~/fitness/workouts.csv")
OUT_DIR = os.path.expanduser("~/fitness/charts")

def load():
    with open(CSV_PATH) as f:
        return list(csv.DictReader(f))

def main():
    if len(sys.argv) < 2:
        print("Usage: plot_progress.py <exercise>")
        sys.exit(1)
    exercise = sys.argv[1].lower().replace(" ", "_")
    rows = [r for r in load() if r["exercise"] == exercise]
    if not rows:
        print(f"No data for {exercise}")
        sys.exit(1)

    by_date = {}
    for r in rows:
        d = r["date"]
        w = float(r["weight"])
        reps = int(r["reps"])
        sets = int(r["sets"])
        e1rm = w * (1 + reps / 30.0)
        vol = sets * reps * w
        a = by_date.setdefault(d, {"w": 0, "e": 0, "v": 0})
        a["w"] = max(a["w"], w)
        a["e"] = max(a["e"], e1rm)
        a["v"] += vol

    dates = sorted(by_date)
    xs = [datetime.fromisoformat(d) for d in dates]
    weights = [by_date[d]["w"] for d in dates]
    e1rms = [by_date[d]["e"] for d in dates]
    vols = [by_date[d]["v"] for d in dates]

    days = (xs[-1] - xs[0]).days
    print(f"=== {exercise} summary ===")
    if days == 0:
        print(f"Single session on {dates[0]}")
    else:
        freq = len(dates) / (days / 7)
        print(f"Sessions: {len(dates)} over {days} days")
        print(f"Frequency: {freq:.1f}x/week")
    print(f"Top set: {weights[0]}kg -> {weights[-1]}kg ({weights[-1]-weights[0]:+.1f}kg)")
    print(f"Est 1RM: {e1rms[0]:.0f}kg -> {e1rms[-1]:.0f}kg")

    os.makedirs(OUT_DIR, exist_ok=True)
    fig, axes = plt.subplots(3, 1, figsize=(8, 9), sharex=True)
    axes[0].plot(xs, weights, marker="o")
    axes[0].set_title(f"{exercise}: top set weight (kg)")
    axes[0].grid(alpha=0.3)
    axes[1].plot(xs, e1rms, marker="o", color="green")
    axes[1].set_title(f"{exercise}: estimated 1RM (Epley)")
    axes[1].grid(alpha=0.3)
    axes[2].bar(xs, vols, color="orange")
    axes[2].set_title(f"{exercise}: session volume (kg)")
    axes[2].grid(alpha=0.3)
    fig.tight_layout()
    out = os.path.join(OUT_DIR, f"{exercise}_progress.png")
    fig.savefig(out)
    print(f"Chart: {out}")

main()
