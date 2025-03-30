from django.utils.functional import cached_property
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField("question?",max_length=200)
    pub_date = models.DateTimeField("date published")
    authors = models.ManyToManyField('auth.User', related_name='questions', blank=True)
    is_public = models.BooleanField(db_index=True, default=False)

    class Meta:
        permissions = (
            ('edit_own_question', 'Edit own questions'),
            ('edit_all_question', 'Edit all questions'),
            ('edit_public_problem', 'Edit public problems'),
        )
    
    @cached_property
    def editor_ids(self):
        return self.authors.values_list('id', flat=True)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)