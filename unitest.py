import unittest
from substructure import Substructure
sub = Substructure(9000,16710, 13720)
length = sub.length
breadth = sub.breadth

class test_substructure(unittest.TestCase):
    def test_site_clearance(self):
        self.assertEqual(sub.site_clearance(), (length*breadth))

    def test_topsoil_excavation(self):
        self.assertEqual(sub.topsoil_excavation(), sub.site_clearance()*150)

    def test_disposal(self):
        self.assertequal(sub.disposal_excavated_material(), sub.topsoil_excavation())

    def test_trench_exctn(self):
        pass

    def test_ews(self):
        pass

    def test_surface_treatment(self):
        pass

    def test_blinding(self):
        pass

    def test_reinforcement(self):
        pass

    def test_formwork(self):
        pass

    def test_concrete(self):
        pass

    def test_compacting(self):
        pass

    def test_dpm(self):
        pass

    def test_reinforcement_slab(self):
        pass

    def test_formwork_slab(self):
        pass

    def test_oversite_concrete_slab(self):
        pass

if __name__ == "__main__":
    unittest.main()
