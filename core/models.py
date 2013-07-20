from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class UserData(models.Model):
	owner = models.ForeignKey(User)
	class Meta:
		abstract=True

class Tag(UserData):
	name = models.TextField()


class Project(UserData):
	name = models.TextField()
	description = models.TextField()
	icon = models.ImageField()
	parent = models.ForeignKey(Project, null=True, blank=True)


class ProjectImage(UserData):
	image = models.ImageField()
	project = models.ForeignKey(Project)

class Protfolio(UserData):
	template = models.TextField()

class ProjectTemplate(UserData):
	template = models.TetField()
	project = mdoels.ForeignKey(Project)
	portfolio = models.ForeignKey(Portfolio)



