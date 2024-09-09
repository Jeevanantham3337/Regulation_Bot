
import pandas as pd

obligation_yes_no=[]
def process(llm):
    df = pd.read_csv("obligation.csv")

    data = df['Section_Content']
    # print(data[1])
    count=0
    for d in data:
        prompt = f'''
        Please respond with either "Yes" if the following content contains any obligations for organizations orelse "No"
        
        Note:Your response should be just "Yes" or "No" without any explanation.
        Please do not include any other detail.
        Example:
        1.Question:For high-risk AI systems that are safety components of products or systems, or which are themselves products or systems, falling within the scope of the following acts, only Article 84 of this Regulation shall apply:
        Response:"Yes"
        
        2.Question:This Regulation shall not apply to public authorities in a third country nor to international organisations falling within the scope of this Regulation pursuant to paragraph 1, where those authorities or organisations use AI systems in the framework of international agreements for law enforcement and judicial cooperation with the Union or with one or more Member States.
        Response:"Yes"

        Question: {d}

        '''

        # Generate the response
        response = llm.generate([prompt])
        
        # Extract the text from the response if needed (adjust this according to the actual output structure)
        res_text = response.generations[0][0].text

        print(res_text)
        # if res_text.lower().startswith("Yes"):
        #     res_text = "Yes"
        # elif res_text.lower().startswith("No"):
        #     res_text = "No"
        # else:
        #     res_text = "No" 
        obligation_yes_no.append(res_text)
        count+=1

    df['obligation']=obligation_yes_no
        
    df.to_csv('content_classified.csv')

def process_content(llm,content):
    prompt = f'''
        "You are a language model tasked with identifying obligations for organizations in a given text. Please respond with either 'Yes' only if the following content contains any obligations for organizations, or 'No' if it does not. Do not provide any additional explanations or responses beyond 'Yes' or 'No.'
        Content:

        {content}

        Response:"

        '''

    # Generate the response
    response = llm.generate([prompt])
    
    # Extract the text from the response if needed (adjust this according to the actual output structure)
    res_text = response.generations[0][0].text

    return res_text.split(',')[0]


    
