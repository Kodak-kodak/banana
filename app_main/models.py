from django.db import models

class Invitation(models.Model):
    invitation_title = models.CharField(max_length=200)
    invitation_writer = models.CharField(max_length=50)
    invitation_input_date = models.DateTimeField('date published')
    invitation_content = models.TextField()

    def __str__(self):
        return '%s : %s' % (self.invitation_writer, self.invitation_title) 
