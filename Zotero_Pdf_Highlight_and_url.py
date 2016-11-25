# -*- coding: utf-8 -*-
# import clipboard from ahk format as %Page%###%Title%###%texthh%


# retrieve the clipboard sent by Ahk  : should be done with win32clipboard instead ot tkinter?
from tkinter import Tk
root = Tk()
root.withdraw()
clipboard_from_ahk = root.clipboard_get()

# 
clipboard_from_ahk_splitted = clipboard_from_ahk.split('###')


#store page number and text highlighted
Pdf_Page_number= clipboard_from_ahk_splitted[0]
Text_Highlighted=clipboard_from_ahk_splitted[2]

#store the title of the .pdf (only keep the part before .pdf :   mypdf.pdf - Adobe Acrobat Pro  )
Title_with_extension= clipboard_from_ahk_splitted[1]
Title_splitted= Title_with_extension.split('.pdf')
Title= Title_splitted[0]

print("Page : ", Pdf_Page_number)
print("Title : ", Title)

import os
import time
import shutil

date_time = time.strftime("_%d_%m_%Y") + time.strftime("_%H_%M_%S")
path_to_zotero_sqlite = 'C:\\Users\xxx\\Desktop\\xxx\\Zotero (online DB)\\zotero.sqlite'
path_to_folder_for_copy_zotero_sqlite = 'C:\\Users\\xxx\\Desktop\\zotero_copy'+ date_time
path_to_COPY_zotero_sqlite = path_to_folder_for_copy_zotero_sqlite + '\\zotero' + date_time + '.sqlite'

if not os.path.exists(path_to_folder_for_copy_zotero_sqlite):
    os.makedirs(path_to_folder_for_copy_zotero_sqlite)
shutil.copy2(path_to_zotero_sqlite, path_to_COPY_zotero_sqlite)

# search in zotero.sqlite for itemID  of the open PDF with the title of the pdf
import sqlite3
db = sqlite3.connect(path_to_COPY_zotero_sqlite)
cursor = db.cursor()
cursor.execute('SELECT itemID FROM itemAttachments WHERE path LIKE ?', ('%{}%'.format(Title), ))
print("\nfetch one:")
itemID_list = cursor.fetchone() 
print(itemID_list)
itemID = itemID_list[0]
print(itemID)


# search in zotero.sqlite for folder name from the itemID
cursor.execute('SELECT key FROM items WHERE itemID =? ', (itemID,))
print("\nfetch one:")
foldername_list = cursor.fetchone() 
print(foldername_list)
foldername=foldername_list[0]


#send 
pdf_direct_link= ("zotero://open-pdf/0_" + foldername + "/" + Pdf_Page_number)
all_data_for_clipboard=(Text_Highlighted+pdf_direct_link)
print(pdf_direct_link)

# send to clipbaord with HTML format



import HtmlClipboard
HtmlClipboard.PutHtml("<p>" + Text_Highlighted + "<span>[<a href=\""+pdf_direct_link+"\" target=\"_blank\">"+Pdf_Page_number+"</a>]  </p>")

if HtmlClipboard.HasHtml(): fragment = HtmlClipboard.GetHtml()
#print(fragment)


# delete folder shutil.rmtree(path_to_folder_for_copy_zotero_sqlite) doesn'T work because folder+file still acces by python -


input("exit")






