from flask import Flask, request, abort
import monobank

app = Flask(__name__)



MONO_TOKEN = 'u8PI0F5SA36yJrCPaWamBEGsTFjyrZWdkyRbIgYf_Ltk'
mono = monobank.Client(MONO_TOKEN)
mono.create_webhook('http://127.0.0.1:8000')

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        #if request.json['data']['account'] == '7dxOnvxACiayZfZzNvs6fA':
        print(request.json)
        return 'success', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
