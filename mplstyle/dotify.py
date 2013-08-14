import collections

class Dotty(object):
	def __init__(self, key, val):
		self.key = key
		self.val = val

def _dotify_nested(d, path=[]):
	dotted = [ _dotify_nested(d[k], path + [k]) if type(d[k]) == dict else Dotty(".".join(path + [k]), d[k]) for k in d ]
	return dotted

def _flatten(l):
    for el in l:
		if isinstance(el, collections.Iterable) and not isinstance(el, basestring):
			for sub in _flatten(el):
				yield sub
		else:
			yield (el.key, el.val)

def dotify(d):
	return dict(_flatten(_dotify_nested(d)))
