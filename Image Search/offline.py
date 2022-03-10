from PIL import Image
from feature_extractor import FeatureExtractor
from pathlib import Path
import numpy as np
import urllib
from mongodbUtils import MongoDbHandler


def downloadImage(filename, imageLink):
    path = "static/img/" + filename + ".jpg"
    imagefile = open(path, 'wb')
    imagefile.write(urllib.request.urlopen(imageLink).read())
    imagefile.close()


def fetchImagesFromDb():
    """Fetch all images from database and extract their features to match with"""

    # establish database connection
    dbUsername = ""
    dbPassword = ""
    databaseName = ""
    mongodb = MongoDbHandler()
    mongodb.connectDb(dbUsername, dbPassword, databaseName)

    collection = "products"
    productsList = mongodb.findAll(collection)

    for product in productsList:
        title = product["title"]            # get product title
        imageLink = product["imageLink"]    # get image link of the product

        print("Saving.... ")
        print(title)
        print(imageLink)
        print("\n")
        downloadImage(title, imageLink)     # save image in flask server side


if __name__ == '__main__':
    fetchImagesFromDb()

    fe = FeatureExtractor()

    for img_path in sorted(Path("./static/img").glob("*.jpg")):
        print(img_path)  # e.g., ./static/img/xxx.jpg
        feature = fe.extract(img=Image.open(img_path))
        # e.g., ./static/feature/xxx.npy
        feature_path = Path("./static/feature") / (img_path.stem + ".npy")
        np.save(feature_path, feature)
