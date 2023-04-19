import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import pathlib


# Recreate the exact same model, including its weights and the optimizer
new_model = tf.keras.models.load_model('./models/model1_inc.h5')

# Show the model architecture
new_model.summary()

# Load and preprocess a single image
img_path = 'C:/Users/cammi/Downloads/gunModel_Tester'
data_dir = pathlib.Path(img_path)
img_list = list(data_dir.glob('*/*.jpg'))
print(len(img_list))
print('lllllllllllll')
i = 0
img_count = {'gun': 0, 'no gun': 0}
while i < len(img_list):
    img = image.load_img(img_list[i], target_size=(112, 112)) # resize to match model input size
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
        img_count['gun'] = img_count['gun'] +1
    else:
        img_count['no gun'] = img_count['no gun'] +1
    i = i+1
print(img_count)