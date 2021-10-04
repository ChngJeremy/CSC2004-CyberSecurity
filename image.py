"""

image.py:

Hides a secret image file into a carrier image file.

Takes in JPG and outputs PNG

"""

from PIL import Image

# CONSTANTS
MAX_COLOR_VALUE = 255
MAX_BIT_VALUE = 8

# Helper Methods
def remove_n_least_significant_bits(value, n):
    value = value >> n 
    return value << n

def get_n_least_significant_bits(value, n):
    value = value << MAX_BIT_VALUE - n
    value = value % MAX_COLOR_VALUE
    return value >> MAX_BIT_VALUE - n

def get_n_most_significant_bits(value, n):
    return value >> MAX_BIT_VALUE - n

def shit_n_bits_to_8(value, n):
    return value << MAX_BIT_VALUE - n

""" Creates a PIL Image Object

This function takes in the matrix and resolution of an image and converts it
into a PIL image object.

"""
def create_PIL_image(data, resolution):

    image = Image.new("RGB", resolution) # Create a new Image object
    image.putdata(data) # Put data matrix (pixels) into the Image object

    return image

""" Encodes an image

This function encodes an image and returns it as an PIL image object.

"""
def encode(secretImage, carrierImage, n_bits):
    
    # Gets resolution of carrier image
    width, height = carrierImage.size
    
    # Gets the object that has the pixel data of the secret and carrier image
    secret_image = secretImage.load() 
    carrier_image = carrierImage.load()

    # Variable to store values of each individual pixel as a matrix
    data = []
    
    # Loop through the carrier image
    for y in range(height):
        for x in range(width):

            try:

                # Gets 'n' most significant bits of RGB values of image to hide
                r_hide, g_hide, b_hide= secret_image[x,y]
                r_hide = get_n_most_significant_bits(r_hide, n_bits)
                g_hide = get_n_most_significant_bits(g_hide, n_bits)
                b_hide = get_n_most_significant_bits(b_hide, n_bits)
                
                # Remove least 'n' significant bits of image to hide in, 
                # to store the 'n' most significant bits in that position
                r_hide_in, g_hide_in, b_hide_in= carrier_image[x,y]
                r_hide_in = remove_n_least_significant_bits(r_hide_in, n_bits)
                g_hide_in = remove_n_least_significant_bits(g_hide_in, n_bits)
                b_hide_in = remove_n_least_significant_bits(b_hide_in, n_bits)

                
                data.append((r_hide + r_hide_in, 
                             g_hide + g_hide_in,
                             b_hide + b_hide_in))

            # Exception handling
            except Exception as e:
                print(e)

    # return an Image object from the above data.
    return create_PIL_image(data, secretImage.size)

""" Decodes an image

This function decodes an image and returns it as an PIL image object.

"""
def decode(image_to_decode, n_bits):
    
    # Gets resolution of the image to be decoded
    width, height = image_to_decode.size

    # Gets the object that has the pixel data of the image to be decoded
    encoded_image = image_to_decode.load()

    # Variable to store values of each individual pixel as a matrix
    data = []

    # Looping through the image to be decoded
    for y in range(height):
        for x in range(width):

            # Gets RGB values of the image to be decoded
            r_encoded, g_encoded, b_encoded = encoded_image[x,y]

            # Get 'n' least significant bits for each RGB value of the image to be decoded
            r_encoded = get_n_least_significant_bits(r_encoded, n_bits)
            g_encoded = get_n_least_significant_bits(g_encoded, n_bits)
            b_encoded = get_n_least_significant_bits(b_encoded, n_bits)
            
            # Shift 'n' bits to the right so that they occupy a total of 8 bit spaces
            r_encoded = shit_n_bits_to_8(r_encoded, n_bits)
            g_encoded = shit_n_bits_to_8(g_encoded, n_bits)
            b_encoded = shit_n_bits_to_8(b_encoded, n_bits)

            data.append((r_encoded, g_encoded, b_encoded))
            
    return create_PIL_image(data, image_to_decode.size)




if __name__ == '__main__':

    # Sets the number of bits to be shifted
    n_bits = 2

    print("####################################################################\n")
    print("!Hides an image into another image and outputs as PNG!\n")
    print("Please ensure that files used are in the same directory!\n")
    print("File types supported: .jpg\n")
    print("####################################################################\n")

    # Prints out a menu for user input
    print("\n1. Hide data")
    print("\n2. Extract data")
    userInput = int(input("\nPlease select an option: "))

    encoded_image_path = "./encoded.png"
    decoded_image_path = "./decoded.png"
    
    if (userInput == 1):

        carrierImage_path = input("\nPlease enter the file name that you wish to hide the data in: ")
        secretImage_path = input("\nPlease enter the name of the file you wish to hide: ")
        
        secretImage = Image.open(secretImage_path)
        carrierImage = Image.open(carrierImage_path)

        # Create a copy of the image to hide with the same resolution as the carrier image
        secretImage = secretImage.resize(carrierImage.size)
        
        encode(secretImage, carrierImage, n_bits).save(encoded_image_path)

        print("\nEncoding successful! \n")
        print("Path: ", encoded_image_path)

    if (userInput == 2):

        carrierImage = input("\nPlease enter the file name that you wish to extract the data from: ")

        image_to_decode = Image.open(carrierImage)

        decode(image_to_decode, n_bits).save(decoded_image_path)

        print("\nDecoding successful! \n")
        print("Path: ", decoded_image_path)