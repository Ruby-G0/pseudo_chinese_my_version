import pseudo_chinese
import tkinter

class pseudo(object):
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("伪中国语生成器（日->中）")
        self.input = tkinter.Entry(self.root, width=30)
        self.display_result = tkinter.Listbox(self.root, width=50)
        self.trans_button = tkinter.Button(self.root, command = self.get_result, text="开始转换")

    def gui_arrange(self):
        self.input.pack()
        self.display_result.pack()
        self.trans_button.pack()

    def get_result(self):
        document = self.input.get()
        result = pseudo_chinese.main(document)

        self.display_result.delete(0)
        self.display_result.insert(0, result)

def main():
    PSD = pseudo()
    PSD.gui_arrange()
    tkinter.mainloop()
    pass

if __name__ == "__main__":
    main()