import dataclasses
import random


@dataclasses.dataclass
class Syllable:
    syllable: str
    length: int


@dataclasses.dataclass
class Rythm:
    syllables: list[Syllable]

    def get_len(self):
        return sum([syllable.length for syllable in self.syllables])

    def add_syllable(self, syllable: Syllable):
        self.syllables.append(syllable)

    def no_first_pause(self):
        return self.syllables[0].syllable != '--'

    def is_proper_rythm(self):
        if not self.syllables:
            return False
        return self.no_first_pause()

    def __str__(self):
        return ' '.join([syl.syllable for syl in self.syllables])


SYLLABLES: list[Syllable] = [
    Syllable('Tou', 3),
    Syllable('taka', 2),
    Syllable('taka', 2),
    Syllable('tiki', 2),
    Syllable('tiki', 2),
    Syllable('Tawaka', 3),
    Syllable('Tawaki', 3),
    Syllable('Touka', 3),
    Syllable('Touki', 3),
    Syllable('Tp', 1),
    Syllable('--', 1)
]


def gen_rythm(bits: int):
    res = Rythm([])
    while res.get_len() != bits and res.is_proper_rythm:

        if res.get_len() > bits:
            res.syllables = []

        new_syllable = (random.choice(SYLLABLES))
        res.add_syllable(new_syllable)

    return res


if __name__ == '__main__':
    print(gen_rythm(16))