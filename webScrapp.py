import webbrowser , sys, pyperclip
if len(sys.argv)>1:
    address = ''.join(sys.argv[1:]) #Get adddress from command line
else:
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/search/' + address)


