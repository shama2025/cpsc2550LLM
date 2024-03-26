from huggingface_hub import hf_hub_download
from llama_cpp import Llama
import requests

def run_inference(prompt,query,llm_select):
    print("llm_select type: ", type(llm_select))
    print("Value of llm_select: ", llm_select)
    models = {
        "Repo_ID" : "TheBloke/Llama-2-7B-Chat-GGUF", "filename": "llama-2-7b-chat.Q4_K_M.gguf" , "model_backend": "llama",
        "Repo_ID" : "N/A" , "filename" :"N/A" , "model_backend": "api_endpoint",
        "Repo_ID" : "TheBloke/NeuralBeagle14-7B-GGUF" , "filename":"neuralbeagle14-7b.Q3_K_M.gguf" , "model_backend": "llama",
    }
    print("Length of dictionary: ", len(models))
    if llm_select == 2:
        try:
                print("Working api endpoint")
                host = "http://10.73.56.27"
                response = requests.get(f"{host}/api", stream=True, params={
                "max_tokens": 350,
                "model": "openchat-3.5-0106",
                "input": f"GPT4 Correct User: {prompt}"
                        f"<|end_of_turn|>GPT4 Correct Assistant:{query}"
            })
             
                response.encoding="utf8"

                content = ''

                for text in response.iter_content(decode_unicode=True):
                    content += text

                return content

        except ValueError as e:
            print("Error: ", e)
    elif llm_select == 1 or llm_select == 3:  
            try:
                print("Working llama")
                model_path = hf_hub_download(repo_id=models["Repo_ID"][llm_select], 
                                    filename=models["filename"][llm_select])
        
                llm = Llama(model_path=model_path)
                output = llm(f"User:{prompt}\n"
                            f"Assistant: {query}.",max_tokens=350)

                return output["choices"][0]["text"]
            except ValueError as e:
                print("Error: ", e)
