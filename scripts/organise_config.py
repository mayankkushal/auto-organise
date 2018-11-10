DOC = "Document"
VIDEO = "Video"
IMG = "Image"
# OTHERS = "Others"
APP = "Application"

# Keep `OTHERS` at the end
files_type_list = [DOC, VIDEO, APP, IMG]

file_type_dict = {
    'doc': DOC,
    'docx': DOC,
    'ppt': DOC,
    'pptx': DOC,
    'pdf': DOC,
    'txt': DOC,
    '3gp': VIDEO,
    'mp4': VIDEO,
    'jpeg': IMG,
    'png': IMG,
    'gif': IMG,
    'jpg': IMG,
    "deb": APP,
    "py": APP
}