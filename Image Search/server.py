import numpy as np
from PIL import Image
from feature_extractor import FeatureExtractor
from datetime import datetime
from flask import Flask, request, render_template, jsonify
from pathlib import Path
import tensorflow as tf
import json

app = Flask(__name__)

# gpu_options = tf.GPUOptions(allow_growth=True)
# session = tf.InteractiveSession(config=tf.ConfigProto(gpu_options=gpu_options))

# Read image features
fe = FeatureExtractor()
features = []
img_paths = []
for feature_path in Path("./static/feature").glob("*.npy"):
    features.append(np.load(feature_path))
    img_paths.append(Path("./static/img") / (feature_path.stem + ".jpg"))
features = np.array(features)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # file = request.files['file']
        queryImgs = request.data.decode()
        queryImgs = queryImgs.replace("@,", "@")

        filePaths = queryImgs.split("@")
        print(filePaths)

        # imageNames = []
        # for i in range(len(filePaths)):
        #     imageNames.append(filePaths[i].split("\\")[-1])

        # print("Image Names: ", imageNames)

        searchedImages = []
        for queryImg in filePaths:
            filename = queryImg.split("\\")[-1]

            if filename == "":
                print("")
            else:

                uploaded_img_path = "static/uploaded/" + \
                    datetime.now().isoformat().replace(":", ".") + "_" + filename
                img = Image.open(queryImg)
                img.save(uploaded_img_path)

                # Run search
                query = fe.extract(img)
                # L2 distances to features
                dists = np.linalg.norm(features-query, axis=1)
                ids = np.argsort(dists)[:5]

                newid = []
                for i in ids:
                    if dists[i] < 0.7:
                        print("DISTANCE : ", dists[i])
                        newid.append(i)

                scoresWithImgPath = [(dists[id], img_paths[id])
                                     for id in newid]

                # scores = [img_paths[id] for id in ids]
                # print("Scores: ", scoresWithImgPath)

                for img in scoresWithImgPath:
                    pathStr = img[1].__str__()
                    imagename = pathStr.split("\\")[-1]
                    searchedImages.append(imagename)

                print("Searched Images: ", searchedImages)

                # return render_template('index.html',
                #                        query_path=uploaded_img_path,
                #                        scores=scoresWithImgPath)

        matchedProducts = {
            "images": searchedImages
        }

        return matchedProducts

        # Save query image
        # img = Image.open(file.stream)  # PIL image
        # uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":",
        #                                                                             ".") + "_" + file.filename
        # img.save(uploaded_img_path)

        # uploaded_img_path = "static/uploaded/" + \
        #     datetime.now().isoformat().replace(":", ".") + "_" + filename
        # img = Image.open(queryImg)
        # img.save(uploaded_img_path)

        # return "Flask Server"
    else:
        # return render_template('index.html')
        return "Flask Server"


if __name__ == "__main__":
    app.run("127.0.0.1")
