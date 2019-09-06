from django.db import models
# from django.contrib.postgres.fields import ArrayField
# Create your models here.
class contact(models.Model):
    name= models.CharField(
    max_length=100)
    email = models.EmailField(
    max_length=70, null=False, blank=False, unique=True)
    message= models.TextField()

    def __str__(self):
	    return '{} ({})'.format(
		self.email,self.name)


class form(models.Model):
    first_name=models.CharField(max_length=264)
    last_name=models.CharField(max_length=264)
    email=models.EmailField()
    def __str__(self):
        return self.first_name

class blogmodel(models.Model):
    title = models.CharField(max_length=200,unique=True)
    paragraph = models.CharField(max_length=2000)
    url = models.URLField(unique=True)
    date=models.CharField(max_length=50)
    button=models.CharField(max_length=50)
    author=models.CharField(max_length=50)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("core:detail",kwargs={'pk':self.pk})

class newsmodel(models.Model):
    title = models.CharField(max_length=200,unique=True)
    paragraph = models.CharField(max_length=2000)
    image_url = models.URLField()
    date=models.CharField(max_length=50)
    source=models.CharField(max_length=50)
    link_url = models.URLField()
    def __str__(self):
        return self.title



# class solutionmodel(models.Model):
#     index=models.CharField(max_length=2)
#     # title_para = ArrayField(models.CharField(max_length=200, default=list,blank=True))
#     title = models.CharField(max_length=200,unique=True)
#     paragraph = models.CharField(max_length=2000)
#     image_url = models.URLField()
#     title2 = models.CharField(max_length=200,default="",blank=True)
#     paragraph2 = models.CharField(max_length=2000,default="",blank=True)

    # def __str__(self):
    #     return self.title
    # def get_absolute_url(self):
    #     return reverse("core:detail",kwargs={'pk':self.pk})

# class datamod(models.Model):
#     index=models.CharField(max_length=2,default="")
#     num= ArrayField(models.IntegerField( blank=True),size=3,default=list)
#     title= ArrayField(models.TextField(max_length=100, blank=True),size=3,default=list)
#     para= ArrayField(models.TextField(max_length=400, blank=True),size=3,default=list)
#     url_link= ArrayField(models.URLField(blank=True),size=3,default=list)
#     def __str__(self):
#         return self.index
