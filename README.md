# Test case for Firefox: 

Tested on Python 3.5 
1) Save HtmlClipboard.py in the Lib\site-packages\ folder of your Pyton installation
2) Run Debugging_Firefox.py
3) Paste what the script put in your clipboard in different HTML editors: you can use http://www.quackit.com/html/online-html-editor/

Then edit these lines in HtmlClipboard.py (around 277) to see how the bug can be fixed:
change 

  fragmentEnd = (fragmentStart + len(fragment))

to 

  fragmentEnd = (fragmentStart + len(fragment)) +1000


and 

  selectionEnd = (selectionStart + len(selection)) 

to 

  selectionEnd = (selectionStart + len(selection)) +1000

