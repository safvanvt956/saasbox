from django.db import models

# Create your models here.

class Email(models.Model):
    email=models.EmailField(null=True)
    
    def __str__(self):
        return self.email
    
    
class Contact(models.Model):
    fullname=models.CharField(max_length=100) #like
    email=models.EmailField()
    topics=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return self.fullname

    

class Update(models.Model):
    image=models.ImageField()
    title=models.CharField(max_length=100)
    parashap=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    

class About(models.Model):
    ICON_CHOICES = (
        ('bi-cup', 'WordPress'),
        ('bi-star-half', 'Frontend Solution'),
        ('bi-geo-alt', 'Live Chat Help'),
        ('bi-graph-up', 'Frontend'),
        ('bi-pie-chart', 'Digital'),
        ('bi-geo-alt' , 'Branding'),
        ('bi-graph-up' , 'Frontend'),
        ('bi-whatsapp' , 'Live Chat Help')
        # Add more icon choices as needed
    )
    icon = models.CharField(max_length=20, choices=ICON_CHOICES)
    title=models.CharField(max_length=100)
    parashap=models.CharField(max_length=100)


    def __str__(self):
        return self.title
    
 
class Gallery_image(models.Model):
    image=models.ImageField()


class Award(models.Model):
    ICON_CHOICES = (
        ('bi-app-indicator', 'Mobile Apps'),
        ('bi-gear', 'Branding'),
        ('bi-tools', 'WordPress 5.0'),
        ('bi-pie-chart', 'Digital'),
        ('bi-geo-alt' , 'Branding'),
        ('bi-graph-up' , 'Frontend'),
        ('bi-whatsapp' , 'Live Chat Help')
        
        # Add more icon choices as needed
    )

    icon = models.CharField(max_length=20, choices=ICON_CHOICES)
    title=models.CharField(max_length=100)
    parashpa=models.CharField(max_length=100)

    def __str__(self):
        return self.title


    
class Busines(models.Model):
    ICON_CHOICES = (
        ('bi-app-indicator', 'Mobile Apps'),
        ('bi-pie-chart', 'Digital Content'),
        ('bi-tools', 'WordPress 5.0'),
        ('bi-sun', 'Business Idea'),
        # Add more icon choices as needed
    )

    icon = models.CharField(max_length=20, choices=ICON_CHOICES)
    title=models.CharField(max_length=100)
    parashpa=models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class index_portfolio_form(models.Model):
    yourname=models.CharField(max_length=100)  
    email=models.EmailField()
    topics=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return self.yourname
    
        

    


    
    
    



    


    

    
   
    
    

    
    
    
    
