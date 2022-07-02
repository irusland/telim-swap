import abc
from typing import Iterable

import numpy as np


class Animation(abc.ABC):
    DELAY = 0.2
    ANIMATION_TAPE = "."

    def __getitem__(self, i: int) -> str:
        return f'```{self.ANIMATION_TAPE[i]}```'

    def __len__(self) -> int:
        return len(self.ANIMATION_TAPE)


# class BarChartAnimation(Animation):
#     ANIMATION_TAPE = '▁▂▃▄▅▆▇█▇▆▅▄▃'
#
#
# class BlindAnimation(Animation):
#     ANIMATION_TAPE = '▉▊▋▌▍▎▏▎▍▌▋▊'
#
#
# class BrailleAnimation(Animation):
#     ANIMATION_TAPE = '⣾⣽⣻⢿⡿⣟⣯⣷'


def tostr(arr):
    return '\n'.join([''.join(line) for line in arr])


def toarr(img):
    return np.array([[char for char in line] for line in img.split('\n')])


def animate(img: str) -> Iterable[str]:
    arr = toarr(img)
    height, width = arr.shape
    frames = width - 2
    film = [tostr(arr)]
    for f in range(frames - 1):
        first = arr[:, [1]]
        for i in range(frames):
            arr[:, [i + 1]] = arr[:, [i + 2]]
        arr[:, [-2]] = first
        film.append(tostr(arr))
    for frame in film:
        yield '\n'.join(('', frame, ''))


class DLSAnimation(Animation):
    DELAY = 0.1

    _DLS = """┌────────────────────────────────┐
│    _/_/_/    _/          _/_/_/│
│   _/    _/  _/        _/       │
│  _/    _/  _/          _/_/    │
│ _/    _/  _/              _/   │
│_/_/_/    _/_/_/_/  _/_/_/      │
└────────────────────────────────┘"""

    def __init__(self):
        self.ANIMATION_TAPE = list(animate(self._DLS))
