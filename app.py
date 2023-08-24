from flask import Flask,request

app=Flask(__name__)
def get_args():
    args=request.args
    print(args.get('n1'))
    n1=int(args.get("n1"))
    n2=int(args.get("n2"))
    return n1,n2

@app.route("/square/<n>")
def print_square(n):
    n=int(n)

    return f'<h1>square of {n} is {n*n}</h1>'

@app.route("/add")
def print_add():
    print("hii")
    print(request.args)
    x=get_args()
    
    return f'<h1>Addition of {x[0]} and {x[1]} is {x[0]+x[1]}</h1>'

@app.route("/sub")
def print_sub():
    x=get_args()
    return f'<h1>Addition of {x[0]} and {x[1]} is {x[0]-x[1]}</h1>'

@app.route("/mult")
def print_mult():
    x=get_args()
    return f'<h1>Addition of {x[0]} and {x[1]} is {x[0]*x[1]}</h1>'

@app.route("/div")
def print_div():
    x=get_args()
    return f'<h1>Addition of {x[0]} and {x[1]} is {x[0]//x[1]}</h1>'

@app.route('/')
def print_hello():
    return '<h1>Hello World Ryan Reynolds</h1>'

if __name__=="__main__":
    
    app.run(debug=True)
