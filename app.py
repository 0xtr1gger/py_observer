from flask import Flask, jsonify, render_template
from platform import system, version, release, machine, architecture, processor
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
    cpu = processor()
    if cpu == '':
        cpu = 'Unknown'
    platform_info = {
        'Operating System': system(),
        'OS version': version(),
        'OS release': release(),
        'Machine': machine(),
        'Platform Architecture': architecture(),
        'Platform processor': cpu
    }
    return jsonify(platform_info)

@app.route('/system-info')
def system_info():
    info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.architecture(),
        "Machine": platform.machine(),
        "Node": platform.node(),
        "Processor": platform.processor(),
        "Python Version": platform.python_version(),
        "Environment Variables": dict(os.environ)
    }
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)
