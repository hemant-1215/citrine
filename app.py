import gradio as gr
from transformers import pipeline

# Load the sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

# Define the function to be used in the Gradio interface
def analyze_sentiment(text):
    result = sentiment_analyzer(text)
    return result

# Create the Gradio interface
interface = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(label="Enter Text"),
    outputs=gr.JSON(label="Sentiment Analysis Result"),
    title="Sentiment Analysis",
    description="Enter a piece of text to get the sentiment analysis result."
)

# Launch the Gradio app
if __name__ == "__main__":
    interface.launch()
