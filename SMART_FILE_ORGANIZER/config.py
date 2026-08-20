FILE_CATEGORIES = {

    "Images": [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".webp",
        ".svg"
    ],

    "Documents": [
        ".pdf",
        ".doc",
        ".docx",
        ".txt",
        ".ppt",
        ".pptx",
        ".xls",
        ".xlsx",
        ".csv"
    ],

    "Videos": [
        ".mp4",
        ".mkv",
        ".avi",
        ".mov",
        ".wmv"
    ],

    "Audio": [
        ".mp3",
        ".wav",
        ".aac",
        ".flac",
        ".m4a"
    ],

    "Archives": [
        ".zip",
        ".rar",
        ".7z",
        ".tar",
        ".gz"
    ],

    "Code": [
        ".py",
        ".java",
        ".cpp",
        ".c",
        ".js",
        ".html",
        ".css",
        ".sql",
        ".json"
    ]
}


def get_category(extension):
    """
    Return the category for a file extension.
    """

    extension = extension.lower()

    for category, extensions in FILE_CATEGORIES.items():

        if extension in extensions:
            return category

    return "Others"