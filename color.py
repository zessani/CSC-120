class Color:
    def __init__(self,r,g,b):
        self._r = r
        self._g = g
        self._b = b

    def _check_range(self, value):
        if value < 0:
            return 0
        elif value > 255:
            return 255
        else:
            return value
    
    def get_rgb(self):
        return (self._r, self._g, self._b)

    def remove_red(self):
        self._r = 0

    def __str__(self):
        return "Color("+self._r ,self._g, self._b+")"

    def __eq__(self, other):
            return (self._r, self._g, self._b) == (other._r, other._g, other._b)
       