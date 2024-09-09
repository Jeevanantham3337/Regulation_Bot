import pandas as pd

def generateControl(llm):

    df = pd.read_csv('content_classified.csv')

    df = df[df['obligation']=='Yes']

    controls=[]

    for d in df['obligation']:
        prompt=f'''
                Can you generate appropriate control for following obligation?
                obligation:{d}
                '''
        res=llm.generate([prompt])
        res_text = res.generations[0][0].text
        
        controls.append(res_text)

def missingControl(llm):
    missingControl=[]
    obligation_control=pd.read_csv()

    for i in range(len(obligation_control)):
        instruction = 'Which part of the Regulation is missing from the Control?'    
        
        prompts = f"""{instruction} 
                'Regulation:' {obligation_control['obligation'].iloc[i]}
                'Control:' {obligation_control['controls'].iloc[i]}
                """
        
        res=llm.generate([prompts])
        res_text = res.generations[0][0].text
        missingControl.append(res_text)


def generateControl_chat(llm,input):

    
    prompt=f'''
            Task: Generate complete and appropriate controls for the following obligation.

            Example Obligation:
            "As regards paragraphs 1, point (d) and 2, each individual use for the purpose of law enforcement of a real-time remote biometric identification system in publicly accessible spaces shall be subject to a prior authorisation granted by a judicial authority or by an independent administrative authority of the Member State in which the use is to take place, issued upon a reasoned request and in accordance with the detailed rules of national law referred to in paragraph 4. However, in a duly justified situation of urgency, the use of the system may be commenced without an authorisation and the authorisation may be requested only during or after the use."

            Response:
            Controls:

            - The bank identifies and categorizes AI systems based on their risk level, with high-risk systems being subject to the most stringent controls.
            - The bank establishes a dedicated AI ethics committee to oversee the development, implementation, and ongoing monitoring of high-risk AI systems.
            - The AI ethics committee performs regular risk assessments on high-risk AI systems, evaluating potential risks to individuals and society, and ensuring that appropriate mitigations are in place.
            - The bank implements robust testing and validation procedures for high-risk AI systems, including thorough unit testing, integration testing, and user acceptance testing.

            Obligation:
            {input}

            Response:
            '''
    res=llm.generate([prompt])
    res_text = res.generations[0][0].text
    
    return res_text