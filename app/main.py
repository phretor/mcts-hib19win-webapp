import os
from flask import Flask, request, render_template
from waitress import serve

app = Flask(__name__)

# config
STEP1_FILE_URL = os.environ.get('STEP1_FILE_URL', '')
FLAG1 = os.environ.get('FLAG1', '')
FLAG2 = os.environ.get('FLAG2', '')
FLAG3 = os.environ.get('FLAG3', '')
PAYLOAD = os.environ.get('PAYLOAD', '')
TX_DELAY = int(os.environ.get('TX_DELAY', '500'))
TX_REPEAT = int(os.environ.get('TX_REPEAT', '16'))
RX_TIMEOUT = int(os.environ.get('RX_TIMEOUT', '10000'))

INTERVAL = '{:.1f}'.format((RX_TIMEOUT + TX_DELAY)/1000.0)


@app.route('/')
@app.route('/step1')
def step1():
    return render_template('step1.html', file_url=STEP1_FILE_URL)


@app.route('/step2', methods=['GET'])
def step2():
    return render_template(
            'step2.html',
            id_len=len(FLAG1),
            interval=INTERVAL)


@app.route('/step2', methods=['POST'])
def solve():
    flag = request.form.get('flag', '')
    step = request.form.get('step', '')

    if step == "step2":
        return step2solve(flag)
    elif step == "step3":
        return step3solve(flag)
    elif step == "step4":
        return step4solve(flag)
    else:
        return render_template(
                'step2.html',
                id_len=len(FLAG1),
                interval=INTERVAL,
                step=step)


def step2solve(flag):
    if flag.strip() != FLAG1:
        return render_template(
                'step2.html',
                id_len=len(FLAG1),
                interval=INTERVAL,
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
                tx_repeat=TX_REPEAT,
                tx_delay='{:.1f}'.format(TX_DELAY/1000.0),
                payload=PAYLOAD)


def step4solve(flag):
    if flag.strip() != FLAG3:
        return render_template(
                'step4.html',
                tx_repeat=TX_REPEAT,
                tx_delay='{:.1f}'.format(TX_DELAY/1000.0),
                payload=PAYLOAD,
                submitted=True)
    else:
        return render_template(
                'step5.html')


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=os.environ.get('FLASK_PORT', 5000))
