import re


class FromRandomCharactersGetPassword:
    def __init__(self, path):
        """
        from a file this class discover a possible banking password.
        :param path: path file
        """
        data = [line.rstrip('\n') for line in open(path, 'r')]
        # order data
        data.reverse()
        self.data = list(dict.fromkeys(data))  # remove repeat raws

    @staticmethod
    def _fill_first(data: list) -> str:
        """
        fix the first characters for the password
        :param data:
        :return:
        """
        first = []
        for i in data:
            si = str(i)
            if si[0] not in first:
                first.append(si[0])
        return "".join(first)

    @staticmethod
    def _fill(second_three_fill: str, data: list, i: int, ii: int) -> str:
        """
        fix the next dynamic character for the password
        :param second_three_fill:
        :param data:
        :param i:
        :param ii:
        :return:
        """
        st_data = []
        for row in data:
            si = str(row)
            reg = ".*".join(list(str(si[i:ii]))) # build a regex expresion for find the number on password string
            x = re.search(reg, second_three_fill) # find the regex expression
            not_exist = True if not x else False
            if not_exist and si[ii - 1] not in st_data:
                st_data.append(si[ii - 1])
        return "".join(st_data)

    def discover_password(self) -> str:
        """
        execute the logic for find the password
        :return:
        """
        first_fill = self._fill_first(self.data)
        max_index = len(str(self.data[0]))  # assuming that a rule is not allow a dispair number on character on glues
        for index in range(1, max_index):
            first_fill += self._fill(first_fill, self.data, 0, index + 1)

        return first_fill


path = "./keylog.txt"
from_random_character_password = FromRandomCharactersGetPassword(path)
possible_password = from_random_character_password.discover_password()

print(f"Possible password: {possible_password}")
print(f"Len password: {len(possible_password)}")
