day_3_input = open('Day_3_input.txt').readlines()

def process_input(puzzle_input=day_3_input):
    """
    Input is list of rectangles with form '#1 @ 912,277: 27x20'

    :param puzzle_input: list of rectangles
    :return:
    """
    rectangle_dict = {key: val for key, val in make_dict_entries(puzzle_input)}
    return rectangle_dict


def make_dict_entries(puzzle_input):
    for rectangle in puzzle_input:
        split_input = rectangle.split()

        dict_key =int(split_input[0][1:])
        xy_tuple = tuple(int(xy) for xy in split_input[2][:-1].split(','))
        xy_dimensions = tuple(int(xy) for xy in split_input[3].split('x'))

        yield dict_key, (xy_tuple, xy_dimensions)






if __name__ == '__main__':
    print(type(day_3_input))
    print(process_input())