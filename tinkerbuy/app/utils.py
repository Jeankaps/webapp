import os
from werkzeug.utils import secure_filename
from flask import current_app

# Function to upload files
def upload_file(file, folder):
    # Get the filename
    filename = secure_filename(file.filename)

    # Get the upload folder path
    upload_folder = os.path.join(current_app.config['UPLOAD_FOLDER'], folder)

    # Create the upload folder if it doesn't exist
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    # Save the file
    file.save(os.path.join(upload_folder, filename))

    # Return the filename
    return filename

# Function to delete files
def delete_file(filename, folder):
    # Get the file path
    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], folder, filename)

    # Delete the file
    if os.path.exists(file_path):
        os.remove(file_path)