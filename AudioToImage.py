import cv2
import numpy as np
import os


# convert data into binary
def to_bin(data):
    """Convert 'data to binary format as string"""
    if isinstance(data, str):
        return ''.join([format(ord(i), "08b") for i in data])
    elif isinstance(data, bytes) or isinstance(data, np.ndarray):
        return [format(i, "08b") for i in data]
    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b")
    else:
        raise TypeError("Type not supported!")

def audio_to_bin(data): #converts bytes read from audio file into binary format as string
    if isinstance(data, bytes) or isinstance(data, np.ndarray):
        return ''.join([format(i, "08b") for i in data])

def encode_audio(image_name, secret_data, num_of_lsb):
    image = cv2.imread(image_name)  # read the image
    # print("This is image bits: ", image)
    n_bytes = image.shape[0] * image.shape[1] * 3 // 8  # maximum bytes to encode
    print("[*] Maximum bytes to encode:", n_bytes)
    secret_data += bytes("=====",'utf-8')
    if len(secret_data) > n_bytes:
        raise ValueError("[!] Insufficient bytes, need bigger image or less data.")
    print("[*] Encoding data...")
    ###############
    lsb=num_of_lsb
    ##############
    data_index = 0
    binary_secret_data = audio_to_bin(secret_data)  # convert data to binary
    if lsb>1:
        binary_secret_data += (lsb-len(binary_secret_data)%lsb) * "0" #Padding data with 0 to match LSB replacement if >1
    data_len = len(binary_secret_data)  # size of data to hide
    for row in image:
        for pixel in row:
            r, g, b = to_bin(pixel)  # convert RGB values to binary format
            if data_index < data_len:  # modify the Least significant bit only if there is still data to store
                pixel[0] = int(r[: -lsb] + binary_secret_data[data_index: data_index+lsb], 2)  # Least significant red pixel bit
                data_index += lsb
            if data_index < data_len:
                pixel[1] = int(g[: -lsb] + binary_secret_data[data_index: data_index+lsb], 2)  # Least significant green pixel bit
                data_index += lsb
            if data_index < data_len:
                pixel[2] = int(b[: -lsb] + binary_secret_data[data_index: data_index+lsb], 2)  # Least significant blue pixel bit
                data_index += lsb
            if data_index >= data_len:  # if data is encoded, just break out of the loop
                break
    print("[*] Encoded!")
    return image

def main():
    num_of_lsb=input("Type in number of LSB: ")
    with open("sample.wav", 'rb') as audio: #open and read audio file
        msg = audio.read()
    image = "secret.png" #de
    if os.path.exists(image): #if file alr exists in current directory, delete it
        os.remove(image)

    img = encode_audio("500kb.jpg", msg, int(num_of_lsb)) #declare img to encode into

    cv2.imwrite("secret.png", img)

if __name__ == "__main__":
    main()
