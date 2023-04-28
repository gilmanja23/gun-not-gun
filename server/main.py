from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import pathlib
from io import BytesIO


app = FastAPI()

# List of allowed origins
origins = [
    "*"
]

# Add the CORS middleware to your FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Recreate the exact same model, including its weights and the optimizer
new_model = tf.keras.models.load_model('../models/model1_inc.h5')
model3 = tf.keras.models.load_model('../models/model3.h5')

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Shelley likes men"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post("/prediction")
def get_prediction(img: UploadFile = File(...)):
    print(img.content_type)
    img_data = img.file.read()
    img_stream = BytesIO(img_data)
    img = image.load_img(img_stream, target_size=(112, 112)) # resize to match model input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) # add batch dimension
    #img_array = img_array / 255.0 # normalize pixel values

    # Pass the preprocessed image to your model for prediction
    predictions = new_model.predict(img_array)

    # Print the predicted outputs
    # print("Preds----------------------------")
    # print(predictions)

    predicted_class = np.argmax(predictions, axis=1)
    if predicted_class == 0:
        print("Gun")
        return {"prediction": "Gun"}
    else:
        print("Not Gun")
        return {"prediction": "Not Gun"}

@app.post("/prediction_model3")
def get_prediction_model3(img: UploadFile = File(...)):
    print(img.content_type)
    img_data = img.file.read()
    img_stream = BytesIO(img_data)
    img = image.load_img(img_stream, target_size=(112, 112)) # resize to match model input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) # add batch dimension
    #img_array = img_array / 255.0 # normalize pixel values

    # Pass the preprocessed image to your model for prediction
    predictions = model3.predict(img_array)

    # Print the predicted outputs
    # print("Preds----------------------------")
    # print(predictions)

    predicted_class = np.argmax(predictions, axis=1)
    if predicted_class == 0:
        print("Gun")
        return {"prediction": "Gun"}
    else:
        print("Not Gun")
        return {"prediction": "Not Gun"}
    