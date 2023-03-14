from django.db import models

class Candidates(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return str(self.candidate_id) + '-'+ self.name
    
class Vote(models.Model):
    candidate_id = models.ForeignKey(Candidates, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(auto_now=True)
    