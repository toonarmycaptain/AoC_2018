from AoC_2018_Day_3.Day_3_read_input import process_input
from AoC_2018_Day_3.Day_3_part_a import make_coord_dict

def answer_b(puzzle_input=process_input()):
    coord_dict = make_coord_dict(puzzle_input)


    no_overlap_coords = {coord for coord in coord_dict if coord_dict[coord] == 1}

    # narrow down possible rectangles by root point not overlapping
    no_overlap_rect_ids = [rect_id for rect_id in puzzle_input if puzzle_input[rect_id][0] in no_overlap_coords]

    non_overlapping_rectangles = test_rectangles_for_overlaps(no_overlap_rect_ids, no_overlap_coords, puzzle_input)

    if len(non_overlapping_rectangles) == 1:
        return(non_overlapping_rectangles[0])
    return non_overlapping_rectangles


def test_rectangles_for_overlaps(rect_ids_with_non_overlapping_roots, non_overlapped_coords, rect_data_dict):
    clean_rectangle_ids = []

    for rectangle_id in rect_ids_with_non_overlapping_roots:
        if test_rectangle_for_overlaps(rect_data_dict[rectangle_id], non_overlapped_coords):
            clean_rectangle_ids.append(rectangle_id)

    return clean_rectangle_ids


def test_rectangle_for_overlaps(rect_data, no_overlap_coords):
    rect_coord_list = []

    start_x_coord = rect_data[0][0]
    start_y_coord = rect_data[0][1]
    x_dim = rect_data[1][0]
    y_dim = rect_data[1][1]
    for x in range(x_dim):
        for y in range(y_dim):
            new_coord = start_x_coord + x, start_y_coord + y
            rect_coord_list.append(new_coord)

    for coord in rect_coord_list:
        if coord not in no_overlap_coords:
            return False
    return True


if __name__ == '__main__':
    test_input = ['#1 @ 912,277: 3x3\n', '#2 @ 129,477: 5x5\n', '#3 @ 915,716: 3x3\n',
                    '#4 @ 809,807: 3x3\n', '#5 @ 130,478: 2x2\n']
    test_input_q = ['#1 @ 1,3: 4x4\n', '#2 @ 3,1: 4x4\n', '#3 @ 5,5: 2x2\n',]
    # print(answer_b(process_input(test_input)))
    print(answer_b())

