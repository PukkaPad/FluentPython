# bisect(haystack, needle)
# se the binary search algorithm to quickly find and insert items in any sorted sequence

import sys
import bisect

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'



def demo(bisect_fn):
    """
    bisect(haystack, needle) does a binary search for needle in haystack—which must be a sorted sequence—to locate the position where needle can be inserted while main‐ taining haystack in ascending order
    """

    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))

if __name__ == '__main__':
    # print(sys.argv, len(sys.argv))
    # https://stackoverflow.com/a/4118133
    #print('sys.argv[-1]: {0}'.format(sys.argv[-1]))

    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left # I can run like this to activate 'left': $ python3 bisect_ordering.py 'left'
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)


def grade(score, breakpoints = [60, 70, 80, 90], grades='FDCBA'):
    """Given a test score, grade returns the corresponding letter grade
"""
    i = bisect.bisect(breakpoints, score)
    return grades[i]

print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])


