import groupy
import sys
from io import StringIO
from groupy import Group
from groupy import Bot


bot = Bot.list().filter(name="Python Bot")[0]
print(bot)

python_group = next(group for group in Group.list() if group.group_id == bot.group_id)


while True:
	newest = None
	try:
		newest = python_group.messages().newest
	except:
		print("failed to connect")
		continue
	

	old = sys.stdout
	old_e = sys.stderr

	text = newest.text
	#text = input("Enter something: ")
	
	if text.startswith(">"):

		if "import os" in text:
			bot.post("Get the fuck out of here")		
			continue

		out = sys.stdout = StringIO()
		try:
			exec(text[1:])
			sys.stdout = old
			out = out.getvalue()
			print(out)
		except Exception as e:
			sys.stdout = old
			out = str(e)
			print(e)
			print("execution failed")
		try:
			bot.post(out)
		except Exception as e:
			print(e)
			print("shit went wrong")


