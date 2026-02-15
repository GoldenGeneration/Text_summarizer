This is an open-sourced model.

-> Virtual environment is advised.
-> Required installation is within Installation directory.
    for file directory similar to mine: (pip install -r Installation/requirements.txt)

You can download the main working model by:

    1. Pipeline method.
        from transformers import pipeline
        pipe = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

        Note: downgrading the version of transformers to transformers<5.0.0, i.e. v4.x is necessary.
        command to downgrade -> pip install "transformers<5.0.0"
        (I have used this method).

    2. Load model directly.
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

        tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
        model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")

    or, you can refer to this link: https://huggingface.co/sshleifer/distilbart-cnn-12-6?library=transformers




