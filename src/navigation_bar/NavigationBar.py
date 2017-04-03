from tkinter import *
from Page import *

class NavigationBar(Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.leftFrame = Frame(self)
        self.rightFrame = Frame(self)
        self.leftFrame.pack(side=LEFT)
        self.rightFrame.pack(side=LEFT)
        self.pages = {}
        self.buttons = {}
        self.current = None

    def addPage(self, PageClass):
        page = PageClass(self.rightFrame)
        self.pages[PageClass] = page
        button = Button(self.leftFrame, text=PageClass.name, command=lambda :self.open(PageClass))
        self.buttons[PageClass] = button
        button.pack(side=BOTTOM)
        if len(self.pages) == 1:
            self.open(PageClass)

    def removePage(self, PageClass):
        page = self.pages[PageClass]
        button = self.buttons[PageClass]
        del self.pages[PageClass]
        del self.buttons[PageClass]
        page.pack_forget()
        button.pack_forget()
        if(PageClass == self.current):
            self.current = None
            self.updateUI()

    def open(self, PageClass):
        self.current = PageClass
        self.updateUI()

    def updateUI(self):
        for key, value in self.pages.items():
            if key == self.current:
                value.pack()
            else:
                value.forget_pack()
        for key, value in self.buttons.items():
            if key == self.current:
                value.configure(background='green')
            else:
                value.configure(background='white')

root = Tk()

nb = NavigationBar(root)

nb.addPage(Page)

nb.pack()

root.mainloop()