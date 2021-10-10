class Largest_number:

    def get_largest_number(self, input_list):
        largest_num = None
        for number in input_list:
            if (largest_num is None or number > largest_num):
                largest_num = number
        return largest_num
