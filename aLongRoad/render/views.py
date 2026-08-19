from django.shortcuts import render
from django.http import HttpResponseNotFound

from . import fixtures


def index2_view(request):
	return HttpResponseNotFound('Please leave')


def _parse_before(request):
	raw = request.GET.get('before')
	if raw is None:
		return None
	try:
		return int(raw)
	except ValueError:
		return None


def index_view(request):
	"""Masthead, head tile, and the first batch of the road.

	`before` lets a no-JS "Continue down the road" link (rendered by
	_batch.html) deep-link straight to the next stretch, since it's just an
	ordinary GET with a cursor.
	"""
	before = _parse_before(request)
	sections, next_cursor = fixtures.get_batch(before=before)
	return render(request, 'render/index.html', {
		'sections': sections,
		'next_cursor': next_cursor,
		'top_section': fixtures.top_section(),
		'jump_to_end_before': fixtures.jump_to_end_cursor(),
		'is_first_batch': before is None,
	})


def road_batch_view(request):
	"""Fragment endpoint the loader (Issue #7) will call as `/v2/road/?before=`.

	Renders the same _batch.html partial index2.html uses for its first
	batch — one markup source for both the server-rendered page and every
	subsequently loaded batch (bible §8, design-plan.html §8.2).
	"""
	before = _parse_before(request)
	sections, next_cursor = fixtures.get_batch(before=before)
	return render(request, 'render/_batch.html', {
		'sections': sections,
		'next_cursor': next_cursor,
	})
