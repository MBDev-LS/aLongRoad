"""Fixture data standing in for Issue #3's model.

The frontend is being built first (project-bible.md §4), so this module is
what render/views.py queries instead of the ORM. get_batch() has the same
shape a real queryset-backed version will need: cursor pagination on slot
number, never offset (bible §8), returning a batch plus the cursor for the
next one (or None when the chain has reached slot 1).

Anchors (entry_l/entry_r/exit_l/exit_r) are illustrative fractions of
artwork width, not measured pixel data — except for the deliberate seam at
slot 9, which reconstructs the real mismatch documented in design-plan.html
§1.3: Road_1 and Road_2 only chain cleanly in one direction. Here Road_2
(slot 8) exits somewhere Road_1 (slot 10) does not enter from, so the vacant
slot 9 between them has to bend across its own height to bridge the two —
demonstrating why vacant slots draw their own connecting road rather than
just being an empty gap.
"""

IMG = {
    "road1": ("images/Road_1.png", 800, 600),
    "road2": ("images/Road_2.png", 800, 600),
    "img1": ("images/image1.png", 800, 600),
    "img2": ("images/image2.png", 800, 800),
    "img3": ("images/image3.png", 600, 800),
}

# (entry_l, entry_r, exit_l, exit_r) per slot, bottom to top. Each slot's
# entry equals the slot below's exit, except across the slot-9 vacant seam.
_SECTIONS = [
    {
        "slot_number": 1,
        "state": "live",
        "title": "Where It Starts",
        "author_name": "Nadia K.",
        "description": (
            "The very first stretch. I wanted something plain and a bit "
            "hopeful — no fanfare, just a road heading off the edge of "
            "the page. Everything after this is someone else's doing."
        ),
        "image": IMG["img1"],
        "anchors": (0.42, 0.58, 0.40, 0.56),
    },
    {
        "slot_number": 2,
        "state": "live",
        "title": "Second Wind",
        "author_name": "Ollie P.",
        "description": "Drawn on a train somewhere between Leeds and York.",
        "image": IMG["img2"],
        "anchors": (0.40, 0.56, 0.36, 0.52),
    },
    {
        "slot_number": 3,
        "state": "live",
        "title": "Low Tide",
        "author_name": "Efe A.",
        "description": (
            "Tried to get the road to feel like it was sinking slightly, "
            "like wet sand. Not sure it reads that way at this size but I "
            "like it anyway."
        ),
        "image": IMG["img3"],
        "anchors": (0.36, 0.52, 0.33, 0.49),
    },
    {
        "slot_number": 4,
        "state": "reserved",
        "anchors": (0.33, 0.49, 0.30, 0.47),
    },
    {
        "slot_number": 5,
        "state": "live",
        "title": "Between Fields",
        "author_name": "Rosa M.",
        "description": "First time drawing anything digitally.",
        "image": IMG["img1"],
        "anchors": (0.30, 0.47, 0.28, 0.46),
    },
    {
        "slot_number": 6,
        "state": "live",
        "title": "Overcast",
        "author_name": "Callum D.",
        "description": (
            "Grey day, grey road. This section took about four evenings, "
            "mostly because I kept redoing the tree line."
        ),
        "image": IMG["img2"],
        "anchors": (0.28, 0.46, 0.27, 0.47),
    },
    {
        "slot_number": 7,
        "state": "live",
        "title": "Turning",
        "author_name": "Beth H.",
        "description": "A bend, because the road needed one here.",
        "image": IMG["img3"],
        "anchors": (0.27, 0.47, 0.29, 0.50),
    },
    {
        "slot_number": 8,
        "state": "live",
        "title": "Outline Sketch",
        "author_name": "Damian G.",
        "description": "Early test drawing, kept as part of the road.",
        "image": IMG["road2"],
        "anchors": (0.29, 0.50, 0.40, 0.58),
    },
    {
        # The bridge: entry matches slot 8's exit, exit matches slot 10's
        # entry. Those two don't match each other, which is the point.
        "slot_number": 9,
        "state": "vacant",
        "anchors": (0.40, 0.58, 0.31, 0.47),
    },
    {
        "slot_number": 10,
        "state": "live",
        "title": "Outline Sketch, Continued",
        "author_name": "Damian G.",
        "description": "The pair to slot 8, drawn the same afternoon.",
        "image": IMG["road1"],
        "anchors": (0.31, 0.47, 0.27, 0.44),
    },
    {
        "slot_number": 11,
        "state": "live",
        "title": "Rise",
        "author_name": "Priya N.",
        "description": "Uphill for once.",
        "image": IMG["img1"],
        "anchors": (0.27, 0.44, 0.30, 0.48),
    },
    {
        "slot_number": 12,
        "state": "live",
        "title": "Switchback",
        "author_name": "Tom O.",
        "description": (
            "Wanted a proper hairpin. Kept the road width steady through "
            "the turn on purpose — a narrowing bend looked like a mistake "
            "every time I tried it."
        ),
        "image": IMG["img2"],
        "anchors": (0.30, 0.48, 0.34, 0.52),
    },
    {
        "slot_number": 13,
        "state": "live",
        "title": "Clearing",
        "author_name": "Sam R.",
        "description": "Short one. Sometimes the road just needs a rest.",
        "image": IMG["img3"],
        "anchors": (0.34, 0.52, 0.31, 0.49),
    },
    {
        "slot_number": 14,
        "state": "live",
        "title": "Latest Addition",
        "author_name": "Jae L.",
        "description": (
            "Whoever draws the next one — the road currently exits here "
            "at roughly a third of the way in from the left. No pressure."
        ),
        "image": IMG["road1"],
        "anchors": (0.31, 0.49, 0.35, 0.53),
    },
]

