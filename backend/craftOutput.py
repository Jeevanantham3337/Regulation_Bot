
def generateControl(llm,user_input):
    
    prompts=f'''
            "I have a Input that lacks clarity and readability. 
            Please rewrite it in a more elegant and easily understandable way, enhancing its flow and structure while retaining the original meaning.
            Do not include any detail other than context.
            Do not include given input in your response."
            Input:{user_input}
            '''
    
    res=llm.generate([prompts])
    res_text=res.generations[0][0].text
    return res_text