from django.db import models
from django.contrib.auth.models import User #to make hunter a user

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    body=models.TextField()
    url=models.TextField()
    image=models.ImageField(upload_to='images/')
    icon=models.ImageField(upload_to='images/')
    votes_total=models.IntegerField(default=1)#when someone post then 1 votes by default
    hunter=models.ForeignKey(User, on_delete=models.CASCADE)

    #hunter should be an actual user in the databae
    #Foreignkey is saying get the id of these other models so we can reference them, id no of different user is stored when it comes to the hunter

    #on_delete=models.cascade means that if the user is deletd then then his products will also be deleted

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
