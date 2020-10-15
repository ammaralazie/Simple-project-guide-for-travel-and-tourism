from django.db import models
import datetime
from django.utils.text import slugify
# Create your models here.
class Food(models.Model):
    tilte=models.CharField(max_length=500,null=True,blank=True)
    tilte2=models.CharField(max_length=500,null=True,blank=True)
    tilte3=models.CharField(max_length=500,null=True,blank=True)
    tilte4=models.CharField(max_length=500,null=True,blank=True)
    tilte5=models.CharField(max_length=500,null=True,blank=True)
    tilte6=models.CharField(max_length=500,null=True,blank=True)
    tilte7=models.CharField(max_length=500,null=True,blank=True)
    tilte8=models.CharField(max_length=500,null=True,blank=True)
    tilte9=models.CharField(max_length=500,null=True,blank=True)
    tilte10=models.CharField(max_length=500,null=True,blank=True)
    tilte11=models.CharField(max_length=500,null=True,blank=True)
    tilte12=models.CharField(max_length=500,null=True,blank=True)
    tilte13=models.CharField(max_length=500,null=True,blank=True)
    tilte14=models.CharField(max_length=500,null=True,blank=True)
    tilte15=models.CharField(max_length=500,null=True,blank=True)
    tilte16=models.CharField(max_length=500,null=True,blank=True)
    tilte17=models.CharField(max_length=500,null=True,blank=True)
    tilte18=models.CharField(max_length=500,null=True,blank=True)
    tilte19=models.CharField(max_length=500,null=True,blank=True)
    tilte20=models.CharField(max_length=500,null=True,blank=True)
    tilte21=models.CharField(max_length=500,null=True,blank=True)
    tilte22=models.CharField(max_length=500,null=True,blank=True)
    ###################
    tilte1_image=models.CharField(max_length=500,null=True,blank=True)
    tilte2_image=models.CharField(max_length=500,null=True,blank=True)
    tilte3_image=models.CharField(max_length=500,null=True,blank=True)
    tilte4_image=models.CharField(max_length=500,null=True,blank=True)
    tilte5_image=models.CharField(max_length=500,null=True,blank=True)
    tilte6_image=models.CharField(max_length=500,null=True,blank=True)
    tilte7_image=models.CharField(max_length=500,null=True,blank=True)
    tilte8_image=models.CharField(max_length=500,null=True,blank=True)
    tilte9_image=models.CharField(max_length=500,null=True,blank=True)
    tilte10_image=models.CharField(max_length=500,null=True,blank=True)
    tilte11_image=models.CharField(max_length=500,null=True,blank=True)
    tilte12_image=models.CharField(max_length=500,null=True,blank=True)

    ###############
    slug=models.SlugField(null=True,blank=True,max_length=500)
    ############
    contant1=models.TextField(null=True,blank=True)
    contant2=models.TextField(null=True,blank=True)
    contant3=models.TextField(null=True,blank=True)
    contant5=models.TextField(null=True,blank=True)
    contant6=models.TextField(null=True,blank=True)
    contant7=models.TextField(null=True,blank=True)
    contant8=models.TextField(null=True,blank=True)
    contant9=models.TextField(null=True,blank=True)
    contant10=models.TextField(null=True,blank=True)
    contant11=models.TextField(null=True,blank=True)
    contant12=models.TextField(null=True,blank=True)
    contant13=models.TextField(null=True,blank=True)
    contant14=models.TextField(null=True,blank=True)
    contant15=models.TextField(null=True,blank=True)
    contant16=models.TextField(null=True,blank=True)
    contant17=models.TextField(null=True,blank=True)
    ##############
    create=models.DateTimeField(default=datetime.datetime.now)
    ###############
    img1=models.ImageField(upload_to='pictuer2')
    img2=models.ImageField(upload_to='pictuer2')
    img3=models.ImageField(upload_to='pictuer2')
    img4=models.ImageField(upload_to='pictuer2')
    img5=models.ImageField(upload_to='pictuer2')
    img6=models.ImageField(upload_to='pictuer2')
    img7=models.ImageField(upload_to='pictuer2')
    img8=models.ImageField(upload_to='pictuer2')
    img9=models.ImageField(upload_to='pictuer2')
    img10=models.ImageField(upload_to='pictuer2')
    img11=models.ImageField(upload_to='pictuer2')
    img12=models.ImageField(upload_to='pictuer2')

    ############
    def __str__(self):
        return self.tilte
        #############
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.tilte)
        return super(Food,self).save(*args,**kwargs)
        ########################
