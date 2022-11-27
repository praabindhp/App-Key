# Initializing The Libraries
import webbrowser
import keyboard
from msvcrt import getch
from sshkeyboard import listen_keyboard

def set_app():
    print("\nSet The App-Key")
    print("---------------")
    print('''The Hotkey Is : "Space"''')
    print('''Format : Hotkey + "Your Text"''')
    print('Leave Key-Text Empty To Exit')
    
    app_key = {}
    while True:
        k = input("\nEnter Key-Text : ")
        if k == '':
            print('App-Key Set Successfully :)')
            break
        url = input("Enter URL : ")
        app_key[k] = url
        global final_key
        final_key = app_key
        
    return final_key
            
def start_app():
    pass
    # print("Enter Value : ")
    # char = msvcrt.getch()
    # print(char)
    # if 'g' in char:
    #     webbrowser.open('https://www.google.com/')
    # elif char == "b'f'":
    #     webbrowser.open('https://www.facebook.com/')
    # elif char == "b'y'":
    #     webbrowser.open('https://www.youtube.com/')

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
            while True:
                key = ord(getch())
                if key == 27: #ESC
                    break
                elif key == 13: #Enter
                    print("You pressed key ENTER")
                    start_app()
                    continue
            
        else:
            exit()

#     if keyboard.is_pressed(hk + '+ g'): 
#         webbrowser.open('https://www.google.com/')
        
#     if keyboard.is_pressed(hk + '+ y'): 
#         webbrowser.open('https://www.youtube.com/')
        
#     if keyboard.is_pressed(hk + '+ f'):
#         webbrowser.open('https://www.facebook.com/')