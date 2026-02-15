import torch
import gradio as gr


# pipeline as a high level helper
from transformers import pipeline
# pipe = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

model_path = "../Models/models--sshleifer--distilbart-cnn-12-6/snapshots/a4f8f3ea906ed274767e9906dbaede7531d660ff"
text_summary = pipeline("summarization", model=model_path, dtype=torch.bfloat16)


text='''Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language. Python 3.0, released in 2008, was a major revision and not completely backward-compatible with earlier versions. Beginning with Python 3.5,[34] capabilities and keywords for typing were added to the language, allowing optional static typing.[35] As of 2026, the Python Software Foundation supports Python 3.10, 3.11, 3.12, 3.13, and 3.14, following the project's annual release cycle and five-year support policy. Python 3.15 is currently in the alpha development phase, and the stable release is expected to come out in October 2026."[36] Earlier versions in the 3.x series have reached end-of-life and no longer receive security updates.'''
print(text_summary(text))

def summary(input):
    output = text_summary(input)
    return output[0]['summary_text']

gr.close_all()

demo = gr.Interface(fn = summary,
                    inputs = [gr.Textbox(label="Input text for summarization",lines=6)],
                    outputs = [gr.Textbox(label="Output summarized text",lines=4)],
                    title = "BroBish Project Text Summarizer",
                    description = "You can use the application to summarize the text")
demo.launch()
