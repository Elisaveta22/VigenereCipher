from tkinter import *
from itertools import cycle


def form_dict():
    return dict([(i, chr(i)) for i in range(128)])


def comparator(value, key):
    return dict([(idx, [ch[0], ch[1]])
                for idx, ch in enumerate(zip(value, cycle(key)))])


def encode_val(word):
    d = form_dict()
    return [k for c in word for k,v in d.items() if v == c]


def full_encode():
    value = encode_val(txt_word.get())
    key = encode_val(txt_encoding_key.get())
    d = comparator(value, key)
    l = len(form_dict())
    encoded_values = [(v[0] + v[1]) % l for v in d.values()]
    encoded_text = str.join("", [chr(v) for v in encoded_values])
    lbl.configure(text="Зашифрованный текст:" + encoded_text)
    txt_to_decode_word.delete(0, END)
    txt_to_decode_word.insert(0, encoded_text)


def decode_val(list_in):
    l = len(list_in)
    d = form_dict()
    return [d[i] for i in list_in if i in d]


def full_decode():
    value = encode_val(txt_to_decode_word.get())
    key = encode_val(txt_decoding_key.get())
    d = comparator(value, key)
    l = len(form_dict())
    decoded_values = [(v[0] - v[1]) % l for v in d.values()]
    decoded_text = str.join("", [chr(v) for v in decoded_values])
    lbl2.configure(text="Расшифрованный текст:" + decoded_text)




window = Tk()
window.geometry('600x350')
window.title("Vigenere Cipher")

# ENCODE

Label(window, text="Текст для шифрования: ").grid(row=0)

txt_word = Entry(window, width=30, font=30)
txt_word.grid(column=1, row=0, padx=20, pady=10)

Label(window, text="Ключ для шифрования:").grid(row=1)

txt_encoding_key = Entry(window, width=30, font=30)
txt_encoding_key.grid(column=1, row=1, padx=20, pady=0)

btn = Button(window, text="Зашифровать", font=12, command=full_encode)
btn.grid(column=1, row=3, padx=5, pady=5)

lbl = Label(window, font=("Arial Bold", 12))
lbl.grid(column=1, row=4)

# DECODE

Label(window, text="Текст для расшифровки: ").grid(row=6)

txt_to_decode_word = Entry(window, width=30, font=30)
txt_to_decode_word.grid(column=1, row=6, padx=20, pady=10)

Label(window, text="Ключ для расшифровки:").grid(row=7)

txt_decoding_key = Entry(window, width=30, font=30)
txt_decoding_key.grid(column=1, row=7, padx=20, pady=0)

btn2 = Button(window, text="Расшифровать", font=12, command=full_decode)
btn2.grid(column=1, row=9, padx=5, pady=5)

lbl2 = Label(window, font=("Arial Bold", 12))
lbl2.grid(column=1, row=10)



window.mainloop()

