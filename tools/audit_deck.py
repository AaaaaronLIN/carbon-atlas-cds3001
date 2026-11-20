#!/usr/bin/env python3
"""Audience-copy audit for the final deck.

Fails if slides contain internal production/speaker language, if speaker notes are
non-empty, or if the embedded media count is not the expected 3.
"""
import re
import sys
from pptx import Presentation

DECK = sys.argv[1] if len(sys.argv) > 1 else "02_Deliverables_and_Submission/presentation/Carbon_Atlas_Deck.pptx"
FORBIDDEN = [
    r"\bSAY\b", r"screenshot", r"fallback", r"no notes", r"even speaking",
    r"click to play", r"play full screen", r"hook:", r"what it does", r"cta:",
    r"placeholder", r"\bTODO\b", r"internal", r"team note", r"cue card",
    r"\brecording\b", r"0:00", r"0:12", r"0:25", r"Member [A-E]",
]
pat = re.compile("|".join(FORBIDDEN), re.I)
prs = Presentation(DECK)
hits = []

for i, slide in enumerate(prs.slides, 1):
    for sh in slide.shapes:
        texts = []
        if sh.has_text_frame:
            texts.append(sh.text_frame.text)
        if sh.has_table:
            for row in sh.table.rows:
                for cell in row.cells:
                    texts.append(cell.text)
        for t in texts:
            if pat.search(t):
                hits.append((i, sh.name, t[:120].replace("\n", " ")))
    notes = slide.notes_slide.notes_text_frame.text.strip()
    if notes:
        hits.append((i, "NOTES", notes[:120].replace("\n", " ")))

media = [(i, sh.name) for i, s in enumerate(prs.slides, 1) for sh in s.shapes if sh.shape_type == 16]
print("slides:", len(prs.slides))
print("media:", media)
if len(media) != 3:
    hits.append(("media", "expected 3 media shapes", str(media)))
if hits:
    print("FAIL — audience-facing/internal copy found:")
    for h in hits:
        print(" ", h)
    raise SystemExit(1)
print("PASS — no internal production/speaker copy, no speaker notes, 3 media shapes")
