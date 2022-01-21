class Concrete:
    def __init__(self, girth, depth, width):
        self.girth = girth
        self.depth = depth
        self.width = width

    def formwork(self):
        return self.girth * 2

    def reinforcement(self):
        pass

    def concrete(self):
        return self.girth * self.depth * self.width

class Substructure:
    def __init__(self, girth, site_breadth, site_length, site_perimeter=None, breadth=None, length=None, perimeter=None):
        self.girth = girth
        self.site_breadth = site_breadth
        self.site_length = site_length
        self.site_perimeter = site_perimeter
        self.breadth = breadth if breadth != None else site_breadth
        self.length = length if length != None else site_length
        self.perimeter = perimeter if perimeter != None else site_perimeter
        self.topsoil_depth = 150
        self.fdn_depth = 450 # Unsure yet
        self.fdn_width = 675 # Unsure yet
        self.concrete = Concrete(girth, self.fdn_depth, self.fdn_width)

    def __str__(self):
        return "Substructure in mm"

    def site_area(self):
        """site area when the area of the site needs to be taken care of apart"""
        return self.length * self.breadth

    def building_area(self):
        """this is for the building area when the site 
        area and the main building area is not the same"""
        return self.site_length * self.site_breadth

    def site_clearance(self):
        return self.site_area()

    def topsoil_excavation(self):
        return  self.building_area() * self.topsoil_depth

    def bulk_excavation(self):
        return self.girth * self.fdn_width * self.fdn_depth

    def disposal_excavated_material(self):
        return self.topsoil_excavation() + self.bulk_excavation()

    def earth_work_support(self, depth, girth):
        return (self.girth * depth) * 2

    def surface_treatment(self, depth, girth):
        return (self.girth * depth) * 3

    def blinding(self, girth, blind_height):
        return format_my_value(self.girth * blind_height)

    def reinforcement(self):
        pass

    def formwork_to_fdn_concrete(self):
        return self.concrete.formwork()

    def reinforcement_in_concrete(self):
        return format_my_value(self.concrete.reinforcement())

    def concrete_in_fdn(self):
        return format_my_value(self.concrete.concrete())

    def filling_to_excavation(self):
        pass

    def filling_to_makeup_level(self):
        pass

    def compacting(self):
        return format_my_value(self.girth * ((self.fdn_width/3) * 2) * self.depth)

def float_to_two_places(func):
    def inner(value):
        value = func(value)

        return "{:,}".format()
    return inner
    
def format_my_value(value):
    """Formating my number values. As in 1,000,000"""
    return "{:,}".format(value)

sub = Substructure(45000.3243, 3400,4300)
print(sub.concrete_in_fdn())