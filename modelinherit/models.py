from weakref import proxy
from django.db import models
from django.forms import CharField

# Create your models here.
# abstract base class...
class country_model(models.Model):
    country_name=models.CharField(max_length=50)

    class Meta:
        abstract=True

class state_model(country_model):

    state_name=models.CharField(max_length=50)



# multitable inheritance..
class book(models.Model):
    book_name=models.CharField(max_length=50)



class book_info(book):
    book_ptr=models.OneToOneField(book,on_delete=models.CASCADE,parent_link=True,primary_key=True)
    author_name=models.CharField(max_length=50)


#proxy model...

class book_lang(models.Model):
    language=models.CharField(max_length=100)
    book_price=models.IntegerField()

class book_price(book_lang):
    class Meta:
    # objects = NewManager()
        proxy=True


