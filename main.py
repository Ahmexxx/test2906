from fastapi import FastAPI,Depends,HTTPException,status
from pydantic import BaseModel
from starlette.responses import JSONResponse
import joblib
import uvicorn
app = FastAPI(title="API Startup", description="with FastAPI by Ahmed Ibrahim", version="1.0")
class StartupData(BaseModel):
    rdspend: float =73721
    administration: float =121344
    marketing: float =211025


@app.on_event("startup")
def startup_event():
    "modello *.pkl di ML"
    global model # la varibile dovrà essere globale
    model = joblib.load("Startup.pkl")
    print(" MODEL LOADED!!")
    return model

                                        #####GET########
@app.get("/")
def home():
    return {" ---->          http://localhost:8000/docs     <----------"}



@app.get("/predict")
async def predictget(data:StartupData=Depends()):
    try:
        X = [[data.rdspend, data.administration, data.marketing]]
        y_pred = model.predict(X)[0]
        res = round(y_pred,2)
        return {'result':res}
    except:
        raise HTTPException(status_code=404, detail="error")
    

                                        #####POST########

@app.post("/predict")
async def predictpost(data:StartupData):
    try:
        X = [[data.rdspend, data.administration, data.marketing]]
        y_pred = model.predict(X)[0]
        res = round(y_pred,2)
        return {'result':res}
    except:
        raise HTTPException(status_code=404, detail="error")

 
    
###########


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

