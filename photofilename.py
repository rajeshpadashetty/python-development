import time, os.path

photofiles=['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']

class BatchRename:
    delimeter = "%"

fmt=input('enter rename style (%d-date %n-seqnum %f-format):')
