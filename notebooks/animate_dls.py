import numpy as np

P = """┌────────────────────────────────┐
│    _/_/_/    _/          _/_/_/│
│   _/    _/  _/        _/       │
│  _/    _/  _/          _/_/    │
│ _/    _/  _/              _/   │
│_/_/_/    _/_/_/_/  _/_/_/      │
└────────────────────────────────┘"""


def tostr(arr):
    return '\n'.join([''.join(line) for line in arr])


def toarr(img):
    return np.array([[char for char in line] for line in img.split('\n')])


DEBUG = False


def debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


def anim(img):
    arr = toarr(img)
    debug(arr)
    height, width = arr.shape
    debug(width, height)
    debug(tostr(arr))
    frames = width - 2
    film = []
    for f in range(frames):
        debug('frame', f)
        first = arr[:, [1]]
        for i in range(frames):
            arr[:, [i + 1]] = arr[:, [i + 2]]
        arr[:, [-2]] = first
        r = tostr(arr)
        debug(r)
        film.append(tostr(arr))
    for frame in film:
        print('"""')
        print(frame)
        print('""",')


if __name__ == '__main__':
    anim(P)
