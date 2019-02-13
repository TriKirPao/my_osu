class Circle:
    """ class play circle """
    def __init__(self, x, y, radius, number, time):
        self._x = x
        self._y = y
        self._radius = radius
        self._time = time
        self._number = number

    def _gettime():
        return self._time

    def _getx(self):
        try:
            return self._x
        except:
            return -1
    def _setx(self, new_x):
        if new_x > 0 and new_x < 1920 - radius:
            self._x = new_x

    def _gety(self):
        try:
            return self._y
        except:
            return -1
    def _sety(self, new_y):
        if new_y > 0 and new_y < 1080 - radius:
            self._y = new_y

    def _getradius(self):
        return self._radius

    def _getnumber(self):
        return self._number
    time = property(_gettime)
    number = property(_getnumber)
    x = property(_getx, _setx)
    y = property(_gety, _sety)
    radius = property(_getradius)
