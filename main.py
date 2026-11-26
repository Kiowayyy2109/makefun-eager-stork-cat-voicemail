import os

LINE = "You've reached Miso. I'm napping on your keyboard and can't take your call. Leave a treat after the beep."

LIMIT = 120
if len(LINE) != 105 or len(LINE) > LIMIT:
    raise SystemExit(f"line must be 105 chars, got {len(LINE)}")

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

# Spoken aloud it should sound like a cat who owns the phone.
