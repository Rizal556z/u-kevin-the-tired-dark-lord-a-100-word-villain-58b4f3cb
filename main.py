"""The Tired Dark Lord: a ~100-word villain monologue.

Pure-stdlib program. Writes the monologue to /output/entry.txt.
The speaker is Lord Anselm of the salt marshes: he exiled his own
brother twenty years ago, runs his conquest by raven and tide, and
now finds the whole business of villainy mostly... administrative.
His tiredness lives in the pauses, the deflections (figs, chairs,
paperwork) and the shrinking of his own grand scheme -- never in
a plain announcement of it.
"""

import os

ENTRY = (
    "Come in. Mind the\u2014 yes, the skulls. I had them polished. Again. "
    "Sit. No, not there. That chair belonged to my brother, and I... "
    "I had him exiled, you know. Twenty years ago. He sends figs every "
    "winter. I eat every last one. Anyway. The plan is simple: at "
    "midnight my ravens take the harbor lanterns, the tide does the "
    "rest, and by dawn the city kneels. Or... crawls. Kneeling takes "
    "effort. I remember when betrayal thrilled me. Now I just want the "
    "paperwork done. So. Kneel, or don't. Bring tea first. The lanterns "
    "are already lit."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    words = ENTRY.split()
    assert 1 <= len(ENTRY) <= 600, "entry must be 1-600 chars"
    assert 90 <= len(words) <= 105, "monologue must be about 100 words"
    assert ENTRY.strip() == ENTRY, "no leading/trailing whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Re-read and verify the gate on what was actually written.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry differs from source text"
    assert 1 <= len(written) <= 600, "written entry outside 1-600 chars"
    assert 90 <= len(written.split()) <= 105, "written entry off word target"


if __name__ == "__main__":
    main()
