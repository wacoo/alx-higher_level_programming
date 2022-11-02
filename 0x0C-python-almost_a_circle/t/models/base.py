
""" Base Class is the super class for all the geometry
sub classes that inherit from it"""
import json
import csv


class Base:
    """ define the base class with attributes and methods"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializing objects"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ converts a dictionary list into json
        format before returning """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save list of instances of inherited to file """
        name = cls.__name__
        with open(name + ".json", "w") as jfile:
            if list_objs is None:
                jfile.write("[]")
            else:
                ls = [lss.to_dictionary() for lss in list_objs]
                dic = Base.to_json_string(ls)
                jfile.write(dic)

    @staticmethod
    def from_json_string(json_string):
        """ decodes json string """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """ load data from file """
        name = cls.__name__ + ".json"
        try:
            with open(name, "r") as jfile:
                list_dic = Base.from_json_string(jfile.read())
                return [cls.create(**dic) for dic in list_dic]
        except IOError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """ creates a class instance for rectangle and square """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save data to csv """
        name = cls.__name__ + ".csv"
        with open(name, "w") as jfile:
            if list_objs is None or list_objs == []:
                jfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fnames = ['id', 'size', 'x', 'y']
                jw = csv.DictWriter(jfile, fieldnames=fnames)
                for obj in list_objs:
                    jw.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Returns a list of classes instantiaated from a csv file """
        try:
            name = cls.__name__ + ".csv"
            with open(name, "r", newline="") as jfile:
                if cls.__name__ == "Rectangle":
                    fns = ["id", "width", "height", "x", "y"]
                else:
                    fns = ["id", "size", "x", "y"]
                list_dics = csv.DictReader(jfile, fieldnames=fns)
                list_dics = [dict([k, int(v)] for k, v in d.items())
                             for d in list_dics]
                return [cls.create(**d) for d in list_dics]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
