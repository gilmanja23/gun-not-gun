import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image



# Recreate the exact same model, including its weights and the optimizer
new_model = tf.keras.models.load_model('/home/cole/github/gun-not-gun/models/model1.h5')

# Show the model architecture
new_model.summary()

# Load and preprocess a single image
img_path = '/home/cole/Desktop/random.jpg'
img = image.load_img(img_path, target_size=(112, 112)) # resize to match model input size
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0) # add batch dimension
img_array = img_array / 255.0 # normalize pixel values

# Pass the preprocessed image to your model for prediction
predictions = new_model.predict(img_array)

# Print the predicted outputs
print("Preds----------------------------")
print(predictions)

predicted_class = np.argmax(predictions, axis=1)
if predicted_class == 0:
    print("Its a gun")
else:
    print("Not a gun")