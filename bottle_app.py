from bottle import default_app, route, template
import requests
@route('/chartwithmap')
def chartwithmap():
    return template("chartwithmap")
application = default_app()
