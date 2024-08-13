from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.ImageField(upload_to='course_pictures/', blank=True, null=True)

    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, related_name='levels', on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.name} - {self.name}"

class Module(models.Model):
    name = models.CharField(max_length=255)
    level = models.ForeignKey(Level, related_name='modules', on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.level.name} - {self.name}"

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    link_name = models.CharField(max_length=255, blank=True, null=True)
    module = models.ForeignKey(Module, related_name='tasks', on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.module.name} - Task {self.order}"
