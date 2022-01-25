class Concrete:
    def __init__(self, girth, depth, width):
        self.girth = girth
        self.depth = depth
        self.width = width

    def formwork(self):
        return (self.girth * self.depth) * 2

    def reinforcement(self):
        pass

    def concrete(self)->int:
        return self.girth * self.depth * self.width

class Ground_beam(Concrete):
    def __init__(self, girth, depth, width):
        super().__init__(girth, depth, width)
        self.girth = girth
        self.depth = depth
        self.width = width

    def gb_formwork(self):
        return self.formwork()

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
        self.concrete_in_foundation = Concrete(girth, 8, self.fdn_width // 3)

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
        self.fdn_depth -= self.topsoil_depth #Subtract the top soil from the fdn depth
        return  self.building_area() * self.topsoil_depth

    def bulk_excavation(self):
        return self.girth * self.fdn_width * self.fdn_depth

    def disposal_excavated_material(self):
        return self.topsoil_excavation()

    def earth_work_support(self, depth):
        return (self.girth * depth) * 2

    def surface_treatment(self, depth):
        return (self.girth * depth) * 3

    def blinding(self, depth):
        self.blinding_depth += depth
        return self.girth * self.fdn_width * self.blind_depth


    def reinforcement(self):
        pass

    def formwork_to_fdn_concrete(self):
        return self.concrete_in_foundation.formwork()

    def reinforcement_in_concrete(self):
        return self.concrete_in_foundatin.reinforcement()

    def concrete_in_fdn(self):
        return self.concrete_in_foundation.concrete()

    def filling_to_excavation(self):
        pass

    def filling_to_makeup_level(self, *compartment_area):

        for area in compartment_area:
            area *= 450

    def compacting(self):
        return self.girth * ((self.fdn_width//3) * 2) * self.fdn_depth

def float_to_two_places(func):
    """Convert the value gotten into two decimal places"""
    def inner(value):
        value = func(value)

        return "{:,}".format()
    return inner
    
def format_my_value(value):
    """Formating my number values. As in 1,000,000"""
    return "{:,}".format(value)

grd_beam = Ground_beam(900, 230, 203000);
print(grd_beam.gb_formwork())