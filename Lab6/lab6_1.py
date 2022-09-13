from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def index():
	L = [31,4,23,14,45,87,76,132]
	return render_template('index.html',list=L)


@app.route('/form1', methods=['GET','POST'])
def form1():
	if request.method == 'POST':
		username = request.form['username']
		email =  request.form['email']
		return render_template('info.html',username=username,email=email)
	return render_template('form.html')


@app.route('/form2', methods=['GET','POST'])
def form2():
    if request.method == 'POST':
        ID = request.form['ID']
        fname =  request.form['fname']
        lname =  request.form['lname']
        level =  request.form['level']
        gpa =  request.form['gpa']
        f = open("students.txt", "a+")
        f.write(ID+' '+fname+' '+lname+' '+level+' '+gpa+'\n')
        f.seek(0,0)
        std = f.readlines()
        # print(std)
        # print(f)
        f.close()
        # return render_template('info2.html',std=std)
        return render_template('form2.html',std=std)
    return render_template('form2.html')


if __name__ == '__main__':
	app.run(debug = True)