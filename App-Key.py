# Initializing The Libraries
import webbrowser
# import keyboard
from msvcrt import getch
from sshkeyboard import listen_keyboard

def set_app():
    print("\nSet The App-Key")
    print("---------------")
    print('''The Hotkey Is : "Space"''')
    print('Leave Key-Text Empty To Exit')
    
    app_key = {}
    while True:
        k = input("\nEnter App-Key : ")
        if k == '':
            print('App-Key Set Successfully :)')
            break
        
        key = ord(k)
        print(key)
        url = input("Enter URL : ")
        app_key[k] = url
        global final_key
        final_key = app_key
        
    return final_key
            
def start_app():
    key = ord(getch())
    print(key)
    if key == 27: # ESC
        print("You Pressed ESC")
    elif key == 13: # Enter
        print("You Pressed ENTER")
    elif key == 103: # g
        webbrowser.open('https://www.google.com/')
    elif key == 102: # f
        webbrowser.open('https://www.facebook.com/')
    elif key == 121: # y
        webbrowser.open('https://www.youtube.com/')

def stop_app():
    pass
  
if __name__ == "__main__":
    while True:
        print("\nWelcome To App-Key Application")
        print("------------------------------")
        print("Select Choice Of Execution")
        print("1 : Set App-Key")
        print("2 : Start App-Key")
        print("3 : Stop App-Key")
        print()

        choice = int(input("Enter The Choice : "))
        if choice == 1:
            set_app()
            print(final_key)
            continue
            
        elif choice == 2:
            print('''Format : Hotkey [Space] + "Your Key"''')
            while True:
                key = ord(getch())
                print(key)
                if key == 32: # Space
                    start_app()
                elif key == 27: # ESC
                    break
            
        else:
            exit()

# Noted Down ------------------------------------------

#     if keyboard.is_pressed(hk + '+ g'): 
#         webbrowser.open('https://www.google.com/')
        
#     if keyboard.is_pressed(hk + '+ y'): 
#         webbrowser.open('https://www.youtube.com/')
        
#     if keyboard.is_pressed(hk + '+ f'):
#         webbrowser.open('https://www.facebook.com/')

# print("Enter Value : ")
# char = msvcrt.getch()
# print(char)
# if 'g' in char:
#     webbrowser.open('https://www.google.com/')
# elif char == "b'f'":
#     webbrowser.open('https://www.facebook.com/')
# elif char == "b'y'":
#     webbrowser.open('https://www.youtube.com/')