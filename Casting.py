class Casting:
    def to_int(s):
        if type(s) == str:
            return int(s.strip())
        else:
            return s
