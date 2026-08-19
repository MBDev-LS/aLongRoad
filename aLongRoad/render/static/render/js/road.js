// The Long And Winding Road — road.js
//
// Currently: the mobile disclosure drawer, and the desktop description
// overflow toggle. This is also the file the infinite-scroll loader
// (Issue #7) will land in, once it exists — the sentinel (.road-sentinel),
// status region (.road-status) and aria-busy plumbing on .road are already
// in place in index2.html waiting for it.

function debounce(fn, wait = 150) {
	let t;
	return (...args) => {
		clearTimeout(t);
		t = setTimeout(() => fn(...args), wait);
	};
}

// Suspends CSS transitions on `el` for a programmatic style change, so it
// applies instantly instead of animating like a deliberate user interaction
// would. Without this, the very first collapse of a mobile drawer — on
// load, or on crossing the 640px breakpoint — visibly flashes open before
// snapping shut, because the same transition rule that makes a *click*
// feel smooth also catches this initial state change.
function withoutTransition(el, fn) {
	el.classList.add('no-transition');
	fn();
	void el.offsetHeight; // force layout so the class above is committed before it's removed
	el.classList.remove('no-transition');
}

// Mobile disclosure drawer (design-plan.html §6.1). Progressive
// enhancement: the drawer defaults to open in CSS (meta.css), so with this
// script absent every section's metadata is readable at every width. Below
// 640px this script collapses drawers into an accordion; at or above
// 640px it removes that wiring entirely, so aria-expanded is never exposed
// on a control that would do nothing.
function initDisclosure(road) {
	const NARROW = window.matchMedia('(max-width: 639.98px)');
	const sections = Array.from(road.querySelectorAll('.road-section:not(.road-slot)'));

	function collapseAll() {
		for (const li of sections) {
			li.removeAttribute('data-expanded');
		}
	}

	function syncAria() {
		for (const li of sections) {
			const trigger = li.querySelector('.road-disclosure-trigger');
			if (!trigger) continue;
			trigger.setAttribute('aria-expanded', li.hasAttribute('data-expanded') ? 'true' : 'false');
		}
	}

	function onTriggerClick(event) {
		const li = event.currentTarget.closest('.road-section');
		const wasExpanded = li.hasAttribute('data-expanded');
		// Accordion: collapse whatever was open before opening the new one,
		// in the same frame, per design-plan.html §6.1.
		collapseAll();
		if (!wasExpanded) {
			li.setAttribute('data-expanded', '');
		}
		syncAria();
	}

	function enhance() {
		road.setAttribute('data-enhanced', '');
		collapseAll(); // closed by default on mobile
		syncAria();
	}

	function unenhance() {
		road.removeAttribute('data-enhanced');
		collapseAll();
		for (const li of sections) {
			const trigger = li.querySelector('.road-disclosure-trigger');
			if (trigger) trigger.removeAttribute('aria-expanded');
		}
	}

	for (const li of sections) {
		const trigger = li.querySelector('.road-disclosure-trigger');
		if (trigger) trigger.addEventListener('click', onTriggerClick);
	}

	function applyMode(matchesNarrow) {
		withoutTransition(road, () => {
			if (matchesNarrow) {
				enhance();
			} else {
				unenhance();
			}
		});
	}

	applyMode(NARROW.matches);
	NARROW.addEventListener('change', (event) => applyMode(event.matches));
}

// Desktop description overflow (>= 640px). road.css pins each section's
// row height to its own artwork's rendered height, so — unlike the mobile
// drawer — .road-meta must never grow past that, or the row stretches and
// the chain visibly breaks (a gap opens below the shorter image). The
// description clips in fixed CSS (components/meta.css) regardless of this
// script; this only adds the "More"/"Less" toggle, and only where a
// description is actually being cut off.
//
// .road-meta-more lives in .road-actions, not inside .road-meta-clip — it
// needs to be genuinely outside the clipped box, not just outside the part
// of it that scrolls, or it either scrolls away with the text or eats into
// the limited reading space by sitting pinned over it. That means it isn't
// a descendant of its clip, so the two are found by pairing each button up
// with the clip named in its aria-controls, rather than by DOM containment.
function initDescOverflow(road) {
	const WIDE = window.matchMedia('(min-width: 640px)');
	const pairs = Array.from(road.querySelectorAll('.road-meta-more'))
		.map((more) => ({
			more,
			item: more.closest('li'),
			clip: document.getElementById(more.getAttribute('aria-controls')),
		}))
		.filter((pair) => pair.clip);

	function measure() {
		// Read every clip's overflow state first, then write the results —
		// avoids interleaving layout reads and writes across many sections.
		// Measured on .road-meta-clip-scroll, not .road-meta-clip itself:
		// the scroll wrapper is what actually clips the text (components/
		// meta.css), so its own scrollHeight is the only one that still
		// reflects the full, unclipped content height. .road-meta-clip's
		// scrollHeight would just equal its clientHeight always, since its
		// only sized child is that same wrapper at a fixed height:100%.
		const updates = pairs.map(({ clip, item }) => {
			const scroll = clip.querySelector('.road-meta-clip-scroll');
			const expanded = clip.hasAttribute('data-expanded');
			const truncated = expanded
				? clip.hasAttribute('data-truncated') // already known; don't re-measure while expanded
				: scroll.scrollHeight > scroll.clientHeight + 1;
			return { clip, item, truncated };
		});
		for (const { clip, item, truncated } of updates) {
			clip.toggleAttribute('data-truncated', truncated);
			item.hidden = !truncated;
		}
	}

	function reset() {
		for (const { clip, item, more } of pairs) {
			clip.removeAttribute('data-expanded');
			clip.removeAttribute('data-truncated');
			item.hidden = true;
			more.setAttribute('aria-expanded', 'false');
			more.querySelector('span').textContent = 'More';
		}
	}

	function onMoreClick(event) {
		const more = event.currentTarget;
		const clip = document.getElementById(more.getAttribute('aria-controls'));
		const expanding = !clip.hasAttribute('data-expanded');
		clip.toggleAttribute('data-expanded', expanding);
		more.setAttribute('aria-expanded', String(expanding));
		more.querySelector('span').textContent = expanding ? 'Less' : 'More';
	}

	for (const { more } of pairs) {
		more.addEventListener('click', onMoreClick);
	}

	const debouncedMeasure = debounce(() => { if (WIDE.matches) measure(); });
	window.addEventListener('resize', debouncedMeasure);

	function applyMode(matchesWide) {
		if (matchesWide) {
			measure();
		} else {
			reset();
		}
	}

	applyMode(WIDE.matches);
	WIDE.addEventListener('change', (event) => applyMode(event.matches));
}

const road = document.querySelector('.road');
if (road) {
	initDisclosure(road);
	initDescOverflow(road);
}
