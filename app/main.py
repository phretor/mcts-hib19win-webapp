import os
from flask import Flask, escape, request, render_template

app = Flask(__name__)

STEP1_FILE_URL = os.environ.get('STEP1_FILE_URL').strip()
FLAG1 = os.environ.get('FLAG1', '').strip()
FLAG2 = os.environ.get('FLAG2', '').strip()
FLAG3 = os.environ.get('FLAG3', '').strip()
PAYLOAD = os.environ.get('PAYLOAD', '').strip()
SYNCWORD = os.environ.get('SYNCWORD', '').strip()


@app.route('/')
@app.route('/step1')
def step1():
    return render_template('step1.html', file_url=STEP1_FILE_URL)


@app.route('/step2', methods=['GET'])
def step2():
    return render_template('step2.html', oracle=FLAG1)


@app.route('/step2', methods=['POST'])
def solve():
    flag = request.form.get('flag', '')
    step = request.form.get('step', '')

    if step == "step2" and flag:
        return step2solve(flag)
    elif step == "step3" and flag:
        return step3solve(flag)
    elif step == "step4" and flag:
        return step4solve(flag)
    else:
        return render_template(
                'step2.html', step=step)


def step2solve(flag):
    if flag.strip() != FLAG1:
        return render_template(
                'step2.html',
                submitted=True)
    else:
        return render_template(
                'step3.html')


def step3solve(flag):
    if flag.strip() != FLAG2:
        return render_template(
                'step3.html',
                submitted=True)
    else:
        return render_template(
                'step4.html',
                payload=PAYLOAD,
                syncword=SYNCWORD)


def step4solve(flag):
    if flag.strip() != FLAG3:
        return render_template(
                'step4.html',
                payload=PAYLOAD,
                syncword=SYNCWORD,
                submitted=True)
    else:
        return render_template(
                'step5.html')
