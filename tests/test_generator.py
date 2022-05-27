import pytest

from generator import gen_rythm


def test_first_pause():
    rythm = gen_rythm(9)
    assert rythm.is_proper_rythm() is True

    rythm.syllables[0].syllable = '--'

    assert rythm.no_first_pause() is False


def test_enough_breathing():
    rythm = gen_rythm(9)
    assert rythm.is_proper_rythm() is True

    rythm.syllables[0].syllable = '--'

    assert rythm.no_first_pause() is False
