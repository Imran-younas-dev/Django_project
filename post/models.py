from django.db import models
from django.utils import timezone



# class Profile(models.Model):
#     user = models.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    Describe = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def get_date(self):
        time = self.datetime.now()
        if self.created_at.day == time.day:
            return str(time.hour - self.created_at.hour) + " hours ago"
        else:
            if self.created_at.month == time.month:
                return str(time.day - self.created_at.day) + " days ago"
            else:
                if self.created_at.year == time.year:
                    return str(time.month - self.created_at.month) + " months ago"
        return self.created_at
    
    def __str__(self):
        return self.author
