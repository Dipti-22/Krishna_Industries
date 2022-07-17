from django.db import models


# makemigrations means to make changes and to store those chages in the file
# # migrate to apply the pending changes to makemigrations 
 
class Contact(models.Model):
    name = models.CharField(max_length= 122)
    email = models.CharField(max_length= 122)
    phone = models.CharField(max_length= 13)
    desc = models.TextField()
    date = models.DateField()

    # to get the name of the person in place of the cantact1 or contact2 in the django file 
    # we just need to create a function # we can also add email with the name of the person 
    # ----------- retrun self.name+self.email --------------------------
    def __str__(self):
        return self.name
    




# Create your models here.