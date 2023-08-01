from transformers import pipeline

model = pipeline("text-generation", model = "gpt2")

sentence = model("Hello, my name is mittesh, I'm from india", do_sample=True, top_k=50, temperature=0.9, max_length=100)
for i in sentence:
    print(i["generated_text"])