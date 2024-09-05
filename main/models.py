from django.db import models

class Post(models.Model):
    email_id = models.CharField(max_length=100)
    password = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        created_time = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        update_time = self.updated_at.strftime("%Y-%m-%d %H:%M:%S")

        return f"제목: {self.email_id}, 생성시간: {created_time}, 수정시간 {update_time}"


class body_cons(models.Model):
    name = models.CharField(max_length=50)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Question(models.Model):
    number = models.IntegerField(unique=True)
    content = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.content} - {self.number}'

class Choice(models.Model):
    content = models.CharField(max_length=100)
    question = models.ForeignKey(to='main.Question',
                                 on_delete=models.CASCADE)
    body_cons = models.ForeignKey(to='main.body_cons',
                                 on_delete=models.CASCADE,
                                 null=True)