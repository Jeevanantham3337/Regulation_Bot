from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

import model
import classify
import generate_control
import missing_control
import checkFrequency
import craftOutput
import problemIncontrol
# run the model
llm = model.run()

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generateControls")
async def chat(request: ChatRequest):
    user_message = request.message
    response_message = classify.process_content(llm, user_message)
    if response_message.strip()!='No':
        control=generate_control.generateControl_chat(llm,user_message)
        prompt=f'Input:{user_message} "response":{response_message} ", The given context contains obligations.","control":{control}'
        # response=craftOutput.generateControl(llm,prompt)
        return {"response":response_message+", The given context contains obligations and Following is the control for given obligations: "+control}
    
    return {"response":response_message+", The given context does not contain obligations"}

@app.post("/missingControls")
async def missingControl(request:ChatRequest):
    user_message = request.message
    # response_message = classify.process_content(llm, user_message)
    response_message='No'
    if response_message.strip()!='No':
        control=generate_control.generateControl_chat(llm,user_message)
        input=user_message+"Control:"+control
        res=missing_control.missingControl(llm,input)
        return {"response":"Obligation:"+user_message+"Generated Controls"+control+"\nMissing controls:"+res}
    
    
    # prompt=f'obligations:{user_message},Missing controls:{res}'
    # response=craftOutput.generateControl(llm,res)
    res=missing_control.missingControl(llm,user_message)
    return {"response":res}

@app.post('/checkfrequency')
async def checkfrequency(request:ChatRequest):
    user_message=request.message
    response_message = classify.process_content(llm, user_message)

    if response_message.strip()=='No':
        return {"response":"The given content doesn't contain obligations"}
    
    response_message=checkFrequency.process_content(llm,user_message)

    return {'response':response_message}

@app.post('/problemIncontrol')
async def problemInControl(request:ChatRequest):
    user_message=request.message
    response_message=classify.process_content(llm, user_message)

    if response_message.strip()=='No':
        return {"response":"The given content doesn't contain obligations"}
    
    response_message=problemIncontrol.process(llm,user_message)

    return {"response":response_message}


