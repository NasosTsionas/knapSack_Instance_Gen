

from tkinter import *
from tkinter import messagebox
import random

fields = ("Number of Objects [int]", "capacity [int]", \
          "min weight [float]", "max weight [float]",\
          "min value [float]", "max value [float]",\
          "floor by [int]", "file name [str]")




def makeform(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0, "10")
      row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
      lab.pack(side = LEFT)
      ent.pack(side = RIGHT, expand = YES, fill = X)
      entries[field] = ent
   return entries


def generate_instance(field_dict):
    name = str(field_dict["file_name"])
    f = open(name, "w")

    line = str(field_dict["num_of_objects"]) + " " + str(field_dict["capacity"]) + "\n"
    f.write(line)

    for i in range(field_dict["num_of_objects"]):
        wi = round(random.uniform(field_dict["min_weight"]\
                  , field_dict["max_weight"]), field_dict["floor_by"])

        vi = round(random.uniform(field_dict["min_value"],\
              field_dict["max_value"]), field_dict["floor_by"])

        line = str(vi) + " " + str(wi) + "\n"
        f.write(line)
    messagebox.showinfo("Success", "Instance created")
    f.close()
    global window
    window.destroy()


def check_results(entries):
    field_dict_def = {}


    # num_of_objects
    try:

        field_dict_def["num_of_objects"]= (int(entries[fields[0]].get()))
    except:
        messagebox.showerror("Error", "Error in: " + str(fields[0]))
        return False

    # capacity
    try:
        field_dict_def["capacity"] = (int(entries[fields[1]].get()))
    except:
        messagebox.showerror("Error", "Error in: " + str(fields[1]))
        return False

    # min weight
    try:
        field_dict_def["min_weight"]= (float(entries[fields[2]].get()))
    except:
        messagebox.showerror("Error", "Error in: " + str(fields[2]))
        return False

    # max weight
    try:

         field_dict_def["max_weight"] = (float(entries[fields[3]].get()))
    except:
        messagebox.showerror("Error", "Error in: " + str(fields[3]))
        return False

    # min value
    try:

         field_dict_def["min_value"] = (float(entries[fields[4]].get()))
    except:
        messagebox.showerror("Error", "Error in: " + str(fields[4]))
        return False

    # max value
    try:

         field_dict_def["max_value"]= (float(entries[fields[5]].get()))
    except:
        messagebox.showerror("Error", "Error in: " + str(fields[5]))
        return False


    # floor by
    try:

         field_dict_def["floor_by"]= (int(entries[fields[6]].get()))
    except:
        messagebox.showerror("Error", "Error in: " + str(fields[6]))
        return False


    # file name
    try:
         field_dict_def["file_name"]= (entries[fields[7]].get())
    except:
        messagebox.showerror("Error", "Error in: " + str(fields[7]))
        return False

    print(field_dict_def)
    generate_instance(field_dict_def)




















window = Tk()
window.title("Knapsack Generator")



# window.geometry('600x600')
window.configure(background = "grey")


ents = makeform(window, fields)

# window.bind('<Return>', (lambda event, e = ents: fetch(e)))


b1 = Button(window, text = 'Generate instance',
      command=(lambda e = ents: check_results(e)))

b1.pack(side = LEFT, padx = 5, pady = 5)





window.mainloop()














