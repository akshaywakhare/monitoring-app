import psutil
from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    cpu_p=psutil.cpu_percent()
    memory_p=psutil.virtual_memory().percent
    mem=psutil.virtual_memory().total
    Message=None

    if cpu_p > 80 or memory_p > 80:
      Message = "CPU or Memory limit reached. Please scale up"

    return render_template("index.html",cpu_p=cpu_p,memory_p=memory_p,message=Message)

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0')
