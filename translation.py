from transformers import MarianMTModel, MarianTokenizer

src_text = [
    "ذهب الرئيس پوتن إلى القصر الرئاسي في العاصمة كييڤ",
]

model_name = "Helsinki-NLP/opus-mt-ar-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

translated_text_to_AR = ' '.join([tokenizer.decode(t, skip_special_tokens=True) for t in translated])
print('translated_text_to_AR: ',translated_text_to_AR)
# expected output:
#     Just follow your heart.
#     Wayne Rahi Dosh?

from transformers import MarianTokenizer, MarianMTModel
mname = "marefa-nlp/marefa-mt-en-ar"
tokenizer = MarianTokenizer.from_pretrained(mname)
model = MarianMTModel.from_pretrained(mname)

# English Sample Text
input = translated_text_to_AR

translated_tokens = model.generate(**tokenizer.prepare_seq2seq_batch([input], return_tensors="pt"))
translated_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated_tokens]

# translated Arabic Text
print('translated_text: ',translated_text)
# ذهب الرئيس پوتن إلى القصر الرئاسي في العاصمة كييڤ
