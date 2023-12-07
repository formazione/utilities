import cv2

# Load the cascade classifiers for cats and dogs
cat_cascade = cv2.CascadeClassifier('cat.xml')
# dog_cascade = cv2.CascadeClassifier('dog.xml')

# Read the image
img = cv2.imread('cat.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect cats and dogs in the image
cats = cat_cascade.detectMultiScale(gray, 1.1, 3)
# dogs = dog_cascade.detectMultiScale(gray, 1.1, 3)

# Print the number of cats and dogs detected
print("Cats detected: ", len(cats))
# print("Dogs detected: ", len(dogs))
