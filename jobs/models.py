from django.db import models

class Job(models.Model):
  STATUS = (
    ('Applied', 'Applied'),
    ('Pending', 'Pending'),
    ('Rejected', 'Rejected')
  )
  company = models.CharField(max_length=100, null=False)
  role = models.CharField(max_length=200, null=False)
  date_applied = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=100, null=False, choices=STATUS)
  link = models.CharField(max_length=500, null=True, blank=True)
#   def __str__(self):
#       return f'{self.company} \t {self.role}'


class Note(models.Model):
  job = models.ForeignKey(Job, null=False, on_delete=models.CASCADE)
  comment = models.CharField(max_length=1000)
  date_created = models.DateTimeField(auto_now_add=True)
#   def __str__(self):
#     return '[ {job}, {role}] \t {comment}'.format(job=self.job.company.upper(), role=self.job.role, comment=self.comment)

  