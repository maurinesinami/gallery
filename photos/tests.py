from django.test import TestCase


from .models import Image,Location,Category


class Photos_TestCases(TestCase):
    def setUp(self):
        self.new_category = Category(category_name='Fashion')
        self.new_category.save_category()
        self.new_location = Location(location_name = 'Atlanta')
        self.new_location.save_location()
        self.new_image = Image(id=1,image_name='Party', description='Party 2017',image='media/gallery/Fashion-3134828_1920.jpg',category=self.new_category,location=self.new_location)
    
    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
        self.assertTrue(isinstance(self.new_category,Category))
        self.assertTrue(isinstance(self.new_location,Location))

    def test_save_method(self):
        self.new_image.save_image()
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects)>0)

    def test_delete_method(self):
        self.new_image.save_image()
        filtered_object = Image.objects.filter(image_name='Party')
        Image.delete_image(filtered_object)
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects) == 0)

    def test_display_all_images_method(self):
        self.new_image.save_image()
        all_objects = Image.get_all_images()
        self.assertEqual(all_objects.image_name,'Party')


    def test_update_single_image(self):
        self.new_image.save_image()
        filtered_object =Image.update_image('Party','Name')
        fetched = Image.objects.get(image_name='Name')
        self.assertEqual(fetched.image_name,'Name')

    def test_get_image_by_id(self):
        self.new_image.save_image()
        fetched_image = Image.get_image_by_id(1)
        self.assertEqual(fetched_image.id,1)

    def test_search_by_category(self):
        self.new_image.save_image()        
        fetch_specific = Category.objects.get(category_name='Fashion')
        self.assertTrue(fetch_specific.category_name=='Fashion')

    def test_filter_by_location(self):
        self.new_image.save_image()        
        fetch_specific = Location.objects.get(location_name='Atlanta')
        self.assertTrue(fetch_specific.location_name=='Atlanta')
