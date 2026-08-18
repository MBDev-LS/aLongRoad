// The Long And Winding Road — road.js
//
// Currently: the mobile disclosure drawer only (design-plan.html §6.1).
// This is also the file the infinite-scroll loader (Issue #7) will land
// in, once it exists — the sentinel (.road-sentinel), status region
// (.road-status) and aria-busy plumbing on .road are already in place in
// index2.html waiting for it.
//
// Progressive enhancement: the drawer defaults to open in CSS (meta.css),
// so with this script absent every section's metadata is readable at every
// width. Below 640px this script collapses drawers into an accordion; at
// or above 640px it removes that wiring entirely, so aria-expanded is never
// exposed on a control that would do nothing.

const NARROW = window.matchMedia('(max-width: 639.98px)');

function initDisclosure(road) {
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
        if (matchesNarrow) {
            enhance();
        } else {
            unenhance();
        }
    }

    applyMode(NARROW.matches);
    NARROW.addEventListener('change', (event) => applyMode(event.matches));
}

const road = document.querySelector('.road');
if (road) {
    initDisclosure(road);
}
