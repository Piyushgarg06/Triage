from fastapi import UploadFile, File
import os 

image_extensions = [
    '.jpg', '.jpeg', '.jpe', '.jif', '.jfif', '.pjpeg', '.pjp', 
    '.png', '.apng',                                             
    '.bmp',                                                       
    '.tiff', '.tif',                                              
    '.webp',                                                      
    '.svg',
    '.ico', '.cur',
    '.avif',
    '.heif', '.heic',                                             
    '.raw', '.cr2', '.nef', '.orf', '.sr2'                        
]

doc_extensions = [
    '.pdf',
    '.doc', '.docx',                                              
    '.txt',
    '.rtf',                                                       
    '.odt',                                                       
    '.md',                                                        
    '.ppt', '.pptx',                                              
    '.xls', '.xlsx',
    '.csv'                                                        
]
valid_extensions = image_extensions + doc_extensions

def validate_file(file: UploadFile):
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in valid_extensions:
        return {"valid": False, "error": f"Invalid file extension: {ext}"}
    return {"valid": True}
