import cv2
import numpy as np
import os
import sys
import tensorflow as tf

from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    #➡️INPUT 
    # the data_dir is a directory with folders after each category (0-42). Inside each of this folders are a bunch of images.

    #🔀COMPUTATIONS
    # Use cv2 to read each image as a numpy.ndarray
    # Resize each image to have the width and height equal to IMG_WIDTH, IMG_HEIGHT
    images=[]
    labels=[]
    #1️⃣ Loop over each directory.
    for item in os.listdir(data_dir):
        # Join the folders inside the directory to make a path:
        category_path = os.path.join(data_dir, item)

        #2️⃣ Check if this item is actually a directory before processing
        if os.path.isdir(category_path):
            # List the image files inside this category directory
            image_files = os.listdir(category_path)

            for image_file in image_files:
                #get the path to the image directly
                image_path = os.path.join(category_path, image_file)
                image = cv2.imread(image_path)

                #3️⃣ check image size and resize it.
                if image.shape != (30,30,3):
                    image = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT))
                
                images.append(image)
                labels.append(int(item))
    
    #print(images, labels) 
    return(images, labels)

    #⏩OUTPUT
    # Return a tuple (images, label). 
    # images should be a list of all of the images in the data set, where each image is represented as a numpy.ndarray of the appropriate size. 
    # labels should be a list of integers, representing the category number for each of the corresponding images in the images list.

    # Platform independence
    #Your function should be platform-independent: that is to say, it should work regardless of operating system. 
    # Note that on macOS, the / character is used to separate path components, while the \ character is used on Windows. 
    # Use os.sep and os.path.join as needed instead of using your platform’s specific separator character.


def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    model = tf.keras.models.Sequential([

        # First convolutional block
        tf.keras.layers.Conv2D(
        32, (3,3),activation="relu", input_shape=(30,30,3)
        ),
        tf.keras.layers.MaxPooling2D((2,2)),

        # Second convolutional block
        tf.keras.layers.Conv2D(64, (3,3), activation="relu"),
        tf.keras.layers.MaxPooling2D((2,2)),
        
        # Third convolutional block 
        tf.keras.layers.Conv2D(128, (3,3), activation="relu"),
        tf.keras.layers.MaxPooling2D((2,2)),

        # Flatten before dense layers
        tf.keras.layers.Flatten(),

        # First dense hidden layer
        tf.keras.layers.Dense(512, activation="relu"),
        tf.keras.layers.Dropout(0.5),
        
        # Second dense hidden layer 
        tf.keras.layers.Dense(256, activation="relu"),
        tf.keras.layers.Dropout(0.4),

        # Third dense hidden layer 
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dropout(0.3),

        tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
    ])

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model


if __name__ == "__main__":
    main()
