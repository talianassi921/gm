from image_labels import get_image_labels

class PerceptionTests:
    
    def test_cat_recognition(self):
        """Ensures a cat is recognized in cats image"""
        labels = get_image_labels("four_cats.jpeg")
        assert any(label.description == "Cat" for label in labels)

    
     