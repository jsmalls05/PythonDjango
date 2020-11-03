from django.db import models

#create your model managers here
class ItemManager(models.Manager):
    def itemValidator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['itemName']) == 0:
            errors["itemNameReq"] = "Hey, you can't submit that! Item name is required"
        
        if len(postData['itemDescription']) == 0:
            errors["descReq"] = "Description is required too!"
        
        elif len(postData['itemDescription']) < 8:
            errors['descLength'] = "Description must be at least 8 characters"
        

        
        return errors





# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length = 255)
    lastName = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Item(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField(null = True)
    favoriters = models.ManyToManyField(User, related_name="fav_items")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()





