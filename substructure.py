class Substructure:
    def __init__(self,site_breadth, site_length, site_perimeter=None, breadth=None, length=None, perimeter=None):
        self.site_breadth = site_breadth
        self.site_length = site_length
        self.site_perimeter = site_perimeter
        self.breadth = breadth if breadth != None else site_breadth
        self.length = length if length != None else site_length
        self.perimeter = perimeter if perimeter != None else site_perimeter
        self.topsoil_depth = 150
        self.fdn_depth = 450 # Unsure yet
        self.fdn_width = 675 # Unsure yet

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

    def bulk_excavation(self, girth):
        return girth * self.fdn_width * self.fdn_depth

    def disposal_excavated_material(self):
        return self.topsoil_excavation() + self.bulk_excavation()

    def earth_work_support(self, depth):
        return (girth * depth) * 2

    def reinforcement(self):
        pass

    def formwork_to_fdn_concrete(self, girth):
        return girth * 2

    def reinforced_concrete_bed(self):
        pass

    def mass_concrete_blinding(self):
        pass

    def concrete_in_fdn(self):
        pass

    def filling_to_excavation(self):
        pass

    def filling_to_makeup_level(self):
        pass

    def compacting(self):
        pass
    


"""

"""

sub = Substructure(3400,4300)
print(sub.formwork_to_fdn_concrete(4500))