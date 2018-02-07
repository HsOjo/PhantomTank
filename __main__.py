from sys import exit

from app import Application

app = Application()
app.start()
exit(app.status)
