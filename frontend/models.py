from django.db import models
from urllib.parse import urlparse, parse_qs

# Create your models here.
class Reading(models.Model):
    link = models.URLField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)

    def get_embed_link(self):
            if 'youtube.com' in self.link:
                url_data = urlparse(self.link)
                query = parse_qs(url_data.query)

                # Check if 'v' key is present in the query parameters
                video = query.get('v', None)
                if video:
                    return f"https://www.youtube.com/embed/{video[0]}"
                
            # Return the original link if 'youtube.com' is not present or 'v' key is not found
            return self.link
    
    def __str__(self):
        return self.description
    
    
class Writing(models.Model):
    link = models.URLField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)

    def get_embed_link(self):
            if 'youtube.com' in self.link:
                url_data = urlparse(self.link)
                query = parse_qs(url_data.query)

                # Check if 'v' key is present in the query parameters
                video = query.get('v', None)
                if video:
                    return f"https://www.youtube.com/embed/{video[0]}"
                
            # Return the original link if 'youtube.com' is not present or 'v' key is not found
            return self.link
    
    def __str__(self):
        return self.description
    
class Listening(models.Model):
    link = models.URLField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)

    def get_embed_link(self):
            if 'youtube.com' in self.link:
                url_data = urlparse(self.link)
                query = parse_qs(url_data.query)

                # Check if 'v' key is present in the query parameters
                video = query.get('v', None)
                if video:
                    return f"https://www.youtube.com/embed/{video[0]}"
                
            # Return the original link if 'youtube.com' is not present or 'v' key is not found
            return self.link
    
    def __str__(self):
        return self.description
    
    
class Speaking(models.Model):
    link = models.URLField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)

    def get_embed_link(self):
            if 'youtube.com' in self.link:
                url_data = urlparse(self.link)
                query = parse_qs(url_data.query)

                # Check if 'v' key is present in the query parameters
                video = query.get('v', None)
                if video:
                    return f"https://www.youtube.com/embed/{video[0]}"
                
            # Return the original link if 'youtube.com' is not present or 'v' key is not found
            return self.link
    
    def __str__(self):
        return self.description

class Contact(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    phone = models.CharField(max_length=200,null=True,blank=True)
    message = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
    
class Zoom(models.Model):
    description = models.TextField(null=True,blank=True)

class Blog(models.Model):
    photo = models.ImageField(upload_to='image/',null=True,blank=True)
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    date = models.TextField(null=True,blank=True)

    
    def __str__(self):
        return self.title
    
class About(models.Model):
    image = models.ImageField(upload_to='image/',null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    title = models.CharField(max_length=200,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    phone = models.CharField(max_length=200,null=True,blank=True)
    facebook = models.URLField(null=True,blank=True)
    twitter = models.URLField(null=True,blank=True)
    youtube = models.URLField(null=True,blank=True)
    linkedin = models.URLField(null=True,blank=True)


    def __str__(self):
        return self.title
    
class Enroll(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    phone = models.CharField(max_length=200,null=True,blank=True)
    education = models.CharField(max_length=200,null=True,blank=True)
    attempts = models.CharField(max_length=200,null=True,blank=True)
    desired_score = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name
    
   
class Stories(models.Model):
    link = models.URLField(null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    score = models.CharField(max_length=200,null=True,blank=True)

    def get_embed_link(self):
            if 'youtube.com' in self.link:
                url_data = urlparse(self.link)
                query = parse_qs(url_data.query)

                # Check if 'v' key is present in the query parameters
                video = query.get('v', None)
                if video:
                    return f"https://www.youtube.com/embed/{video[0]}"
                
            # Return the original link if 'youtube.com' is not present or 'v' key is not found
            return self.link
    
    def __str__(self):
        return self.name