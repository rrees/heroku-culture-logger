import datetime

from pony import orm

from . import models

def add(title, rating=None, category=None, event_date=None, content=None, tags=None):
	if not category:
		category = ''

	if not content:
		content = ''

	if not tags:
		tags = []

	if not event_date:
		event_date = datetime.date.today()

	with orm.db_session:
		log = models.CultureLog(
			title = title,
			event_date = event_date,
			rating = rating,
			category = category,
			content=content,
			tags=tags,
			)
		return log

def update(id, **kwargs):

	with orm.db_session: 
		log = models.CultureLog[id]

		for key, value in kwargs.items():
			print(key)
			if hasattr(log, key):
				print(f'Setting {key}')
				setattr(log, key, value)

	return log