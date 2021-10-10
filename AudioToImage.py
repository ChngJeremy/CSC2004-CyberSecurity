#import ffmpy ##NOT USED
import soundfile as sf
import numpy as np
import cv2
from PIL import Image
import RGBAImg2img as img

##NOT USED##
# def mp3towav(src, dest):
#     ff = ffmpy.FFmpeg(
#         inputs={src: None},
#         outputs={dest: None})
#     ff.run()
#
#
# def wavtomp3(src, dest):
#     ff = ffmpy.FFmpeg(
#         inputs={src: None},
#         outputs={dest: None})
#     ff.run()
#
#
# def openmp3(filename):
#     with open(filename, 'rb') as f:
#         while f.readable():
#             print(f.read(1))
##NOT USED##

def audiotoimage(filename):
    data, samplerate = sf.read(filename, dtype='int16')
    # print(len(data))
    #
    # print(data[66149])
    #
    # print(samplerate)

    npdata = np.array(data)
    npdatat = npdata.transpose()

    channel1 = npdatat[0]
    channel2 = npdatat[1]

    def paddingzeroesattheend(array, no):
        arr = []
        i = 0
        while (i <= no):
            arr.append(0)
            i = i + 1

        array = np.append(array, arr)
        return array

    length = len(channel1)
    square = length ** (0.5)

    if (square > int(square)):
        square = int(square) + 1

    #print(square)

    channel1 = paddingzeroesattheend(channel1, ((square * square) - len(channel1) - 1))
    channel2 = paddingzeroesattheend(channel2, ((square * square) - len(channel2) - 1))

    channel1 = np.array(channel1)
    channel2 = np.array(channel2)

    channel1 = channel1 + 32768
    channel2 = channel2 + 32768

    channel1front = channel1 / 256
    channel1end = channel1front - channel1front.astype(int)
    channel1end = channel1end * 256

    channel1front = channel1front.astype(int)
    channel1end = channel1end.astype(int)

    channel2front = channel2 / 256
    channel2end = channel2front - channel2front.astype(int)
    channel2end = channel2end * 256

    channel2front = channel2front.astype(int)
    channel2end = channel2end.astype(int)

    d2channel1front = np.reshape(channel1front, (square, square))
    d2channel1end = np.reshape(channel1end, (square, square))
    d2channel2front = np.reshape(channel2front, (square, square))
    d2channel2end = np.reshape(channel2end, (square, square))

    allchannel = [d2channel1front, d2channel2front, d2channel1end, d2channel2end]

    allchannel = np.array(allchannel)

    allchannel = np.transpose(allchannel)
    #print(allchannel)

    cv2.imwrite("tmpIMG/encodedImage.png", allchannel, [cv2.IMWRITE_PNG_COMPRESSION, 9])

    print("[+] Audio converted to Image!")

def imagetoaudio(filename, outputdes):
    img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

    allchannel = np.array(img)

    allchannel = np.transpose(allchannel)

    d2channel1front = np.array(allchannel[0])

    d2channel2front = np.array(allchannel[1])

    d2channel1end = np.array(allchannel[2])

    d2channel2end = np.array(allchannel[3])

    channel1front = np.reshape(d2channel1front, (1, -1))
    channel1front = np.array(channel1front[0])
    channel1end = np.reshape(d2channel1end, (1, -1))
    channel1end = np.array(channel1end[0])
    channel2front = np.reshape(d2channel2front, (1, -1))
    channel2front = np.array(channel2front[0])
    channel2end = np.reshape(d2channel2end, (1, -1))
    channel2end = np.array(channel2end[0])

    channel1 = (channel1front * 256 + channel1end)
    channel2 = (channel2front * 256 + channel2end)

    channel1 = channel1.astype(int)
    channel2 = channel2.astype(int)

    channel1 = channel1 - 32768
    channel2 = channel2 - 32768

    data = [channel1, channel2]

    data = np.array(data)
    data = np.transpose(data)

    data = data[0:14467107]

    npdata = data.astype('int16')

    sf.write(outputdes, npdata, 44100)


def main():
    #Get wav/mp3,audio2img
    #use img2img to do LSB
    #use img2img to decode LSB
    #use img2audio to get back audio


    #############
    ##ENCODING##
    ############
    ##User input to select number of bits
    n_bits=int(input("Type in number of LSB: "))
    #Payload file for encoding (User select in GUI)
    filepath='sample.wav'

    print("[+] Converting audio to image...")
    audiotoimage(filepath)
    print("[+] Audio converted into image!")

    #secret.png is the final product of encoding
    encoded_image_path = "./secret.png"
    #Leave this path hardcoded
    decoded_image_path = "tmpIMG/decodedImage.png"

    #Carrier file for encoding (User select in GUI)
    carrierImage_path = "mkt.jpg"

    #Leave this path hardcoded
    secretImage_path = "tmpIMG/encodedImage.png"

    secretImage = Image.open(secretImage_path)

    #!!Need to keep this as a variable for the decoding part later!!!!!!!!!!!!!!!!!!
    originalSize=secretImage.size
    ################################################################################

    #convert carrier file to RGBA format
    carrierImage = Image.open(carrierImage_path).convert('RGBA')
    secretImage = secretImage.resize(carrierImage.size)
    print("[+] Encoding to image....")
    img.encode(secretImage, carrierImage, n_bits).save(encoded_image_path)
    print("[+] Encoded!")

    #############
    ##DECODING##
    ############
    #change carrier image path to secret.png for decoding
    print("[+] Extracting secret audio from image...")

    #Can make this path user select in GUI
    carrierImage = "./secret.png"
    image_to_decode = Image.open(carrierImage)


    img.decode(image_to_decode, n_bits).save(decoded_image_path)
    print("[+] Secret audio(image) extracted from image!")
    print("[+] Converting secret audio back to .wav...")
    #Resize upscaled image back to original size
    #Opens the decoded image, resize back to how it was before encoding, then save it back to file
    Image.open(decoded_image_path).resize(originalSize).save(decoded_image_path)

    #extracted.wav is the final product from decoding
    imagetoaudio(decoded_image_path,"extracted.wav")
    print("[+] Converted!")

#All paths under tmpIMG/xxx can leave hardcoded, won't be touched by user at all
#secret.png and extracted.wav are the final output files

if __name__ == '__main__':
    main()
