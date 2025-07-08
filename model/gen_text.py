from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def generate_text(prompt: str, max_length: int = 100) -> str:
    result = generator(prompt, max_length=max_length, num_return_sequences=1)[0]
    
    return result['generated_text']
