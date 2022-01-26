class Concrete:
    def __init__(self, length, height, width):
        self.length = length
        self.height = height
        self.width = width

    def formwork(self):
        return (self.length * self.depth) * 2

    def reinforcement(self, length):
        return length

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
        self.blind_depth = 0
        self.topsoil_depth = 150
        self.fdn_depth = 1050 # Unsure yet
        self.fdn_width = 230 * 3 # Unsure yet
        self.concrete = Concrete(girth, 8, self.fdn_width // 3)

    def __str__(self):
        return "Substructure in mm"

    def site_area(self):
        """
        site area when the area of the site 
        needs to be taken care of apart
        """
        return self.length * self.breadth

    def building_area(self):
        """
        this is for the building area when the site 
        area and the main building area is not the same
        """
        return self.site_length * self.site_breadth

    def site_clearance(self):
        return self.site_area()

    def topsoil_excavation(self, depth):
        """
        Subtract the top soil from the fdn depth
        """
        self.concrete.height -= depth
        return  self.building_area() * depth

    def disposal_excavated_material(self, depth):
        return self.topsoil_excavation(depth)

    def trench_excavation(self, depth):
        self.concrete.height -= depth
        return self.girth * self.fdn_width * depth


    def earth_work_support(self, depth):
        return (self.girth * depth) * 2

    def surface_treatment(self, depth):
        return (self.girth * depth) * 3

    def blinding(self, depth):
        self.blinding_depth += depth
        return self.girth * self.fdn_width * self.blind_depth

    def formwork_to_ground_beam(self):
        return self.concrete.formwork()

    def reinforcement_in_ground_beam(self):
        return self.concrete.reinforcement()

    def concrete_in_ground_beam(self):
        return self.concrete.concrete()

    def filling_to_excavation(self):
        return self.girth * self.fdn_depth * ((self.fdn_width / 3) * 2)

    def filling_to_makeup_level(self, *compartment_area):
        """
        - get the inputted value of the each room area
        - fill up the room to make it rhyme with
          ground beam height
        """
        self.filling_makeup = self.concrete.height + self.blinding_depth
        areas = [area * self.filling_makeup for area in compartment_area]
        area = sum(areas)
        return area * self.filling_makeup

    def compacting(self):
        return self.filling_makeup

def float_to_two_places(func):
    """Convert the value gotten into two decimal places
       ex- 43.43
    """
    def inner(value):
        value = func(value)

        return "{:,}".format(value)
    return inner
    
def format_my_value(value):
    """Formating my number values. As in 1,000,000"""
    return "{:,}".format(value)