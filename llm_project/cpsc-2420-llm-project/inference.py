from huggingface_hub import hf_hub_download
from llama_cpp import Llama

def run_inference(prompt,query):
    try:
        model_path = hf_hub_download(repo_id="TheBloke/Llama-2-7B-Chat-GGUF", 
                                filename="llama-2-7b-chat.Q4_K_M.gguf")
    
        llm = Llama(model_path=model_path)
        output = llm(f"User:{prompt}\n"
                f"Assistant: {query}.")

        return output["choices"][0]["text"]
    except ValueError as e:
        print("Error: ", e)
