'''
CSC 120 (A8)
File: street.py
Author: Aditya Gupta
Purpose: a program to read given input,
        prompt the user for a one-line
        specification of a city street and 
        then prints a simple ASCII rendering of it.
'''
class Street:
    '''
    Street
    Creates an instance of street
    initialises with zero ht and wt.
    '''
    def __init__(self):
        '''
        __init__
        initialises street object

        Parameters:
            self - object itself
        
        Returns: None
        '''
        self._street = []
        self._height = 0
        self._width = 0

    def street(self):
        '''
        street
        returns the street

        Parameters:
            self - object itself
        
        Returns: street
        '''
        return self._street

    def height(self):
        '''
        height
        returns the height

        Parameters:
            self - object itself
        
        Returns: height
        '''
        return self._height

    def width(self):
        '''
        width
        returns the width

        Parameters:
            self - object itself
        
        Returns: width
        '''
        return self._width

    def add(self, item):
        """
        instance of other class added using this

        Parameters:
            self - object
            item - another class' instance

        Returns: None.
        """
        self._street.append(item)

    def gt_height(self, object):
        """
        gt_height
        changes height of street if other
        object hinders the height

        Parameters:
            self - object itself
            object - height to be checked

        Returns: None
        """
        if object > self.height():
            self._height = object

    def width_inc(self, value):
        """
        width_inc
        changes width of street
        depending on objects added

        Parameters:
            self - object itself
            object - value to increase by

        Returns: None
        """
        self._width += value

    def print_instance(self, h):
        """
        print_instance
        prints the layout of street
        along with objects

        Parameters:
            self - object itself
            h - height

        Returns: None
        """
        if h == -1:
            print ("+" + "-" * self.width() + "+")
        elif h == self.height():
            print ("+" + "-" * self.width() + "+")
            print ("|" + " " * self.width() + "|")
            self.print_instance(h - 1)
        else:
            print ("|" + self.level_street(self._street, h) + "|")
            self.print_instance(h - 1)

    def level_street(self, street_list, h):
        """
        level_street
        checks the street_list and recurses through
        prints each instance of other objects in street

        Parameters:
            self - object itself
            street_list - street list
            h - height

        Returns: string 
        """
        if street_list == []:
            return ""
        else:
            return street_list[0].print_instance(h) \
                + self.level_street(street_list[1:] , h)

    def __str__(self):
        """
        __str__
        string implementation of the st class

        Parameters:
            self - object itself

        Returns: String
        """
        return "H: " + str(self._height) + \
                ", W: " + str(self._width) + \
                    ", St: " + str(self._street)

class Building:
    '''
    Building
    Creates an instance of building
    initialises with width & height
    '''
    def __init__(self, deets):
        '''
        __init__
        initialises building object

        Parameters:
            self - object itself
            deets - what kind string
        
        Returns: None
        '''
        deets = deets.split(",")
        self._shape = []
        self._width = int(deets[0])
        self._height = int(deets[1])
        self._brick = deets[2]
        self.build(self._width, self._height, self._brick)
        
    def width(self):
        '''
        width
        returns the width

        Parameters:
            self - object itself
        
        Returns: width
        '''
        return self._width
    
    def height(self):
        '''
        height
        returns the height

        Parameters:
            self - object itself
        
        Returns: height
        '''
        return self._height

    def brick(self):
        '''
        brick
        returns the brick

        Parameters:
            self - object itself
        
        Returns: brick
        '''
        return self._brick

    def shape(self):
        '''
        shape
        returns the shape

        Parameters:
            self - object itself
        
        Returns: shape
        '''
        return self._shape

    def build(self, w, h, b):
        '''
        build
        builds each lebel of building

        Parameters:
            self - object itself
            w - width
            h - height
            b - build string
        
        Returns: None
        '''
        if h != 0:
            self._shape.append(b * w)
            self.build(w, h - 1, b)
            
    def print_instance(self, h):
        '''
        print_instance
        prints till height h

        Parameters:
            self - object itself
            h - height
        
        Returns: String
        '''
        if h >= self._height:
            return " " * self._width
        else:
            return self._shape[h]
        
    def __str__(self):
        """
        __str__
        string implementation of the class

        Parameters:
            self - object itself

        Returns: String
        """
        return "b:" + str(self._width) + "," + str(self._height) + ","\
            + self._brick + ": " + str(self._shape)

