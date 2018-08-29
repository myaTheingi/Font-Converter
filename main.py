from flask import Flask , render_template , request , jsonify
import zg2uni
import uni2zg
import win2uni
import uni2win

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dropdown')
def dropdown():
    return render_template('dropdown.html')

@app.route("/convert1", methods=["POST"])
def convert1():
    myinput = request.form['myinput']
    myinput = zg2uni.convert(myinput)
    myoutput = myinput
    if myinput:
        return jsonify({'myoutput': myoutput})
    return jsonify({'myoutput': "Please write text in textarea"})

@app.route('/dropdown2')
def dropdown2():
    return render_template('dropdown2.html')

@app.route("/convert2", methods=["POST"])
def convert2():
    myinput = request.form['myinput']
    myinput = zg2uni.convert(myinput)
    myinput = uni2win.convert(myinput)
    myoutput = myinput
    if myinput:
        return jsonify({'myoutput': myoutput})
    return jsonify({'myoutput': "Please write text in  textarea"})
@app.route('/dropdown3')
def dropdown3():
    return render_template('dropdown3.html')

@app.route("/convert3", methods=["POST"])
def convert3():
    myinput = request.form['myinput']
    myinput = win2uni.convert(myinput)
    myoutput =myinput
    if myinput:
        return jsonify({'myoutput': myoutput})
    return jsonify({'myoutput': "Please write  text in  textarea"})
@app.route('/dropdown4')
def dropdown4():
    return render_template('dropdown4.html')

@app.route("/convert4", methods=["POST"])
def convert4():
    myinput = request.form['myinput']
    myinput = win2uni.convert(myinput)
    myinput = uni2zg.convert(myinput)
    myoutput = myinput
    if myinput:
        return jsonify({'myoutput': myoutput})
    return jsonify({'myoutput': "Please write text in  textarea"})
@app.route('/dropdown5')
def dropdown5():
    return render_template('dropdown5.html')

@app.route("/convert5", methods=["POST"])
def convert5():
    myinput = request.form['myinput']
    myinput = uni2win.convert(myinput)
    myoutput = myinput
    if myinput:
        return jsonify({'myoutput': myoutput})
    return jsonify({'myoutput': "Please write  text in  textarea"})
@app.route('/dropdown6')
def dropdown6():
    return render_template('dropdown6.html')

@app.route("/convert6", methods=["POST"])
def convert6():
    myinput = request.form['myinput']
    myinput = uni2zg.convert(myinput)
    myoutput = myinput
    if myinput:
        return jsonify({'myoutput': myoutput})
    return jsonify({'myoutput': "Please write text in textarea"})
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/Answer')
def Answer():
    return render_template('Answer.html')

@app.route('/mytable')
def mytable():
    return render_template('mytable.html')

@app.route('/Question')
def Question():
    return render_template('Question.html')

@app.route('/read')
def read():
    return render_template('read.html')

if __name__ == '__main__':
    app.run(debug=True)
