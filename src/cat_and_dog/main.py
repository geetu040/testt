import numpy as np
import tensorflow as tf
import io, base64, requests

model_path = "./src/cat_and_dog/model_85.9.h5"
"""
This Model has an accuracy of 85.9%
"""

model = tf.keras.models.load_model(model_path)

def predict(img_data, img_url):
	try:
		if img_url == None:
			content = img_data.replace(" ", "+")
			converted = bytes(content, "utf-8")
			img = base64.decodebytes(converted)
		else:
			img = requests.get(img_url).content

		img = io.BytesIO(img)
		img = tf.keras.preprocessing.image.load_img(img, target_size=model.input_shape[1:])
		img = np.array(img)
		img = img.reshape(1, *img.shape)
		img = img / 255.
		pred = model.predict(img)[0, 0]
		pred = float(pred)
		# print(pred)
		return [round(1-pred, 3), round(pred, 3)]
	except Exception as e:
		# print(e)
		return False