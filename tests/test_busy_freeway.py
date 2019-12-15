from image_recognition.image_labels import get_image_labels
from image_recognition.object_bounds import get_object_bounds

class BusyFreewayTests:
    
    def setup_method(self):
        self.image_labels = get_image_labels("busy_freeway.jpg")
        self.object_bounds = get_object_bounds("busy_freeway.jpg")
    
    def test_road_recognition(self, benchmark):
        benchmark(self.validate_road_recognition)
        
    def validate_road_recognition(self):
        """Ensures correct labels recognized in freeway image"""
        labels = [x.description.lower() for x in self.image_labels]
        freeway_labels = ["lane", "traffic", "road", "motor vehicle", "freeway"]
        for freeway_label in freeway_labels:
            assert freeway_label in labels
            
    def test_car_in_front_of_driver(self, benchmark):
        benchmark(self.validate_car_in_front_of_driver)
    
    def validate_car_in_front_of_driver(self):
        """Ensures function detects car in front of driver"""
        car_object = next((x for x in self.object_bounds if x.name == "Car"), None)
        assert car_object is not None
        
    def test_car_position(self, benchmark):
        benchmark(self.validate_car_position)    
    
    def validate_car_position(self):
        """Ensures function returns correct position for car in front of driver """
        expected_car = {
            "top_left": {
                "x": 0.57245612,
                "y": 0.6841895
            },
            "top_right": {
                "x": 0.68708038,
                "y": 0.6841895
            },
            "bottom_right": {
                "x": 0.68708038,
                "y": 0.81795764
            },
            "bottom_left": {
                "x": 0.57245612,
                "y": 0.81795764
            }
        }
        car_object = next((x for x in self.object_bounds if x.name == "Car"), None)
        actual_car = {
            "top_left": {
                "x": round(car_object.bounding_poly.normalized_vertices[0].x, 8),
                "y": round(car_object.bounding_poly.normalized_vertices[0].y, 8)
            },
            "top_right": {
                "x": round(car_object.bounding_poly.normalized_vertices[1].x, 8),
                "y": round(car_object.bounding_poly.normalized_vertices[1].y, 8)
            },
            "bottom_right": {
                "x": round(car_object.bounding_poly.normalized_vertices[2].x, 8),
                "y": round(car_object.bounding_poly.normalized_vertices[2].y, 8)
            },
            "bottom_left": {
                "x": round(car_object.bounding_poly.normalized_vertices[3].x, 8),
                "y": round(car_object.bounding_poly.normalized_vertices[3].y, 8)
            }
        }
        assert expected_car == actual_car