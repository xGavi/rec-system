from dataBase import DataBase

class Game:
	def __init__(self, db : DataBase, name : str, dev : str, pub : str, year: str, *tags : str ):
		self.name = name
		self.dev = dev
		self.pub = pub
		self.year = year
		self.tags = [name, dev, pub, year]
		self.otherTags = tags
		self.tags.extend(tags)
		self.sortTags()
		db.add(self)

	def __repr__(self) -> str:
		return f"{self.name}"# by {self.dev} (Published in {self.year} by {self.pub}). Tags: {self.tags}"

	def __str__(self) -> str:
		out = f"""==============================================
Game: {self.name}
Developer: {self.dev}
Publisher: {self.pub}
Year of Launch: {self.year}
Tags: {self.otherTags}
=============================================="""
		return out


	def sortTags(self) -> None:
		self.tags.sort()
