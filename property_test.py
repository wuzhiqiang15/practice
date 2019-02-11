class Screen(object):

    def __init__(self):
        pass

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width =value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def resolution(self):
        return self.__height *self.__width