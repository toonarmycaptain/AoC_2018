day_2_input = open('Day_2_input.txt').readlines()

def process_input(puzzle_input=day_2_input):

    string_list = [x.split()[0] for x in puzzle_input]

    return string_list


if __name__ == '__main__':
    print(type(day_2_input))
    print(process_input())