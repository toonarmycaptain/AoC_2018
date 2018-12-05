"""
...at least 1000in seems to mean at most 1000in if you look at the data

Use enumerate and zip to be faster?
"""



from AoC_2018_Day_3.Day_3_read_input import process_input



def answer_a(puzzle_input=process_input()):
    """
    Takes rectangle input dict with entry form:
        rectangle_num: (tuple xy coord of top (ie bottom) rt corner, tuple of x, y dimensions)
        eg  3 wide, 2 high rect with bottom rt corner at 2, 2:
        rectangle_num: ((2, 2), 3, 2))
    :param puzzle_input:
    :return:
    """

    coord_dict = make_coord_dict(puzzle_input)

    overlaps = sum(1 for coord_occupants in coord_dict.values() if coord_occupants > 1)

    return overlaps



def make_coord_dict(puzzle_input):
    coord_dict = {}

    for rectangle  in puzzle_input.values():

        start_x_coord = rectangle[0][0]
        start_y_coord = rectangle[0][1]
        x_dim = rectangle[1][0]
        y_dim = rectangle[1][1]
        for x in range(x_dim):
            for y in range(y_dim):
                coordinates = (start_x_coord + x, start_y_coord + y)
                coord_dict[coordinates] = coord_dict.get(coordinates, 0) + 1

    return coord_dict

if __name__ == '__main__':
    print(answer_a())

