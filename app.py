from flask import Flask, Response
import getpass
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Tushar Sanjeev Shinde"
    user = getpass.getuser()
    time_ist = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    time_ist_str = time_ist.strftime("%Y-%m-%d %H:%M:%S.%f")

    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1'], stderr=subprocess.STDOUT).decode()
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"

    output = f"""Name: {name}
user: {user}
Server Time (IST): {time_ist_str}
TOP output:

{top_output}
"""
    return Response(output, mimetype='text/plain')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
