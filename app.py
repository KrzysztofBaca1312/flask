from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/mypage/contact', methods=['GET', 'POST'])
def message():
    if request.method == 'GET':
        print("We received GET")
        return render_template("contact.html")
    elif request.method == 'POST':
        print("We received POST")
        print(request.form)
        return render_template("about.html")
        