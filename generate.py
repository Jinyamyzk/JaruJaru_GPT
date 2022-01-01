import torch
from transformers import AutoModelForCausalLM, T5Tokenizer
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-medium")
tokenizer.do_lower_case = True
model = AutoModelForCausalLM.from_pretrained('GPT-2/output/')
model.to(device)
model.eval()

def generate_yatu(text, num_gen):
    input_text = text
    input_ids = tokenizer.encode(input_text, return_tensors='pt').to(device)
    out = model.generate(input_ids, do_sample=True, top_p=0.95, top_k=40, 
                         num_return_sequences=num_gen, max_length=64, bad_words_ids=[[1], [5]])
    
    for sent in tokenizer.batch_decode(out):
        sent = sent.replace('</s>', '')
        if "奴" in sent:
            print(sent)

if __name__ == "__main__":
    text = input()
    generate_yatu(text, 30)