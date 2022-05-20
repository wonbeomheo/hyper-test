from django.db import models


class Project(models.Model):
    ONGOING = 'ON'
    DELAYED = 'DL'
    DONE = 'DN'
    STATUS_CHOICES = [
        (ONGOING, 'ongoing'),
        (DELAYED, 'delayed'),
        (DONE, 'done'),
    ]
    title = models.CharField(max_length=200)
    detail = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=ONGOING,
    )


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    ONGOING = 'ON'
    DELAYED = 'DL'
    DONE = 'DN'
    STATUS_CHOICES = [
        (ONGOING, 'ongoing'),
        (DELAYED, 'delayed'),
        (DONE, 'done'),
    ]
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=ONGOING,
    )
