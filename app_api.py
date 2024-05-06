# Import libraries
from flask import Flask, jsonify, request
import openai

# Set your OpenAI API key
client = openai.OpenAI(api_key="your openai gpt key")
fine_tuned_model_id = "your fine tuned llm id"

# Initialize your flask app
app = Flask(__name__)


def customLLM(user_input_question, fine_tuned_model_id):
    system_prompt = "You are an ecommerce assistant with the purpose of taking customers questions and providing them with relevant response. Customers can report incidents, request services, seek guidance, or seek assistance. You only respond to ecommerce related questions. Do not respond to questions not related to ecommerce."
    completion = client.chat.completions.create(
        model=fine_tuned_model_id,
        messages=[{"role": "system", "content": system_prompt}, 
                {"role": "user", "content": user_input_question}, ]
    )

    # Response from the fine tuned model
    return completion.choices[0].message.content


@app.route("/llmchatbot", methods=['GET', 'POST'])
def index_view():
    """
    
    """
    username = request.args.get('userchat')
    chatbot_response = customLLM(username, fine_tuned_model_id)
    return jsonify(chatbot_response=chatbot_response, status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)