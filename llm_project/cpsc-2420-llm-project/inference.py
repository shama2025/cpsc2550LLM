from huggingface_hub import hf_hub_download
from llama_cpp import Llama

def run_inference(prompt):
    try:
        prompt = prompt
        model_path = hf_hub_download(repo_id="TheBloke/Llama-2-7B-Chat-GGUF", 
                                filename="llama-2-7b-chat.Q4_K_M.gguf")
    
        llm = Llama(model_path=model_path)
        output = llm(f"User:{prompt}\n"
                "Assistant: You are a middle schooler who has depression and will be replying as if you are a client of a therapists.")

        return output["choices"][0]["text"]
    except ValueError as e:
        print("Error: ", e)
    

