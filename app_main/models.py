from django.db import models

# invitation ==> invi
class Invitation(models.Model):
    invi_title = models.CharField(max_length=200)
    invi_writer = models.CharField(max_length=50)
    invi_input_date = models.DateTimeField('date published')
    invi_content = models.TextField()

    def __str__(self):
        return '%s : %s' % (self.invi_writer, self.invi_title) 
