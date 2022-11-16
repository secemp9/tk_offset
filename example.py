import tkinter as tk


root = tk.Tk()

main_text = tk.Text(root)

box_text = tk.Text(root, height=1, width=10)
box_text.pack()

txt = """hello world"""

len_txt = len(txt) # get the total length of the text content. Can be replaced by `os.path.getsize` or other alternatives for files

main_text.insert(tk.INSERT, txt)

def offset():
    inputValue = box_text.get("1.0", "end-1c") # get the input of the text widget without newline (since it's added by default)

    # focusing the other text widget, deleting and re-insert the original text so that the selection/tag is updated (no need to move the mouse to the other widget in this example)
    main_text.focus()
    main_text.delete("1.0", tk.END)
    main_text.insert(tk.INSERT, txt)

    try:
        to_do = inputValue.split("-")
        if len(to_do) == 1: # if length is 1, it probably is a single offset for a single byte/char
            to_do.append(to_do[0])
            # second = to_do[0]
        if int(to_do[0]) > int(to_do[1]): # This is to support reverse range offset, so 11-2 -> 2-11, etc
            first = int(to_do[1]) - 1
            first = str(first).split("-")[-1:][0]

            second = (int(to_do[0]) - len_txt) - 1
            second = str(second).split("-")[-1:][0]
        else: # use the offset range normally
            first = int(to_do[0]) - 1
            first = str(first).split("-")[-1:][0]

            second = (int(to_do[1]) - len_txt) - 1
            second = str(second).split("-")[-1:][0]

        print(first, second)
        main_text.tag_add("sel", '1.0 + {}c'.format(first), 'end - {}c'.format(second))
    except Exception as test: # not good practice, but hopefully should be fine for this small example
        pass

buttonCommit = tk.Button(root, text="use offset",
                    command=lambda: offset())
buttonCommit.pack()
main_text.pack(fill="both", expand=1)
main_text.pack_propagate(0)
root.mainloop()
