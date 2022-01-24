import unittest
from substructure import Substructure
sub = Substructure(0,16710, 13720)
length = sub.length
breadth = sub.breadth

class test_substructure(unittest.TestCase):
    def test_site_clearance(self):
        self.assertEqual(sub.site_clearance(), (length*breadth))

    def test_topsoil_excavation(self):
        self.assertEqual(sub.topsoil_excavation(), sub.site_clearance()*150)

if __name__ == "__main__":
    unittest.main()
