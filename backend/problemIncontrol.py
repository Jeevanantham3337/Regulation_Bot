def process(llm,input):

    regulation=input.split('Controls:')[0]
    controls=input.split('Controls:')[1]

    prompt=f'''Review the provided controls in relation to the given regulation and identify any issues or gaps. Focus on whether the controls meet the specific requirements of the regulation and suggest any improvements if needed.

                Regulation: This Regulation applies to high-risk AI systems that have been placed on the market or put into service before the regulation's application date, only if these systems undergo significant changes in their design or purpose after that date.

                Controls: The bank has set up an AI Ethics and Compliance Committee to ensure that high-risk AI systems comply with regulations. The committee's duties include identifying high-risk AI systems, managing risks, ensuring compliance with guidelines, conducting regular risk assessments, and providing training for staff.

                Example Response: The controls set by the bank do not clearly address how to monitor and evaluate pre-existing AI systems for significant changes in their design or purpose, which is a key requirement of the regulation. The controls should include steps to assess these systems regularly and ensure they comply with the regulation if they undergo such changes.

                Regulation:{regulation} 
                Controls: {controls}

                Response:  '''
    
    res=llm.generate([prompt])
    res_text = res.generations[0][0].text
    return res_text