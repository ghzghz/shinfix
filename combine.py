from itertools import groupby

"""
This has an assumptions on the key being an integer
due to the current values from each iterator being initialised to 0
maybe this could be init to None instead (is None < min int / min char etc)?
"""

def combine(main, *others):
    iterators = [groupby(it, lambda x: x[0]) for it, fn in others]
    groupers = [fn for it, fn in others]
    currents = [(0, None)] * len(iterators)
    for k in main:
        values = []
        for i, it in enumerate(iterators):
            try:
                while True:
                    ck, cv = currents[i]
                    if ck == k:
                        values.append(groupers[i](cv))
                        break
                    elif ck < k:
                        currents[i] = next(it)
                    else:
                        values.append([])
                        break
            except StopIteration:
                values.append([])
                continue

        yield k, tuple(values)
