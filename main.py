# u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9: the GPS's own excuse for
# sending the driver down the wrong road. The program writes that single
# line to /output/entry.txt.
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Gate: the entry is one line of 1-200 characters.
MAX_CHARS = 200

# The joke in two beats: the GPS denies the accusation, then reframes it with
# a specific detail (a lakeside wedding, forty minutes late) and ends by
# blaming the map — smug, defensive, caught red-handed. No "recalculating"
# joke; the turn is the wedding the driver was not invited to.
MESSAGE = "I didn't send you into a lake \u2014 I sent you to a lakeside wedding you weren't invited to, forty minutes late. The map said turn left. Blame the map."


def validate_message(text):
    assert 1 <= len(text) <= MAX_CHARS, f"message is {len(text)} chars, must be 1-200"
    assert text.strip(), "message must not be only whitespace"
    assert "\n" not in text, "message must be a single line"


def main():
    validate_message(MESSAGE)
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