class Park:
    '''
    park
    Creates an instance of park
    initialises with ht and wt.
    '''
    def __init__(self, deets):
        '''
        __init__
        initialises park object

        Parameters:
            self - object itself
            deets - what kind string
        
        Returns: None
        '''
        deets = deets.split(",")
        self._width = int(deets[0])
        self._foliage = deets[1]
        self._shape = []
        self.build(self._width, self._foliage, 5)

    def width(self):
        '''
        width    
        returns the width

        Parameters:
            self - object itself
        
        Returns: width
        '''
        return self._width

    def foliage(self):
        '''
        foliage
        returns the foliage

        Parameters:
            self - object itself
        
        Returns: foliage
        '''
        return self._foliage

    def shape(self):
        '''
        shape
        returns the shape

        Parameters:
            self - object itself
        
        Returns: shape
        '''
        return self._shape

    def build(self, w, f, h):
        '''
        build
        builds each lebel of park

        Parameters:
            self - object itself
            w - width
            h - height
            h - build string
        
        Returns: None
        '''
        if h != 0:
            half = w // 2
            if h == 1:
                self._shape.append(" " * half + f + " " * half)
            elif h == 2:
                self._shape.append(" " * (half - 1) + f * 3 + " "\
                    * (half - 1))
            elif h == 3:
                self._shape.append(" " * (half - 2) + f * 5 + " "\
                    * (half - 2))
            else:
                self._shape.append(" " * half + "|" + " " * half)
            self.build(w, f, h - 1)

    def print_instance(self, h):
        '''
        print_instance
        prints till height h

        Parameters:
            self - object itself
            h - height
        
        Returns: String
        '''
        if h >= 5:
            return " " * self._width
        else:
            return self._shape[h]

    def __str__(self):
        """
        __str__
        string implementation of the class

        Parameters:
            self - object itself

        Returns: String
        """
        return "p:" + str(self._width) + "," \
            + self._foliage + ": " + str(self._shape)

class lots:
    '''
    lots
    Creates an instance of lots
    initialises with ht and wt.
    '''
    def __init__(self, deets):
        '''
        __init__
        initialises building object

        Parameters:
            self - object itself
            deets - what kind string
        
        Returns: None
        '''
        deets = deets.split(",")
        self._width = int(deets[0])
        self._trash = deets[1]
        self._trash = self._trash.replace("_", " ")
        self._shape = ""
        self.build(self._width, self._trash)

    def width(self):
        '''
        width    
        returns the width

        Parameters:
            self - object itself
        
        Returns: width
        '''
        return self._width

    def trash(self):
        '''
        trash  
        returns the trash

        Parameters:
            self - object itself
        
        Returns: trash
        '''
        return self._trash

    def shape(self):
        '''
        shape
        returns the shape

        Parameters:
            self - object itself
        
        Returns: shape
        '''
        return self._shape

    def build(self, w, t):
        '''
        build
        build creates empty lot

        Parameters:
            self - object itself
            w - width
            t - trash string

        Returns: None
        '''
        if w <= len(t):
            self._shape += t[:w]
        else:
            self._shape += t
            self.build(w - len(t), t)

    def print_instance(self, h):
        '''
        print_instance
        prints till height h

        Parameters:
            self - object itself
            h - height
        
        Returns: String
        '''
        if h >= 1:
            return " " * self._width
        else:
            return self._shape

    def __str__(self):
        """
        __str__
        string implementation of the class

        Parameters:
            self - object itself

        Returns: String
        """
        return "e:" + str(self._width) + "," + \
            self._trash + ": " + str(self._shape)

def linereader(list_streets, street):
    '''
    linereader
    Checks the input for available/given objects
    adds the streets and calls other functions
    accordingly, and recurses through itself.

    Parameters:
        list_streets - list of streets
        street - street object

    Returns - None
    '''
    if list_streets != []:
        if list_streets[0][0] == "p":
            p = Park(list_streets[0][2:])
            street.add(p)
            street.gt_height(5)
            street.width_inc(p.width())
        if list_streets[0][0] == "b":
            b = Building(list_streets[0][2:])
            street.add(b)
            if b.width() != 0:
                street.gt_height(b.height())
            if b.height() != 0:
                street.width_inc(b.width())
        if list_streets[0][0] == "e":
            e = lots(list_streets[0][2:])
            street.add(e)
            if e.width() != 0:
                street.gt_height(1)
            street.width_inc(e.width())
        linereader(list_streets[1:], street)

def main():
    street = Street()
    input_st = input("Street: ").split()
    linereader(input_st, street)
    street.print_instance(street.height())

main()