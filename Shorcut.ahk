!^+h::             ;Alt(!) CTRL(^) shift(+) AND h
clipboard =
Send, {CTRLDOWN}c{CTRLUP}{ESC}
ClipWait
texthh = %clipboard%
WinGetActiveTitle, Title
ControlGetText, Page, Edit2,  %Title%
clipboard = %Page%###%Title%###%texthh%
ClipWait
Run Highlight_from_pdf_with_url.py, C:\Users\xxx\Desktop
return
