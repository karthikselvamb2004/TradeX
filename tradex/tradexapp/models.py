from django.db import models



# Create your models here.
class login(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    user_type=models.CharField(max_length=20)

class user(models.Model):
    name=models.CharField(max_length=100)
    contact=models.CharField(max_length=20)
    loginid=models.ForeignKey('login',on_delete=models.CASCADE)
    status=models.IntegerField(default=0)


class news(models.Model):
    news=models.CharField(max_length=100)
    cdate=models.DateTimeField(auto_now_add=True)

class StockMarketNews(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    source = models.CharField(max_length=255)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


