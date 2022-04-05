"""
Example code for uploading and retrieving an image from a server
"""

from tkinter import filedialog
import base64
import requests

server = "http://vcm-21170.vm.duke.edu"
# server = "http://127.0.0.1"


def upload_image_driver():
    """
    This function calls the necessary functions for uploading an image file
    to a server.  First, it calls a function to get the filename of the image
    to upload.  Second, it calls a function to convert that file to a base64
    string.  Third, it calls a function that makes a post request to the server
    to send the base64 string.
    """
    filename = get_filename_image()
    b64_string = convert_file_to_b64_string(filename)
    answer = send_b64_string_to_server(b64_string)


def convert_file_to_b64_string(filename):
    """
    This function receives the name of a file that contains an image.  It then
    opens that file for reading as a binary file.  The data is read in and
    encoded into base64 bytes using the "base64" Python package.  These base64
    bytes are then converted into a base64 string which is returned to the
    calling function.  This code is taken from the Image Toolbox in the BME 547
    class repository.
    """
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string


def send_b64_string_to_server(b64_string):
    """
    This function makes a post request to the image server.  See the server
    API at
    "https://github.com/dward2/BME547/blob/main/Lectures/
        image_encoding_decoding.md#server-api"
    """
    out_json = {"image": b64_string, "net_id": "jc895", "id_no": 27}
    r = requests.post(server + "/add_image", json=out_json)
    print(r.status_code)
    print(r.text)
    return r.text


def get_filename_image():
    """
    This function uses the tkinter filedialog package to ask the user for a
    file name.
    """
    filename = filedialog.askopenfilename()
    return filename


def save_image_from_server():
    """
    This function makes a request to the image server to download the images
    from the server.  If the request is successful, it asks the user for a
    filename and then calls a function to save the image to a file.
    """
    r = requests.get(server + "/get_image/jc895/27")
    if r.status_code != 200:
        print(r.text)
        return False
    else:
        new_filename = filedialog.asksaveasfilename()
        save_base64_string_to_file(r.text, new_filename)


def save_base64_string_to_file(b64_str, filename):
    """
    This function converts a base64 string into a binary file on the computer.
    This code is taken from the Image Toolbox.
    """
    image_bytes = base64.b64decode(b64_str)
    with open(filename, "wb") as out_file:
        out_file.write(image_bytes)


if __name__ == '__main__':
    upload_image_driver()
    save_image_from_server()
