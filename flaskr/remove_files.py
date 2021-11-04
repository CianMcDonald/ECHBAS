import os
import datetime
import time

def main():
    QR_FOLDER = 'static/qrphotos/'
    for f in os.listdir(QR_FOLDER):
            file_path = os.path.join(QR_FOLDER, f)
            if f != "qrdata.png":
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)

main()
