from generator import gen_rythm

if __name__ == '__main__':
    while True:
        rythm = gen_rythm(16)
        if rythm.syllables:
            print(rythm.syllables[0])
            if rythm.syllables[0].syllable == '--':
                print('FUCK')