from tkinter import *
import string


print("Welcome to Passman")
print("0:Encrypt / 1:Decrypt / 2:Fetch password / 3:Exit")

char = list(" " + string.punctuation + string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase)
key = " ~bZAMoDfOSTaDnTUMWjdwCPCuIvFVKHkhnm!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}NmqtlczwIgjAyplsPHGubykEEiKYatQWzLvxRFciGJxBeZhNsrYfqegdOJQVBXSoLUrXRp"
    
class Passman(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x400")
        self.minsize(700,400)
    
    def Encryptor(self):
        plain_text = Encrypt_input.get()
        cipher_text = ""
        for letter in plain_text:
            index = char.index(letter)
            cipher_text += key[index]
        Encrypted_text = Label(self, text=f"Here is your encrypted password{cipher_text}").place(x=50,y=150)
        storing_value = Encrypt_id_input.get()
        update_passfile = open("encrypted/passwords.txt", "a")
        update_passfile.write(f"{storing_value} : {cipher_text}\n")
        update_passfile.close()
        
    def Decryptor(self):
        cipher_text_input = Decrypt_input.get()
        plain_text = ""
        for letter in cipher_text_input:
            index = key.index(letter)
            plain_text += char[index]
        Decrypted_text = Label(self, text=f"Your decrypted text is : {plain_text}").place(x=500,y=150)
        
    def Fetch_pass(self):
        index_value = Enter_id_input.get()
        fetch_file = open("encrypted/passwords.txt", "r")
        res = {key.strip(): value.strip() for key, value in (line.split(':', 1) for line in fetch_file)}
        stored_cipher_txt = res.get(index_value)
        plain_txt = ""
        for letter in stored_cipher_txt:
            index = key.index(letter)
            plain_txt += char[index]
        Fetched_pass = Label(self, text=f"Your password is : {plain_txt}").place(x=250,y=200)
        
    def destroy_prog(self):
        self.destroy()
        
        

passman = Passman()
passman.title("Passman - The password manager")

#Encryptor
Encrypt_label = Label(passman, text="Enter your password").place(x=50,y=60)
Encrypt_input = Entry(passman)
Encrypt_input.place(x=50,y=85)
Encrypt_id_label = Label(passman, text="Enter a unique id").place(x=50,y=10)
Encrypt_id_input = Entry(passman)
Encrypt_id_input.place(x=50,y=35)
Encrypt_btn = Button(passman, text="Encrypt", command=passman.Encryptor).place(x=50,y=120)

#Decryptor
Decrypt_label = Label(passman, text="Enter message to decrypt").place(x=500,y=60)
Decrypt_input = Entry(passman)
Decrypt_input.place(x=500,y=85)
Decrypt_btn = Button(passman, text="Decrypt", command=passman.Decryptor).place(x=500,y=120)

#Password_fetcher
Enter_id_label = Label(passman, text="Enter unique ID of your password").place(x=250,y=10)
Enter_id_input = Entry(passman)
Enter_id_input.place(x=250,y=35)
Enter_id_btn = Button(passman, text="Fetch", command=passman.Fetch_pass).place(x=250,y=70)

#Quit
Quit_btn = Button(passman, text="Quit!" , command=passman.destroy_prog).place(x=300,y=300)

passman.mainloop()