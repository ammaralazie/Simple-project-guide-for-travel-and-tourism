from django.db import models
from django.utils.text import slugify
import datetime
class Contry(models.Model):
    contry_name=models.CharField(max_length=30)
    slug=models.SlugField(blank=True,null=True)
    about=models.TextField(blank=True,null=True)
    history=models.TextField(blank=True,null=True)
    langunge=models.TextField(blank=True,null=True)
    culture=models.TextField(blank=True,null=True)
    wather=models.TextField(blank=True,null=True)
    geography=models.TextField(blank=True,null=True)
    img=models.ImageField(upload_to='photo')
    #######################################
    created=models.DateTimeField(default=datetime.datetime.now)
    #########################################
    tag1=models.CharField(max_length=100)
    tag2=models.CharField(max_length=100)
    tag3=models.CharField(max_length=100)
    tag4=models.CharField(max_length=100)
    tag5=models.CharField(max_length=100)
    tag6=models.CharField(max_length=100)
    ##########################################
    img2=models.ImageField(upload_to='photo')
    img3=models.ImageField(upload_to='photo')
    img4=models.ImageField(upload_to='photo')
    img5=models.ImageField(upload_to='photo')
    img6=models.ImageField(upload_to='photo')
    img7=models.ImageField(upload_to='photo')

    ###########################

    img22=models.ImageField(upload_to='photo')
    img33=models.ImageField(upload_to='photo')
    img44=models.ImageField(upload_to='photo')
    img55=models.ImageField(upload_to='photo')
    img66=models.ImageField(upload_to='photo')
    img77=models.ImageField(upload_to='photo')

    ##########################
    tag11=models.CharField(max_length=100 ,blank=True)
    tag22=models.CharField(max_length=100,blank=True)
    tag33=models.CharField(max_length=100,blank=True)
    tag44=models.CharField(max_length=100,blank=True)
    tag55=models.CharField(max_length=100,blank=True)
    tag66=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.contry_name
    def save(self,*ags,**kwargs):
        if not self.slug :
            self.slug=slugify(self.contry_name)
        return super(Contry,self).save(*ags,**kwargs)
