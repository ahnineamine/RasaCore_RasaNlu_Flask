# # Part-1:Add Natural Language understanding(create NLU  model)

import nlu_server
import core_server
import logging
import os
from flask import Flask
from flask import request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
api = Api(app)


##################### Building NLU Model ####################
logging.info("Training NLU model")

nl = nlu_server.NluServer()
nl.build_nlu()

logging.info("NLU model runs successfuly")

##################### Building Core Model ###################

logging.info("Training CORE model")

cs = core_server.CoreServer()
cs.build_core()

logging.info("CORE model runs successfuly")

##################### Build API ##############################
#@app.route("/conversations/default/respond",methods=['POST'])
@app.route("/response/default/conversations",methods=['POST'])
@cross_origin()
def run_hr_bot():
    # calling rasa agent
    agent = cs.agent
    ## Collect Query from POST request
    data = request.get_json(force=True)
    print(data)
    ## Send Query to Agent
    responses=agent.handle_text(data)
    ## Get Response of BOT
    #for response in responses:
        #return jsonify(response['text'])
    return jsonify(responses)

if __name__ == '__main__':
    #port = int(os.environ.get("PORT", 5005))
    app.run(host='0.0.0.0',port=5005,debug=True)
