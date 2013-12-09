from django.db import models

from django.contrib.auth.models import User

ROLE = (
	('Tutor', 'Tutor'),
	('Leaner', 'Leaner'),
)
SESSION_STATUS = (
	('New', 'New'),
	('Sold', 'Sold'),
	('Finished', 'Finished'),
	('On going', 'On going')
)
class ProgrammingLanguage(models.Model):
	title = models.CharField('Title', max_length=100)
	description = models.TextField('Description')

	def __unicode__(self):
		return self.title

class Session(models.Model):
	tutor = models.ForeignKey(User, related_name="session_tutor")
	leaner = models.ForeignKey(User, related_name="session_leaner")
	start_time = models.DateTimeField('Strart Time')
	end_time = models.DateTimeField('End Time')
	status = models.CharField('Status', max_length=8, choices=SESSION_STATUS)

	def __unicode__(self):
		return self.tutor.first_name + ' - ' + self.leaner.first_name

class Course(models.Model):
	name = models.CharField('Course',max_length=100)
	description = models.TextField('Description')

class UserProfile(models.Model):
	user = models.ForeignKey(User)
	role = models.CharField('Role', max_length=6)
	programming_languages = models.ManyToManyField(ProgrammingLanguage)
	location = models.TextField('Location')
	hourly_rate = models.CharField('Hourly Rate', max_length=3)
	course = models.ForeignKey(Course,null=True, blank=True)
	card_number = models.IntegerField(null=True, blank=True)
	verification_code = models.CharField(max_length=6,null=True, blank=True)
	expiration_date = models.DateTimeField(null=True, blank=True)


	def __unicode__(self):
		return self.user.first_name + ' ' + self.user.last_name



