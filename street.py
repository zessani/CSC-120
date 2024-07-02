class Building:
    def __init__(self, width, height, brick):
        self._width = int(width)
        self._height = int(height)
        self._brick = brick

    def height(self):
        return self._height

    def width(self):
        return self._width

    def brick(self):
        return self._brick

    def at_height(self, height):
        if height >= self._height:
            return ' ' * self._width
        else:
            return self._brick * self._width


class Park:
    def __init__(self, details):
        details = details.split(",")
        self._width = int(details[0])
        self._tree = details[1]

    def get_width(self):
        return self._width

    def at_height(self, height):
        if height >= 5:
            return ' ' * self._width
        elif height == 4:
            return (' ' * (self._width // 2)) + self._tree + (' ' * (self._width // 2))
        elif height == 3:
            return (' ' * (self._width // 2 - 1)) + (self._tree * 3) + (' ' * (self._width // 2 - 1))
        elif height == 2:
            return (' ' * (self._width // 2 - 2)) + self._tree * 5 + (' ' * (self._width // 2 - 2))
        elif height == 1:
            return (' ' * (self._width // 2)) + '|' + (' ' * (self._width // 2))
        elif height == 0:
            return (' ' * (self._width // 2)) + '|' + (' ' * (self._width // 2))

class EmptyLot:
    def __init__(self, width, trash):
        self._width = int(width)
        self._trash = trash

    def at_height(self, height):
        if height == 0:
            pattern = ". ` "
            return pattern * (self._width // 5) + "."
        else:
            return ' ' * self._width



    def width(self):
        return self._width


class Street:
    def __init__(self):
        self._street = []
        self._height = 0
        self._width = 0

    def street(self):
        return self._street

    def height(self):
        return self._height

    def width(self):
        return self._width

    def add(self, item):
        self._street.append(item)

    def gt_height(self, object):
        if object > self.height():
            self._height = object

    def width_inc(self, value):
        self._width += value

    def print_instance(self, h):
        if h == -1:
            print("+" + "-" * self.width() + "+")
        elif h == self.height():
            print("+" + "-" * self.width() + "+")
            print("|" + " " * self.width() + "|")
            self.print_instance(h - 1)
        else:
            print("|" + self.level_street(self._street, h) + "|")
            self.print_instance(h - 1)

    def level_street(self, street_list, h):
        if street_list == []:
            return ""
        else:
            return street_list[0].at_height(h) + self.level_street(street_list[1:], h)

def read_file(list_streets, street):
    if list_streets != []:
        if list_streets[0][0] == "p":
            p = Park(list_streets[0][2:])
            street.add(p)
            street.gt_height(5)
            street.width_inc(p.get_width())
        elif list_streets[0][0] == "b":
            building_details = list_streets[0][2:].split(",")
            b = Building(*building_details)
            street.add(b)
            if b.width() != 0:
                street.gt_height(b.height())
            if b.height() != 0:
                street.width_inc(b.width())
        elif list_streets[0][0] == "e":
            empty_lot_details = list_streets[0][2:].split(",")
            e = EmptyLot(empty_lot_details[0], empty_lot_details[1])

            street.add(e)
            if e.width() != 0:
                street.gt_height(1)
            street.width_inc(e.width())
        read_file(list_streets[1:], street)


def main():
    street = Street()
    input_st = input("Street: ").split()
    read_file(input_st, street)
    street.print_instance(street.height())

main()
