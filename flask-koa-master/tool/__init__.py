from flask import Flask,render_template
from views import more,errors,ad 
app=Flask(__name__)
app.register_blueprint(more.more,url_prefix='/more')
app.register_blueprint(errors.errors,url_prefix='/errors')
'''


def creat_app(config_name):
    app=Flask(__name__)
    app.register_blueprint(more,url_prefix='/more')
    app.config['JSON_AS_ASCII'] = False
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    return app
'''