class Drink(models.Model):
    tilte=models.CharField(max_length=500,null=True,blank=True)
    tilte2=models.CharField(max_length=500,null=True,blank=True)
    tilte3=models.CharField(max_length=500,null=True,blank=True)
    tilte4=models.CharField(max_length=500,null=True,blank=True)
    tilte5=models.CharField(max_length=500,null=True,blank=True)
    tilte6=models.CharField(max_length=500,null=True,blank=True)
    tilte7=models.CharField(max_length=500,null=True,blank=True)
    tilte8=models.CharField(max_length=500,null=True,blank=True)
    tilte9=models.CharField(max_length=500,null=True,blank=True)
    tilte10=models.CharField(max_length=500,null=True,blank=True)
    tilte11=models.CharField(max_length=500,null=True,blank=True)
    tilte12=models.CharField(max_length=500,null=True,blank=True)
    tilte13=models.CharField(max_length=500,null=True,blank=True)
    tilte14=models.CharField(max_length=500,null=True,blank=True)
    tilte15=models.CharField(max_length=500,null=True,blank=True)
    tilte16=models.CharField(max_length=500,null=True,blank=True)
    tilte17=models.CharField(max_length=500,null=True,blank=True)
    tilte18=models.CharField(max_length=500,null=True,blank=True)
    tilte19=models.CharField(max_length=500,null=True,blank=True)
    tilte20=models.CharField(max_length=500,null=True,blank=True)
    tilte21=models.CharField(max_length=500,null=True,blank=True)
    tilte22=models.CharField(max_length=500,null=True,blank=True)
    ###############
    slug=models.SlugField(null=True,blank=True,max_length=500)
    ############
    tilte1_image=models.CharField(max_length=500,null=True,blank=True)
    tilte2_image=models.CharField(max_length=500,null=True,blank=True)
    tilte3_image=models.CharField(max_length=500,null=True,blank=True)
    tilte4_image=models.CharField(max_length=500,null=True,blank=True)
    tilte5_image=models.CharField(max_length=500,null=True,blank=True)
    tilte6_image=models.CharField(max_length=500,null=True,blank=True)
    tilte7_image=models.CharField(max_length=500,null=True,blank=True)
    tilte8_image=models.CharField(max_length=500,null=True,blank=True)
    tilte9_image=models.CharField(max_length=500,null=True,blank=True)
    tilte10_image=models.CharField(max_length=500,null=True,blank=True)
    tilte11_image=models.CharField(max_length=500,null=True,blank=True)
    tilte12_image=models.CharField(max_length=500,null=True,blank=True)
    #############################
    contant1=models.TextField(null=True,blank=True)
    contant2=models.TextField(null=True,blank=True)
    contant3=models.TextField(null=True,blank=True)
    contant5=models.TextField(null=True,blank=True)
    contant6=models.TextField(null=True,blank=True)
    contant7=models.TextField(null=True,blank=True)
    contant8=models.TextField(null=True,blank=True)
    contant9=models.TextField(null=True,blank=True)
    contant10=models.TextField(null=True,blank=True)
    contant11=models.TextField(null=True,blank=True)
    contant12=models.TextField(null=True,blank=True)
    contant13=models.TextField(null=True,blank=True)
    contant14=models.TextField(null=True,blank=True)
    contant15=models.TextField(null=True,blank=True)
    contant16=models.TextField(null=True,blank=True)
    contant17=models.TextField(null=True,blank=True)
    ##############
    create=models.DateTimeField(default=datetime.datetime.now)
    ###############
    img1=models.ImageField(upload_to='pictuer2')
    img2=models.ImageField(upload_to='pictuer2')
    img3=models.ImageField(upload_to='pictuer2')
    img4=models.ImageField(upload_to='pictuer2')
    img5=models.ImageField(upload_to='pictuer2')
    img6=models.ImageField(upload_to='pictuer2')
    img7=models.ImageField(upload_to='pictuer2')
    img8=models.ImageField(upload_to='pictuer2')
    img9=models.ImageField(upload_to='pictuer2')
    img10=models.ImageField(upload_to='pictuer2')
    img11=models.ImageField(upload_to='pictuer2')
    img12=models.ImageField(upload_to='pictuer2')
    ############
    def __str__(self):
        return self.tilte
        #############
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.tilte)
        return super(Drink,self).save(*args,**kwargs)
        ########################
