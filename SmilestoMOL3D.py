#Developed by Vishvajit Bakarola
#At Laboratory of Machine Intelligence at Uka Tarsadia University, Gujarat, India
#vishvajit.bakrola@utu.ac.in

import os
import pandas as pd
import tkinter as tk

root= tk.Tk()

root.geometry("550x170")
root.title("Chemical Smiley to Mol3d Convertor by MI Laboratory - UTU")

def smi_to_mol3d():
    data = pd.read_excel("smiles.xlsx", header=0)

    total_smiles = len(data)
    for i in range (0, total_smiles):
        smi = "smiley" + str(i) + ".smi"
        file = open(smi, "w")
        file.write(data['smiles'][i])
        file.close()
        
        a = "obabel "
        b = smi + " "
        c = "-O out.sdf --gen3d"
        mol3d = "mol" + str(i) + ".sdf"

        os.system('cmd /c' "obabel "+b+"-O " +mol3d+ " --gen3d")

        os.remove(smi)

T = tk.Text(root, height = 5, width = 85)
l = tk.Label(root, text = "Instrctions")
l.config(font=("Courier", 14))
ins1 = "1. Please keep your .xlxs formatted file in the current directory."
ins2 = "2. The name of .xlxs should be smiles"
ins3 = "3. There should be only one colum named smiles"

button1 = tk.Button(text='Convert my Smiley to Mol3D', command=smi_to_mol3d, bg='green', fg='white', font=('helvetica', 12, 'bold'))

l.pack()
T.pack()
button1.pack()
T.insert(tk.END, ins1 + "\n")
T.insert(tk.END, ins2 + "\n")
T.insert(tk.END, ins3)
root.mainloop()
