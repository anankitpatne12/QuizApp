from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Use this custom manager to get the active quiz while working on the frontend part of application
# class ActiveQuizManager(models.Manager):
#     def get_active_quiz(self):
#         current_datetime = timezone.now()
#         active_quiz = self.filter(start_date__lte=current_datetime, end_date__gte=current_datetime).first()
#         return active_quiz


class Quiz(models.Model):
    STATUS_CHOICES = (
        ('inactive', 'Inactive'),
        ('active', 'Active'),
        ('finished', 'Finished'),
    )

    question = models.TextField()
    options = models.JSONField()
    right_answer = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def save(self, *args, **kwargs):
        # Update the status based on the current date and time
        now = timezone.now()
        if now < self.start_date:
            self.status = 'inactive'
        elif now > self.end_date:
            self.status = 'finished'
        else:
            self.status = 'active'
        super().save(*args, **kwargs)


    def __str__(self):
        return self.question

    # objects = models.Manager()  # The default manager
    # active_quiz_objects = ActiveQuizManager()  # Custom manager for active quizzes
    
@receiver(pre_save, sender=Quiz)
def update_quiz_status(sender, instance, **kwargs):
    current_datetime = timezone.now()
    if instance.start_date <= current_datetime <= instance.end_date:
        instance.status = 'active'
    elif current_datetime > instance.end_date:
        instance.status = 'finished'
    else:
        instance.status = 'inactive'


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text
