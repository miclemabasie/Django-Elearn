from django.db import models
from django.db.models.fields import CharField, DateTimeField
from django.utils import timezone

# An example of Abstract classes

class BaseContent(models.Model):
    title = CharField(max_length=10)
    created = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Text(BaseContent):
    body = models.TextField()

    
# A Multity-Table inheritance example

class BasemultiContent(models.Model):
    title = CharField(max_length=10)
    created = DateTimeField(auto_now_add=True)

class TextMulti(BasemultiContent):
    body = models.TextField()
    

# A Proxy models inheritance example
class ProxyBaseContent(models.Model):
    title = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

class OrderedContent(ProxyBaseContent):
    class Meta:
        proxy = True
        ordering = ['-created']

    def create_delta(self):
        return timezone.now() - self.created
