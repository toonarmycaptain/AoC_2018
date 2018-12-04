from AoC_2018_Day_2.Day_2_read_input import process_input

def answer_b(puzzle_input=process_input()):
    match_list = []
    for first_word in puzzle_input:
        for second_word in puzzle_input:
            if one_letter_different(first_word, second_word):
                if first_word != second_word and (second_word, first_word) not in match_list: # check pair not already in list.
                    match_list.append((first_word, second_word))

    answer_list = []
    for pair in match_list:
        answer = ''
        for letter_1, letter_2 in zip(pair[0], pair[1]):
            if letter_1 == letter_2:
                answer += letter_1
        answer_list.append(answer)

    if len(answer_list) == 1:
        return answer_list[0]
    # else:  # ie if more than one answer found
    return_string = 'Found more than 1 answer: '
    for answer in answer_list:
        return_string += answer, ' '
    return answer_list


def one_letter_different(word_1, word_2):
    one_different = False

    for letter_a, letter_b in zip(word_1, word_2):  # zip('abc', 'zzc') yields ('a', 'z'), ('b', 'z'), ('c', 'c')
        if letter_a != letter_b:
            if one_different:  # if already found one difference
                return False
            else:
                one_different = True

    return one_different


if __name__ == '__main__':

    print(answer_b())

'bvnfawcnyoeyudzrpgsleimtkj'
'bvnfawcnyoeyudzrpgsldimtkj'

'bvnfawcnyoeyudzrpgsldimtkj'
'bvnfawcnyoeyudzrpgsleimtkj'