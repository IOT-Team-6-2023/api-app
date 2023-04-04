from django.db import models

class Party(models.Model):
    party_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)

class Candidate(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50, blank=False, null=False)
    middleName = models.CharField(max_length=50, blank=True)
    lastName = models.CharField(max_length=50, blank=True)
    dateOfBirth = models.DateField()
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.candidate_id) + '-'+ self.firstName + " " + self.middleName + " " + self.lastName
    
class Constituency(models.Model):
    constituency_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.name)
    
class TallyItem(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    constituency = models.ForeignKey(Constituency, on_delete=models.CASCADE)