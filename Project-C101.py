import dropbox

class DataTransfer:
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFiles(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = "oh1UloYZsMcAAAAAAAAAAT7jORAcaVLlnHCDRM3zis4V9MMJlLOwEkouimG0v810"
    transferData = DataTransfer(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload the files in the dropbox: ")

    transferData.uploadFiles(file_from, file_to)

    print("File has been moved")

main()
