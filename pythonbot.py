import groupy
import sys
from io import StringIO
from groupy import Group
from groupy import Bot


bot = Bot.list().filter(name="Python Bot")[0]
print(bot)

python_group = next(group for group in Group.list() if group.group_id == bot.group_id)


while True:
	old = sys.stdout
	try:
		newest = python_group.messages().newest
		text = newest.text
		redirected = sys.stdout = StringIO()
		exec(text)
		sys.stdout = old
		print(redirected.getvalue())
		bot.post(redirected.getvalue())
	except:
		sys.stdout = old
		print("code failed")

