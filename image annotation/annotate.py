import cv2 as cv
import matplotlib.pyplot as plt


# Load image
img = cv.imread('../images/29.jpg')

# Convert to rgb for plotting in matplotlib
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.figure(figsize=(8, 6))
plt.imshow(rgb_img)
plt.show()


# Annotation
img_copy = rgb_img.copy()

cv.rectangle(img_copy, (15, 75), (105, 105), (255, 0, 0), 1)
cv.rectangle(img_copy, (15, 65), (40, 75), (255, 0, 0), -1)
cv.putText(img_copy, 'car', (15, 73),
           cv.FONT_HERSHEY_COMPLEX, 0.3, (0, 0, 0), 1)

cv.rectangle(img_copy, (105, 50), (175, 180), (0, 255, 0), 1)
cv.rectangle(img_copy, (105, 40), (140, 50), (0, 255, 0), -1)
cv.putText(img_copy, 'person', (105, 46),
           cv.FONT_HERSHEY_COMPLEX, 0.3, (0, 0, 0), 1)


plt.figure(figsize=(8, 6))
plt.imshow(img_copy)
plt.show()
