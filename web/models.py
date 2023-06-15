from django.db import models

# Create your models here.

class About(models.Model):
    titlle = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='profile/')
    description = models.TextField()

    def __str__(self) -> str:
        return self.titlle
    

class ContactSettings(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=250)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.email

class Catagory(models.Model):
    name = models.CharField(max_length=30)
    

    def __str__(self):
        return "%s " % (self.name)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    description = models.TextField()
    blog_image = models.ImageField(upload_to='profile/')
    publish_date = models.DateField()

    def __str__(self):
        return "%s - %s - %s" % (self.title, self.publish_date, self.catagory)