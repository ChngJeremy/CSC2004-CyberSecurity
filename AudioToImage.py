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

def encode_audio(image_name, secret_data):
    image = cv2.imread(image_name)  # read the image
    # print("This is image bits: ", image)
    n_bytes = image.shape[0] * image.shape[1] * 3 // 8  # maximum bytes to encode
    print("[*] Maximum bytes to encode:", n_bytes)
    secret_data += bytes("=====",'utf-8')
    if len(secret_data) > n_bytes:
        raise ValueError("[!] Insufficient bytes, need bigger image or less data.")
    print("[*] Encoding data...")

    data_index = 0
    binary_secret_data = audio_to_bin(secret_data)  # convert data to binary
    data_len = len(binary_secret_data)  # size of data to hide
    for row in image:
        for pixel in row:
            r, g, b = to_bin(pixel)  # convert RGB values to binary format
            if data_index < data_len:  # modify the Least significant bit only if there is still data to store
                pixel[0] = int(r[: -1] + binary_secret_data[data_index], 2)  # Least significant red pixel bit
                data_index += 1
            if data_index < data_len:
                pixel[1] = int(g[: -1] + binary_secret_data[data_index], 2)  # Least significant green pixel bit
                data_index += 1
            if data_index < data_len:
                pixel[2] = int(b[: -1] + binary_secret_data[data_index], 2)  # Least significant blue pixel bit
                data_index += 1
            if data_index >= data_len:  # if data is encoded, just break out of the loop
                break
    print("[*] Encoded!")
    return image
# def audio_decode(image_name): #doesnt work :(
#     print("[+] Decoding...")
#     # read the image
#     image = cv2.imread(image_name)
#     binary_data = ""
#     for row in image:
#         for pixel in row:
#             r, g, b = to_bin(pixel)
#             binary_data += r[-1]
#             binary_data += g[-1]
#             binary_data += b[-1]
#     # split by 8-bits
#     all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8)]
#     # convert from bits to characters
#     audio = []
#     for byte in all_bytes:
#         audio.append(byte)
#         if audio[-5:] == to_bin(bytes("=====", 'utf-8')):
#             break
#     audio = audio[: -5]
#     decoded_audio = bytearray()
#     for i in range(len(audio)):
#         # audio[i]=bin(int(audio[i],2))
#         decoded_audio.extend((int(audio[i], 2)).to_bytes(2, byteorder='big'))
#     print(decoded_audio)
#     ##need to convert audio from a list of string-binary back into bytearray##
#     # nAudio=bytes(decoded_audio)
#     # newAudio = wave.open('decodedStego.wav', 'wb')
#     # newAudio.setparams(nAudio.getparams())
#     # newAudio.writeframes(nAudio)
#     #
#     # newAudio.close()

def main():
    with open("sample.wav", 'rb') as audio: #open and read audio file
        msg = audio.read()
    image = "secret.png" #de
    if os.path.exists(image): #if file alr exists in current directory, delete it
        os.remove(image)

    img = encode_audio("500kb.jpg", msg) #declare img to encode into

    cv2.imwrite("secret.png", img)

if __name__ == "__main__":
    main()
