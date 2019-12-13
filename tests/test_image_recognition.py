from image_recognition.image_labels import get_image_labels
from image_recognition.image_labels import get_object_bounds

class PerceptionTests:
    
    def test_cat_recognition(self):
        """Ensures a cat is recognized in cats image"""
        labels = get_image_labels("four_cats.jpeg")
        assert any(label.description == "Cat" for label in labels)

    def test_count_cats_in_image(self):
        """Ensures 4 cats are counted in cats image"""
        objects = get_object_bounds("four_cats.jpeg")
        object_counter = 0
        for recognized_object in objects:
            if recognized_object.name == "Cat":
                object_counter += 1
        assert object_counter == 4
        
    def test_no_object_in_image(self):
        """Ensures no objects are detected in blank image"""
        objects = get_object_bounds("blank_white.png")
        object_counter = 0
        for recognized_object in objects:
            if recognized_object:
                object_counter += 1
        assert object_counter == 0
     

# test that things dont exist in images, assert dog not in image, bicycle/tricycle
# test the bounds - assert each vertex is >0 and less than 1