from flask import Flask, request, render_template
import openai

app = Flask(__name__)

# Use OpenAI API Key
openai.api_key = "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"


@app.route("/")
def index():
    return render_template(("index.html"))


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=userText,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1,
    )
    answer = response["choices"][0]["text"]

    return str(answer)


if __name__ == "__main__":
   #  app.run(host="127.0.0.1", port=5001, debug=True)
    app.run()
