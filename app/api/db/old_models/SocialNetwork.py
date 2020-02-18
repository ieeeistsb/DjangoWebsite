from django.db import models

class SocialNetworkModel(models.Model):

	AVAILABLE_SOCIALS = (
		('facebook' , 'Facebook' ),
		('instagram', 'Instagram'),
		('linkedin' , 'Linkedin' ),
		('twitter'  , 'Twitter'  )
	)

	name = models.CharField(max_length = 100,  choices = AVAILABLE_SOCIALS)

	url  = models.CharField(max_length = 400)

	def __unicode__(self):

		return f'{self.name} with url {self.url}'
