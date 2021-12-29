import enum


class Options(enum.Enum):
    Rock = 0,
    Paper = 1,
    Scissors = 2

    @staticmethod
    def _win_map():
        return {
            Options.Rock: Options.Scissors,
            Options.Paper: Options.Rock,
            Options.Scissors: Options.Paper
        }

    @staticmethod
    def _parse_map():
        return {
            'r': Options.Rock,
            'rock': Options.Rock,
            'p': Options.Paper,
            'paper': Options.Paper,
            's': Options.Scissors,
            'scissors': Options.Scissors
        }

    @staticmethod
    def from_string(s):
        return Options._parse_map()[s.lower()]

    @staticmethod
    def is_winner(e1, e2):
        dic = Options._win_map()

        if dic[e1] == e2:
            return True
        elif dic[e2] == e1:
            return False
        # redundant
        else:
            return None
