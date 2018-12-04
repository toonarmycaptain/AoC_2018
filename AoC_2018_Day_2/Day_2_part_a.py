from collections import Counter

from AoC_2018_Day_2.Day_2_read_input import process_input



def answer_a(puzzle_input=process_input()):
    two_letters = []
    three_letters = []
    for word in puzzle_input:
        counts = Counter(word)  # Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})

        # print('counts:', counts)

        for freq in list(counts.values()):
            if freq == 2:
                two_letters.append(word)
                break
        for freq in list(counts.values()):
            if freq == 3:
                three_letters.append(word)
                break

    # print('two_letters:', two_letters)
    # print('three_letters:', three_letters)

    return len(two_letters) * len(three_letters)

if __name__ == '__main__':
    print(answer_a())
