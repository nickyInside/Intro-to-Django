from django.db import models

#primary key: Django has a default PK called id, but you can specify your own as well

#in sql, the class country will get its own table with a name field and a pop field
class Country(models.Model):
	name = models.CharField(max_length=225)
	population = models.IntegerField()
	
#overrides the default names of the tables
	class Meta:
		db_table = "countries"

#function used by Django - text representaion of the model.
	def __unicode__(self):
		return self.name
