from django.db import models

class ListeningExam(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class ListeningQuestion(models.Model):
    exam = models.ForeignKey(ListeningExam, on_delete=models.CASCADE)
    question_text = models.TextField()

    def __str__(self):
        return self.question_text

class ListeningOption(models.Model):
    question = models.ForeignKey(ListeningQuestion, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.option_text

class ReadingExam(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class ReadingQuestion(models.Model):
    exam = models.ForeignKey(ReadingExam, on_delete=models.CASCADE)
    question_text = models.TextField()

    def __str__(self):
        return self.question_text

class ReadingBlank(models.Model):
    question = models.ForeignKey(ReadingQuestion, on_delete=models.CASCADE)
    blank_text = models.CharField(max_length=200)

    def __str__(self):
        return self.blank_text
