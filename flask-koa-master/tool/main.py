from flask import Flask,render_template
from . import more,errors,ad 
app=Flask(__name__)
app.register_blueprint(more.more,url_prefix='/more')
app.register_blueprint(ad.ad,url_prefix='/ad')


@app.route('/')
def ToolsPage(name = None):
    return render_template('base.html',name = 'Tools')

"""
@app.errorhandler(404)
def page_not_found(e):
    response=dict(status=0,message="404 NOT Found")
    return jsonify(response),404
    #return render_template('404.html'),404
	    
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500
"""







'''


def creat_app(config_name):
    app=Flask(__name__)
    app.register_blueprint(more,url_prefix='/more')
    app.config['JSON_AS_ASCII'] = False
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    return app
'''
