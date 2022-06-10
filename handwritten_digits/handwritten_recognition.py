import cv2 as cv
import matplotlib.pyplot as plt
import torch
from torchvision import transforms
from model import ConvNet


def load_images(file_pth, show=False):
    """
    given an image file path, loads the image and returns both
    original and gray scale version.
    Optionally plots the gray scale image
    """
    digits_pth = file_pth
    digits = cv.imread(digits_pth)

    gray_digits = cv.cvtColor(digits, cv.COLOR_BGR2GRAY)

    if show:
        plt.figure(figsize=(15, 8))
        plt.imshow(gray_digits, cmap='gray')
        plt.show()

    return digits, gray_digits


def preprocess(img, n_digits, offset=70, thresh=100):
    # binarize image
    _, threshold = cv.threshold(img, thresh, 255, cv.THRESH_BINARY_INV)

    # dilate to better find contours
    dilated = cv.dilate(threshold, (3, 3), iterations=5)

    # find contours
    contours, _ = cv.findContours(
        dilated, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    sorted_contours = sorted(contours, key=cv.contourArea, reverse=True)
    final_contours = sorted_contours[:n_digits]

    # crop out digits from image and resize cropped digits
    cropped_digits = []
    for idx in range(len(final_contours)):
        x, y, w, h = cv.boundingRect(final_contours[idx])

        x = x - offset
        y = y - offset
        w = w + 2*offset
        h = w + 2*offset

        resized_digit = cv.resize(
            dilated[y:y+h, x:x+w], (28, 28), interpolation=cv.INTER_CUBIC)
        cropped_digits.append(resized_digit)

    return cropped_digits


def predict(img):
    # Load model and setup transformation pipeline
    convnet = ConvNet()
    convnet.load_state_dict(torch.load('model.pth'))

    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5), (0.5))
    ])

    convnet.eval()
    with torch.no_grad():
        trsf_digit = transform(img).unsqueeze(0)
        logsoft = convnet(trsf_digit)
        return torch.argmax(logsoft, 1)


def show_digits(cropped_digits):
    string_digits = ''
    for digit in cropped_digits:
        string_digits += str(predict(digit).item())

    print(string_digits)
