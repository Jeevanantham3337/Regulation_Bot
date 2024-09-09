from langchain_community.llms import LlamaCpp 
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler 
# import llama_cpp

def run():
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    llm = LlamaCpp(
        model_path="instructlab-granite-7b-lab-Q4_K_M.gguf",
        # do_sample=True,
        temperature=0.4,  
        max_tokens=600,   
        top_p=1,         
        top_k=50,        
        n_ctx=1024,
        callback_manager=callback_manager,
        verbose=True,
    )
    return llm