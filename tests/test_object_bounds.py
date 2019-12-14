from object_bounds import get_object_bounds

class ObjectBoundsTests:

    def test_count_cats_in_image(self):
        """Ensures 4 cats are counted in cats image"""
        objects = get_object_bounds("four_cats.jpeg")
        assert len(objects) == 4
        
    def test_no_object_in_image(self):
        """Ensures no objects are detected in blank image"""
        objects = get_object_bounds("blank_white.png")
        assert len(objects) == 0
        
    def test_object_bounds(self):
        """Ensures object vertices are between 0 and 1"""
        objects = get_object_bounds("four_cats.jpeg")
        # assert that each vertex is between 0 and 1
        