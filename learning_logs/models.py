from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):  #inherits from Model—a parent class included in Django that defines a model’s basic functionality
 """A topic the user is learning about."""
 text = models.CharField(max_length=200)
 date_added = models.DateTimeField(auto_now_add=True) 
 owner = models.ForeignKey(User, on_delete=models.CASCADE)
 def __str__(self):
    """Return a string representation of the model."""
    return self.text   #returns the string stored in the text attribute
class Entry(models.Model):
  """Something specific learned about a topic."""
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
  text = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)
  class Meta:
   verbose_name_plural = 'entries'
  def __str__(self):
   """Return a string representation of the model."""
   return f"{self.text[:50]}..."

#  foreign key is a database term; it’s a reference to another record in the database. This is the 
# code that connects each entry to a specific topic.

# The on_delete=models.CASCADE argument tells Django that when a topic is deleted, all the entries associated with that topic 
# should be deleted as well. 
# This is known as a cascading delete.

# The Meta class holds extra information for managing a model.
# it allows us to set a special attribute telling Django to use Entries when it needs to refer to more than 
# one entry

# The __str__() method tells Django which information to show when it refers to individual entries








# NB...................................................

# CharField—a piece of data that’s made up of characters, or text. You use CharField when you want to store a small amount of 
# text, such as a name, a title, or a city.
# When we define a CharField attribute, we have to tell Django how much space it should reserve in the database.

# The date_added attribute is a DateTimeField—a piece of data that will record a date and time.and
# We pass the argument auto_now_add=True, which tells Django to automatically set this attribute to the current date and time 
# whenever the user creates a new topic.


#1) Activating Models

# To use our models, we have to tell Django to include our app in the overall .
# 
#  Open settings.py (in the learning_log/learning_log directory); you’ll 
# see a section that tells Django which apps are installed and work together in the projectproject,
# then Add our app to this list by modifying INSTALLED_APPS
# ....................................................