day_1_input = open('Day_1_input.txt').readlines()

def process_input(puzzle_input=day_1_input):

    int_list = [int(x) for x in puzzle_input]
    return int_list


if __name__ == '__main__':
    print(type(day_1_input))
    print(process_input())