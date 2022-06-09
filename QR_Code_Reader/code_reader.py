import cv2 as cv
import matplotlib.pyplot as plt


def qr_code_reader(filename):
    """
    Given a file path to a QR Code image, 
    read the content of the code, detects the QR code
    area and draws a blue bounding box around it
    """
    try:
        img = cv.imread(filename)

        decoder = cv.QRCodeDetector()
        text, bbox, straitqr = decoder.detectAndDecode(img)
        if bbox is not None:
            print('QR Code Detected')
            print(f'Encoded text : {text}')
            bbox = bbox.squeeze().astype(int)
            for i in range(len(bbox)):
                next_pt_idx = (i + 1) % len(bbox)
                cv.line(img, tuple(bbox[i]), tuple(
                    bbox[next_pt_idx]), (0, 0, 255), 2)
            plt.figure(figsize=(8, 8))
            plt.imshow(img)
            plt.show()
    except:
        print('QR Code Not Detected!!!')


# Read the QR Code
qr_code_reader('../images/qr_code.png')
