class check:

    def swap_len(self, str_1, str_2):
        len_str_1 = len(str_1)
        len_str_2 = len(str_2)
        if len_str_1 < len_str_2 :
            temp = str_1
            str_1 = str_2
            str_2 = temp
        return str_1, str_2

    def gap_len(self, str_1, str_2):
        len_str_1 = len(str_1)
        len_str_2 = len(str_2)
        return 1 - ((len_str_1 - len_str_2) / len_str_2)

    def check_len(self, str_1, str_2):
        str_1, str_2 = self.swap_len(str_1, str_2)
        len_str_1 = len(str_1)
        len_str_2 = len(str_2)
        if len_str_1 == len_str_2 :
            return 60
        elif len_str_1 >= (len_str_2*2):
            return 0
        else :
            return self.gap_len(str_1, str_2)

    def check_alpha(self):
        return 1

    def score(self, first_str, second_str):
        return 1

