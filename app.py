from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  
  {
    'id' : 1,
    'title' : 'Data Analyst',
    'location' : 'Benguluru,India',
    'Salary' : 'Rs. 10,00,000'
  },
  {
    'id' : 2,
    'title' : 'Data Scientist',
    'location' : 'Delhi,India',
    'Salary' : 'Rs. 15,00,000'
    
  },
  {
    'id' : 3,
    'title' : 'front-end Engineer',
    'location' : 'remote',
    'Salary' : 'Rs. 12,00,000'
    
  },
  {
    'id' : 4,
    'title' : 'Back-end Engineer',
    'location' : 'Noida,India'
    
    
  }
]

@app.route("/")
def hello_world():
  return render_template("home.html",jobs=JOBS,
                         Company_name = 'Alok')

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0' ,debug=True)

