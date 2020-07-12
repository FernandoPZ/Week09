import web 

render=web.template.render('page/views/alumnos/')

class List():
    def GET(self):
      try:
        return render.list()
      except Exception as e:
        return "--E-R-R-R-R--" + str(e.args)
