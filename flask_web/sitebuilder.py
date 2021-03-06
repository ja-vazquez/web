

import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flask_bootstrap import Bootstrap
from flask_moment import Moment


DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION   = '.md'


app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route ("/")
def index():
    return render_template('index.html', pages=pages)



@app.route("/<path:path>/")
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)




@app.route('/tag/<string:tag>/')
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    else:
        app.run(debug=True, port=8000)