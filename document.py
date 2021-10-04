"""

document.py:

Currently able to hide .txt and .xls files into an image file.

"""
import PIL as pillow
from PIL import Image
import binascii
import optparse
import sys
from os import path

DELIMITTER = '1111111111111110'
SUB_DELIMITTER = '1110111011101110'

""" Converts RGB to Hex

This function takes the current value of the red, green and blue
pixels of the image and converts them to hex values.

"""
def rgb_to_hex(red, green, blue):

    return '#{:02x}{:02x}{:02x}'.format(red, green, blue)

""" Converts Hex to RGB

This function takes the hexcode and convert it back to RGB values.

This is done by removing the "#" sign from the hex value to filter
out each RGB color through the tuple to ensure that each pixel gets
their correct value to before inserting the binary message.

"""
def hex_to_rgb(hexcode):

    hex_values = hexcode.lstrip('#')
    rgb_values = tuple(int(hex_values[i:i+2], 16) for i in (0, 2, 4))
    return rgb_values[0], rgb_values[1], rgb_values[2]

""" Converts String to Binary

This function converts String values to Binary for processing.

When this function receives the message from the hide() function,
it converts the message into hex in case 16. Then, it transforms
the values into integer followed by changing the integer to a
binary string. Thereafter, return the binary string without '0b'
appended at the beginning.

"""
def string_to_binary(message):

    message = str(message)
    binary_array = [bin(ord(x))[2:].zfill(8) for x in message]
    binary_message = ""
    element = 0
    while element < len(binary_array):
        binary_message += binary_array[int(element)]
        element += 1
    return binary_message

""" Converts Binary to String

This function converts Binary to String for processing.

This function takes the binary message and converts it to ASCII by
first converting the binary values into an integer, followed by
converting the integer to its equivalent ASCII and then returning
the message to the calling function.

"""
def binary_to_string(binary):
    message = binascii.unhexlify('%x' % (int('0b'+binary, 2)))
    message = (str(message).lstrip('b').replace("'", "").strip('"'))
    return message

""" Encodes the Hex values 

This function takes in the Hex values and check its range.

This function takes the Hex value of each pixel and check if it is
within the range of 0 to 5. If so, it adds the current digit of the
binary message to the hexcode variable and returns the current pixel
that has the desired hex value of 0 to 5. If the hexcode variable is
not between 0 to 6, nothing will be returned to the calling function.

"""
def encode(hexcode, digit):

    if hexcode[-1] in ('0', '1', '2', '3', '4', '5'):
        hexcode = hexcode[:-1] + digit
        return hexcode
    else:
        return None

""" Decodes the Hex values 

This function takes in the Hex values and returns either 0 or 1.

This function takes each Hex value and returns either 0 or 1 to the
extract() function to be stored in the digit variable.

"""
def decode(hexcode):

    if hexcode[-1] in ('0', '1'):
        return hexcode[-1]
    else:
        return None

""" Hides the input file into an image 

This function takes in the file name, user input, and binary value of
the file to be hidden.

"""
def hide(filename, user_input, filename_binary):
    
    # Converts string to binary and add delimiter
    if filename_binary == None:
        binary = string_to_binary(user_input) + DELIMITTER
    else:
        binary = user_input + DELIMITTER + filename_binary + SUB_DELIMITTER
    
    # Open the image and set it to a variable (img) and send the message
    # text from the main function to string_to_binary() function and the results
    # to the binary variable.
    img = Image.open(filename)
        
    if img.mode in ('RGBA'):
        img = img.convert('RGBA')
        datas = img.getdata()

        newData = []
        digit = 0
        temp = ''
        for item in datas:
            if (digit < len(binary)):

                # Go through the entire length of binary message using
                # the digit variable. Each digit of the binary message
                # is stored. The rgb_to_hex() function will be called
                # which will then call the encode() function to store
                # the hidden file in the image

                newpix = encode(rgb_to_hex(item[0], item[1], item[2]), binary[digit])

                # If the encode() function returns None, the current hex value
                # is more than 5. If such is the case, append the pixel to the
                # newData array

                if newpix == None:

                    # Take values from the newpixe variable from the encode
                    # funciton and call hex_to_rgb() function to restore their
                    # RGB values and make all the values to RGBA format
                    # and make increments to the digits variable

                    newData.append(item)
                else:

                    # When the digits variable exceeds the length of the
                    # binary message, append the remaining pixels to the
                    # item variable until the end of the data variable
                    # for the entire file to be hidden

                    r, g, b = hex_to_rgb(newpix)
                    newData.append((r, g, b, 255))
                    digit += 1

            else:
                newData.append(item)

        # After the loop is completed and the data is stored for each available pixel,
        # store the altered pixels in the newData variable and saves the file and
        # display a completion message.

        img.putdata(newData)
        img.save(filename, "PNG")
        return "\nCompleted!\n"

    return "Error, unable to hide the selected file in the image!\n"


