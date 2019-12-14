from image_recognition.image_labels import get_image_labels
from image_recognition.object_bounds import get_object_bounds

class ImageLabelsTests:
        
    def setup_method(self):
        self.image_labels = get_image_labels("empty_road.png")
        self.object_bounds = get_object_bounds("empty_road.png")

    def test_empty_road_no_cars(self):
        """Ensures no cars are detected in empty road"""
        labels = [x.description.lower() for x in self.image_labels]
        for empty_road_label in ["car", "motor vehicle", "traffic", "truck"]:
            assert empty_road_label not in labels
            
    def test_empty_road_landscape(self):
        """Ensures landscape is properly recognized in empty road"""
        labels = [x.description.lower() for x in self.image_labels]
        for empty_road_label in ["road", "lane", "asphalt"]:
            assert empty_road_label in labels
            
    def test_car_in_front_of_driver(self):
        """Ensures function detects car is not in front of driver"""
        car_object = next((x for x in self.object_bounds if x.name == "Car"), None)
        assert car_object is None