from django.db import models
class Image(models.Model):
    image_name = models.CharField(max_length =30)
    image_description = models.TextField()
    image_path = models.ImageField(upload_to = 'gallery/')
    def __str__(self):
        return self.image_name

    @classmethod
    def search_by_category(cls,search_term):
        search_result = cls.objects.filter(image_category__cat_name__icontains=search_term)
        return search_result

    @classmethod
    def get_image_by_id(cls,incoming_id):
        image_result = cls.objects.get(id=incoming_id)
        return image_result

    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()

        
    @classmethod
    def retrieve_all(cls):
        all_objects = Image.objects.all()
        for item in all_objects:
            return item


    @classmethod
    def update_image(cls,current_value,new_value):
        fetched_object = Image.objects.filter(image_name=current_value).update(image_name=new_value)
        return fetched_object