""" Extracts the input file from an image 

This function takes in the file name, user input, and binary value of
the file to be hidden.

"""
def extract(filename, retrieve):

    # Open the altered file and store it into the img variable

    img = Image.open(filename)
    binary = ''
    
    text = 1
    file = 2

    # Check if the image in RGBA format

    if img.mode in ('RGBA'):

        # Convert the image to RGB and store it in the img variable and store
        # the values in the datas variable in a sequence that does not alter
        # the appearance of the image

        img = img.convert('RGBA')
        datas = img.getdata()

        for item in datas:

            # Conver the pixels to Hex values and take the last value of each
            # pixel if it is either 0 or 1 and assign it to the digit variable.
            # If the digit is None, move on to the next pixel.

            digit = decode(rgb_to_hex(item[0], item[1], item[2]))
            if digit == None:
                pass
            else:
                binary = binary + digit

                if retrieve == text:
                    if (binary[-16:] == DELIMITTER):
                        print("\nSuccess!\n")
                        return binary_to_string(binary[:-16])
                
                elif retrieve == file:
                    if (binary[-16:] == SUB_DELIMITTER):
                        start = binary.find(DELIMITTER) + len(DELIMITTER)
                        end = binary.find(SUB_DELIMITTER)
                        filename_binary = binary[start:end]
                        filename = binary_to_string(filename_binary)
                        file_index = len(DELIMITTER) + len(SUB_DELIMITTER) + len(filename_binary)
                        file_content = (binary_to_string(binary[:-(file_index)])).split('\\n')
                        with open(filename, "w") as out:
                            for line in file_content:
                                print(line, file=out)
                        return "\nSuccess!\n"
                       
                        
    return "Error, unable to retrieve the hidden file!\n"

if __name__ == '__main__':

    print("####################################################################\n")
    print("!Hides documents into cover object (tested with .jpg)!\n")
    print("Please ensure that files used are in the same directory!\n")
    print("File types supported: .txt, .xls\n")
    print("####################################################################\n")

    # Prints out a menu for user input

    print("\n1. Hide data")
    print("\n2. Extract data")
    userInput = int(input("\nPlease select an option: "))

    if (userInput == 1):

        filename = input("\nPlease enter the file name that you wish to hide the data in: ")

        infile = input("\nPlease enter the name of the file you wish to hide: ")

        if path.exists(infile):
           
            with open(infile, 'rb') as out:
                    message = out.read()
           
            binary_message = string_to_binary(message)
            filename_binary = string_to_binary(infile)
           
            print(hide(filename, binary_message, filename_binary))

        else:
            print("\nThis is not a valid file. Please check the filename or directory path and restart the program.\n")
          
    elif(userInput == 2):

        filename = input("\nPlease enter the file name that you wish to extract the data from: ")
        retrieve = 2
       
        print(extract(filename, retrieve))

    else:
        print("\nInvalid option selected! Program exiting...")
        exit(0)

