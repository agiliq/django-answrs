from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

import os.path
import re
import shutil

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique = True)
    pic = models.ImageField(upload_to = 'profiles')
    best_answers = models.IntegerField(default = 0)
    answers = models.IntegerField(default = 0)
    points = models.IntegerField(default = 100)
    
    def save(self):
        oldname = self.pic
        files_ = str(self.pic).split('.')
        ext = files_[len(files_) - 1]
        self.pic = '%s.%s' % (self.user.username, ext)
        super(UserProfile, self).save()
        dirs = settings.MEDIA_ROOT
        oldpath = os.path.join(dirs, oldname).replace('\\','/')
        newpath = os.path.join(dirs, self.pic).replace('\\','/')
        shutil.move(oldpath, newpath)    
    
    class Admin:
        pass

class Category(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    slug = models.SlugField(unique = True)
    
    def save(self):
        self.slug = slugify(self.name)
        super(Category, self).save()
    
    def get_absolute_url(self):
        return '/cat/%s/' % self.slug
    
    def __str__(self):
        return self.name
        
    class Admin:
        pass    

class Question(models.Model):
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length = 300)
    description = models.TextField()
    is_open = models.BooleanField(default = True)
    created_on = models.DateTimeField(auto_now_add = 1)
    
    @models.permalink
    def get_absolute_url(self):
        return ('answrs.views.answer', [self.id])

    def __str__(self):
        return self.title 
    
    class Admin:
        pass    
    
class Answer(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    created_on = models.DateTimeField(auto_now_add = 1)
    text = models.TextField()
    is_best = models.BooleanField(default = True)
    points = models.BooleanField(default = 1)
    
    def __str__(self):
        return self.text    
    
    class Admin:
        pass    
    
def slugify(string):
    string = re.sub('\s+', '_', string)
    string = re.sub('[^\w.-]', '', string)
    return string.strip('_.- ').lower()

