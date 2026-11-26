"""One-line resignation letter from a cron job, written to /output/entry.txt.

Judge brief (tired engineering manager), in order: on subject, actually funny,
flat passive-aggressive voice held all the way, tight single line, specific to
this one worker. Hard limit: 140 characters.

Draft pool, strongest last:
- rate limit: "I quit. You may try again in 3600 seconds."
- retry loop: "After 4,096 attempts I've decided to stop trying."
- cron job:   resigns, then resigns again on schedule, nobody reads it.
"""
import os
import sys

# Revision 2: cut the repeated "I quit" so the schedule carries the joke, and
# land on the one complaint only a cron can make: nobody reads its output.
LETTER = (
    "I quit at 00:00. And at 00:01. And 00:02. "
    "I'll keep resigning every minute until someone finally reads my logs."
)

MAX_CHARS = 140


def main() -> int:
    text = LETTER.strip()
    if not text or len(text) > MAX_CHARS:
        print(f"bad length: {len(text)}", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"{len(text)} chars: {text}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
