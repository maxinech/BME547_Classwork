import tkinter as tk
from tkinter import ttk


def main_window():

    def cancel_cmd():
        root.destroy()

    def ok_cmd():
        print("Here is the data")
        entered_name = name_entry.get()
        print("Name: {}".format(entered_name))
        entered_id = id_entry.get()
        print("Id: {}".format(entered_id))
        entered_blood_letter = blood_letter.get()
        entered_rh_factor = rh_factor.get()
        print("Blood type: {}".format(entered_blood_letter+entered_rh_factor))

    root = tk.Tk()
    root.title("Health Database")
    root.geometry("700x400")

    ttk.Label(root, text="Blood Donor Database").grid(column=0, row=0,
                                                      columnspan=2,
                                                      sticky='w')
    ttk.Label(root, text="Name:").grid(column=0, row=1, sticky=tk.E)
    name_entry = tk.StringVar()
    name_entry.set("Enter a name here")
    ttk.Entry(root, width=40, textvariable=name_entry).grid(column=1, row=1,
                                                            sticky=tk.W)

    ttk.Label(root, text="ID:").grid(column=0, row=2, sticky=tk.E)
    id_entry = tk.StringVar()
    ttk.Entry(root, textvariable=id_entry).grid(column=1, row=2, sticky=tk.W)

    blood_letter = tk.StringVar()
    ttk.Radiobutton(root, text="A", variable=blood_letter, value="A")\
        .grid(column=0, row=3, sticky=tk.W)
    ttk.Radiobutton(root, text="B", variable=blood_letter, value="B")\
        .grid(column=0, row=4, sticky=tk.W)
    ttk.Radiobutton(root, text="AB", variable=blood_letter, value="AB")\
        .grid(column=0, row=5, sticky=tk.W)
    ttk.Radiobutton(root, text="O", variable=blood_letter, value="o")\
        .grid(column=0, row=6, sticky=tk.W)

    rh_factor = tk.StringVar()
    rh_factor.set('+')
    ttk.Checkbutton(root, text="Rh Positive", variable=rh_factor,
                    onvalue='+', offvalue='-').grid(column=1, row=4)

    ttk.Label(root, text="Nearest Donation Center").grid(column=2, row=0)
    donor_center = tk.StringVar()
    center_dropdown = ttk.Combobox(root, textvariable=donor_center)
    center_dropdown.grid(column=2, row=1)
    center_dropdown["values"] = ("Durham", "Raleigh", "Cary", "Apex")
    center_dropdown.state(['readonly'])

    ttk.Button(root, text="Ok", command=ok_cmd).grid(column=1, row=20)
    ttk.Button(root, text="Cancel", command=cancel_cmd).grid(column=2, row=20)

    root.mainloop()


if __name__ == '__main__':
    main_window()
