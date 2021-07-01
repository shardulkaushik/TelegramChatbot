#!flask/bin/python
from flask import Flask
from flask import request, jsonify
from chatflow.validate_chatflow import ValidateChatflow

app = Flask(__name__)


@app.route('/uploadChatflow/', methods=['POST'])
def upload_chatflow():
    flow_file = request.files.get('chatflow')
    if flow_file:
        validate_chatflow = ValidateChatflow(file_instance=flow_file)
        return jsonify({'message':'SUCCESS', 'data': validate_chatflow.to_json()}), 201
    return jsonify({'message':'Chatflow was not attached.', 'data': None}), 400

if __name__ == '__main__':
    app.run(debug=True)