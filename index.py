from flask import Flask,render_template,request
import recommend as rc

app = Flask('__name__')

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/result', methods = ['GET','POST'])
def result():
    if request.method == 'GET':
       movie_name = str(request.args.get('find'))
       list = rc.movieList(movie_name)
       return render_template("moviename.html", lists = list)

if __name__ == '__main__':
    app.run(debug=True, port=5050)
