from flask import Flask, make_response, jsonify
from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

app = Flask(__name__)
tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)


@app.route('/api/<message>', methods=['GET'])
def api(message):
    model_predict = model.predict([message], k=2)[0]
    response = {x: y for x, y in filter(lambda x: model_predict[x[0]] == max(model_predict.values()),
                                        model_predict.items())}
    return make_response(jsonify({'response': response}))


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run()
