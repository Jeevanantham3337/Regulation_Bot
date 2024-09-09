def missingControl(llm,user_input):
    missingControl=[]
    input=user_input.split('Control:')
    instruction = 'can you find part of the Regulation is missing from given Control?'    
        
    prompts = prompt = f"""
    You are a language model specialized in compliance and regulatory analysis. 
    Your task is to analyze the obligation and the provided controls and identify if any controls are missing, and clearly list those missing controls only.
    List missing controls only. 
    Obligation:
    "{input[0]}"

    Provided Controls:
    "{input[1]}"

    Response: Please identify and list any missing controls that are needed to fully comply with the given obligation."""
    res=llm.generate([prompts])
    res_text = res.generations[0][0].text
    return res_text