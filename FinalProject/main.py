from gui8 import *

def main():
    window = Tk()
    window.geometry('1440x787')
    window.title('My Image Processing Application')
    window.resizable(False, False)

    window.configure(background='#fccc65')

    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()