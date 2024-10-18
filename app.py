from flask import Flask, jsonify, render_template
from platform import system, version, release, machine, architecture, node, python_version
import requests
import psutil
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/cpu')
def cpu():
    cpu_info = {
        'Physical cores': psutil.cpu_count(logical=False),
        'Total cores': psutil.cpu_count(logical=True),
        'CPU usage per core': dict(enumerate(psutil.cpu_percent(percpu=True, interval=1))),
        'CPU frequency': psutil.cpu_freq().current,
        'Total CPU usage': psutil.cpu_percent(interval=1)
    }
    return jsonify(cpu_info)


@app.route('/platform')
def platform():
    platform_info = {
        'Operating System': system(),
        'OS version': version(),
        'OS release': release(),
        'Machine': machine(),
        'Platform Architecture': architecture()
    }
    return jsonify(platform_info)

@app.route('/system-info')
def system_info():
    info = {
        'OS': system(),
        'OS Version': version(),
        'Architecture': architecture(),
        'Machine': machine(),
        'Node': node(),
        'Python Version': python_version()
    }
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
