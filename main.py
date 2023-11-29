import qrcode
import cv2

def encode_qr_code(data, filename):
    """
    Encode data into a QR code and save it as an image file.

    Parameters:
    - data: The data to be encoded into the QR code.
    - filename: The filename (with extension) to save the QR code image.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def decode_qr_code(image_path):
    """
    Decode a QR code from an image file.

    Parameters:
    - image_path: The path to the QR code image.

    Returns:
    - The decoded data from the QR code.
    """
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    retval, decoded_info, points, straight_qrcode = detector.detectAndDecodeMulti(img)

    if retval:
        decoded_data = decoded_info[0]
        return decoded_data
    else:
        return None

# Example Usage:

# Encode data and save as QR code image
data_to_encode = "https://web.ncf.ca/andersonm/23F-NET2000-010/"
output_filename = "encoded_qr_code.png"
encode_qr_code(data_to_encode, output_filename)
print(f"QR Code encoded and saved as {output_filename}")

# Decode QR code from image
input_filename = "encoded_qr_code.png"
decoded_data = decode_qr_code(input_filename)

if decoded_data:
    print(f"Decoded data from QR Code: {decoded_data}")
else:
    print("Failed to decode QR Code.")
