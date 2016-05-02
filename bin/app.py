import web
from jungletemple import map

urls = (
    '/game', 'GameEngine',
    '/', 'Lobby',
    '/help', 'Help',
    '/lobby', 'Lobby',
    '/about', 'About',
)

app = web.application(urls,globals())

if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store, initializer = {'room': None})
	web.config._session = session
else:
	session = web.config._session

render = web.template.render('templates/', base="layout")


class About(object):
	def GET(self):
	    return render.about()

class Lobby(object):
	def GET(self):
		session.room = map.START
		return render.lobby()


class Help(object):
	def GET(self):
		if session.room:
		    return render.help(room = session.room)
		else: 
		    return render.lobby()


   
class GameEngine(object):
 
	def GET(self):
		if session.room:
			return render.show_room(room=session.room)
		else:
			return render.you_died()
 	
	def POST(self):
		form = web.input(action=None)
 		
		if session.room and form.action:
			if session.room.go(form.action)!=None:
			    session.room = session.room.go(form.action)
			else:
			    session.room = session.room.go('*')
        
 		web.seeother("/game")  


if __name__ == "__main__":
    app.run()

