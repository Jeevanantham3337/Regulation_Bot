def process_content(llm,content):

    prompt=f'''
                Analyze the following obligation and determine the frequency with which this obligation needs to occur according to the regulation. Provide your answer as a clear and concise statement.
                Options for Frequency - once per year,once per quarter,once in half a year.

                choose one option based on obligation.
                Obligation: Testing procedures shall be suitable to achieve the intended purpose of the AI system and do not need to go beyond what is necessary to achieve that purpose.

                Output Example: Once per quarter.

                Obligation: {content}

                Output:
            '''

    response = llm.generate([prompt])
    
    # Extract the text from the response if needed (adjust this according to the actual output structure)
    res_text = response.generations[0][0].text

    return res_text