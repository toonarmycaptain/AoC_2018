from AoC_2018_Day_1.Day_1_read_input import process_input

def answer_b(frequency_change_list=process_input()):
    current_frequency = 0
    frequency_set = {0}

    # debugging code
    # iteration_tracking_count = 0  # Track number of frequencies iterated through
    # cycle_count = 1

    while True:
        for change in frequency_change_list:
            current_frequency += change
            if current_frequency in frequency_set:
                return current_frequency
            frequency_set.add(current_frequency)

        # debugging code
        #     iteration_tracking_count += 1
            # print('cycle_count:', cycle_count, 'iterations:', iteration_tracking_count, 'current_freq =', current_frequency)
        # print('cycle_count:', cycle_count, 'iterations:', iteration_tracking_count, 'current_freq =', current_frequency)
        # cycle_count += 1


    print('No frequencies reached twice.')
    return None

if __name__ == '__main__':

    print(answer_b())


