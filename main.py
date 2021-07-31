from flask import Flask # Import Flask Class
from waitress import serve
app = Flask(__name__) # Create an Instance
from transformers import pipeline
summarizer = pipeline("summarization")
@app.route('/<var>') # Route the Function
def main(var): # Run the function with an arg 'var'
  if(var[:24] == "1OXCr3Bdg9dGb+GMBAT6Bg=="):
    return { "text": summarizer(var[24:], max_length=130, min_length=30, do_sample=False)[0].get("summary_text")}
  else:
    return "not authorized"

if __name__ == "__main__":
  serve(app, host="0.0.0.0", port=8080)