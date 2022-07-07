from flask import Flask, request, abort
import monobank
import os

app = Flask(__name__)


MONO_TOKEN = 'u8PI0F5SA36yJrCPaWamBEGsTFjyrZWdkyRbIgYf_Ltk'
mono = monobank.Client(MONO_TOKEN)


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        #if request.json['data']['account'] == '7dxOnvxACiayZfZzNvs6fA':
        print(request.json)
        return 'success', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', default=8000), debug=True)
    mono.create_webhook('https://monobank-webhook.herokuapp.com/webhook')