_MIN_SLOT = min(s["slot_number"] for s in _SECTIONS)
_BY_SLOT = {s["slot_number"]: s for s in _SECTIONS}


def _to_context(raw):
    entry_l, entry_r, exit_l, exit_r = raw["anchors"]
    ctx = {
        "slot_number": raw["slot_number"],
        "state": raw["state"],
        "entry_l": entry_l,
        "entry_r": entry_r,
        "exit_l": exit_l,
        "exit_r": exit_r,
    }
    if raw["state"] == "live":
        path, width, height = raw["image"]
        ctx.update(
            title=raw["title"],
            author_name=raw["author_name"],
            description=raw["description"],
            image=path,
            width=width,
            height=height,
            ratio=height / width,
        )
    else:
        # Vacant/reserved tiles still reserve height as chrome, not artwork.
        ctx.update(width=800, height=500, ratio=500 / 800)
    return ctx


def get_batch(before=None, limit=5):
    """Return (sections, next_cursor).

    Sections are ordered highest slot number first, matching DOM order (the
    top of the road is the highest-numbered completed section). `before`
    filters to slot numbers strictly less than it, mirroring `?before=`.
    next_cursor is the lowest slot number in the batch, or None once slot 1
    has been included — the chain has reached its end.
    """
    pool = sorted(_BY_SLOT.keys(), reverse=True)
    if before is not None:
        pool = [n for n in pool if n < before]
    page = pool[:limit]
    sections = [_to_context(_BY_SLOT[n]) for n in page]
    if not page or page[-1] == _MIN_SLOT:
        next_cursor = None
    else:
        next_cursor = page[-1]
    return sections, next_cursor


def top_section():
    """The highest-numbered completed section, for the head tile's stub."""
    return _to_context(_BY_SLOT[max(_BY_SLOT.keys())])


def jump_to_end_cursor():
    """The `before` value whose batch contains slot 1 — the masthead's
    "jump to the end of the road" link uses this so it is a real, working
    no-JS control rather than a placeholder (bible §11's "otherwise
    unreachable by keyboard" requirement)."""
    return _MIN_SLOT + 1
