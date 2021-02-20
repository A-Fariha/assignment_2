from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)


@app.route('/index')
def aboutpage():
    return render_template("index.html")

@app.route('/about')
def homepage():
    return render_template("about.html")


@app.route('/', defaults = {'name': " "})
@app.route('/<name>')
def mainpage(name):
    return render_template("index.html", name= name)


@app.route('/submit', methods = ['GET'])
def submit():
    if request.method == 'GET':
        sl = request.args['NAME']
        sw = request.args['EMAIL']
        pl = request.args['MOBILE']
        Al = request.args['COMMENT']
        print("    "+sl+"    "+sw+"    "+pl+"      "+Al)
        return redirect(url_for('mainpage', name = "    "+sl+"    "+sw+"    "+pl+"   "+Al))
    else:
        return redirect(url_for('mainpage'))



if __name__ == '__main__':
    app.run(debug = True)