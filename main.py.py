import customtkinter as ctk
from tkinter import messagebox, filedialog
from Crypto.Cipher import AES
import base64
import hashlib
import os

# --- ORTAK FONKSİYONLAR ---
def get_key(password):
    return hashlib.sha256(password.encode('utf-8')).digest()

# --- METİN ŞİFRELEME FONKSİYONLARI ---
def encrypt_message():
    try:
        password = entry_password.get()
        message = text_input.get("1.0", "end-1c")
        
        if not password or not message:
            messagebox.showwarning("Uyarı", "Lütfen şifre ve metin alanlarını doldurun.")
            return

        key = get_key(password)
        cipher = AES.new(key, AES.MODE_GCM)
        ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
        
        encrypted_data = cipher.nonce + tag + ciphertext
        encrypted_base64 = base64.b64encode(encrypted_data).decode('utf-8')
        
        text_output.delete("1.0", "end")
        text_output.insert("end", encrypted_base64)
    except Exception as e:
        messagebox.showerror("Hata", f"Şifreleme başarısız:\n{e}")

def decrypt_message():
    try:
        password = entry_password.get()
        encrypted_b64 = text_input.get("1.0", "end-1c").strip()
        
        if not password or not encrypted_b64:
            messagebox.showwarning("Uyarı", "Lütfen parola ve şifreli metin alanlarını doldurun.")
            return

        key = get_key(password)
        encrypted_data = base64.b64decode(encrypted_b64)
        
        nonce = encrypted_data[:16]
        tag = encrypted_data[16:32]
        ciphertext = encrypted_data[32:]
        
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        decrypted_message = cipher.decrypt_and_verify(ciphertext, tag)
        
        text_output.delete("1.0", "end")
        text_output.insert("end", decrypted_message.decode('utf-8'))
    except ValueError:
        messagebox.showerror("Hata", "Şifre çözülemedi! Parola yanlış veya veri bozulmuş.")
    except Exception as e:
        messagebox.showerror("Hata", f"Çözme başarısız:\n{e}")

# --- DOSYA ŞİFRELEME FONKSİYONLARI ---
def encrypt_file():
    password = entry_password.get()
    if not password:
        messagebox.showwarning("Uyarı", "Lütfen önce yukarıya bir parola girin.")
        return
        
    file_path = filedialog.askopenfilename(title="Şifrelenecek Dosyayı Seçin")
    if not file_path:
        return
        
    try:
        key = get_key(password)
        with open(file_path, "rb") as f:
            file_data = f.read()
            
        cipher = AES.new(key, AES.MODE_GCM)
        ciphertext, tag = cipher.encrypt_and_digest(file_data)
        
        # Dosyayı .enc (encrypted) uzantısıyla kaydediyoruz
        output_path = file_path + ".enc"
        with open(output_path, "wb") as f:
            f.write(cipher.nonce + tag + ciphertext)
            
        messagebox.showinfo("Başarılı", f"Dosya başarıyla şifrelendi!\nKaydedildi: {output_path}")
    except Exception as e:
        messagebox.showerror("Hata", f"Dosya şifrelenirken hata oluştu:\n{e}")

def decrypt_file():
    password = entry_password.get()
    if not password:
        messagebox.showwarning("Uyarı", "Lütfen önce yukarıya bir parola girin.")
        return
        
    file_path = filedialog.askopenfilename(title="Çözülecek Dosyayı Seçin (.enc)")
    if not file_path:
        return
        
    try:
        key = get_key(password)
        with open(file_path, "rb") as f:
            encrypted_data = f.read()
            
        nonce = encrypted_data[:16]
        tag = encrypted_data[16:32]
        ciphertext = encrypted_data[32:]
        
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
        
        # Dosya adındaki .enc uzantısını kaldırıp orijinal haliyle kaydediyoruz
        output_path = file_path.replace(".enc", "") 
        # Eğer uzantı yoksa (farklı bir isimleyse) sonuna _cozuldu ekle
        if output_path == file_path:
            output_path += "_cozuldu"
            
        with open(output_path, "wb") as f:
            f.write(decrypted_data)
            
        messagebox.showinfo("Başarılı", f"Dosya başarıyla çözüldü!\nKaydedildi: {output_path}")
    except ValueError:
        messagebox.showerror("Hata", "Şifre çözülemedi! Parola yanlış veya dosya bozulmuş.")
    except Exception as e:
        messagebox.showerror("Hata", f"Dosya çözülürken hata oluştu:\n{e}")


# --- MODERN GÖRSEL ARAYÜZ (GUI) KURULUMU ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("AES-256 Gelişmiş Şifreleme")
app.geometry("550x650")
app.resizable(False, False)

# Başlık
title_label = ctk.CTkLabel(app, text="🔒 AES-256 Şifreleme Aracı", font=("Roboto", 24, "bold"))
title_label.pack(pady=(20, 10))

# Ortak Parola Alanı (Her iki sekme de bu parolayı kullanacak)
label_password = ctk.CTkLabel(app, text="Gizli Anahtar (Parola)", font=("Roboto", 14))
label_password.pack(anchor="w", padx=30)
entry_password = ctk.CTkEntry(app, width=490, show="*", placeholder_text="Tüm işlemler için parolanızı buraya girin...", font=("Roboto", 14))
entry_password.pack(pady=(0, 15), padx=30)

# --- SEKMELER (TABS) ---
tabview = ctk.CTkTabview(app, width=490, height=400)
tabview.pack(padx=30, pady=10)

tab_text = tabview.add("Metin İşlemleri")
tab_file = tabview.add("Dosya İşlemleri")

# --- 1. SEKME: METİN İŞLEMLERİ ---
label_input = ctk.CTkLabel(tab_text, text="İşlem Yapılacak Metin", font=("Roboto", 14))
label_input.pack(anchor="w", padx=10, pady=(10, 0))
text_input = ctk.CTkTextbox(tab_text, width=450, height=100, font=("Roboto", 14))
text_input.pack(pady=(5, 15), padx=10)

button_frame = ctk.CTkFrame(tab_text, fg_color="transparent")
button_frame.pack(pady=5)
btn_encrypt = ctk.CTkButton(button_frame, text="Kilitle (Şifrele)", width=200, fg_color="#27ae60", hover_color="#2ecc71", command=encrypt_message)
btn_encrypt.grid(row=0, column=0, padx=10)
btn_decrypt = ctk.CTkButton(button_frame, text="Kilidi Aç (Çöz)", width=200, fg_color="#2980b9", hover_color="#3498db", command=decrypt_message)
btn_decrypt.grid(row=0, column=1, padx=10)

label_output = ctk.CTkLabel(tab_text, text="Sonuç", font=("Roboto", 14))
label_output.pack(anchor="w", padx=10, pady=(10, 0))
text_output = ctk.CTkTextbox(tab_text, width=450, height=100, font=("Roboto", 14), text_color="#f1c40f")
text_output.pack(pady=(5, 10), padx=10)

# --- 2. SEKME: DOSYA İŞLEMLERİ ---
file_info = ctk.CTkLabel(tab_file, text="Bilgisayarınızdaki herhangi bir dosyayı (PDF, PNG, TXT vb.)\nAES-256 ile şifreleyebilir veya çözebilirsiniz.", font=("Roboto", 14), justify="center")
file_info.pack(pady=(40, 30))

btn_encrypt_file = ctk.CTkButton(tab_file, text="📄 Dosya Seç ve Şifrele", width=300, height=40, fg_color="#27ae60", hover_color="#2ecc71", font=("Roboto", 15, "bold"), command=encrypt_file)
btn_encrypt_file.pack(pady=10)

btn_decrypt_file = ctk.CTkButton(tab_file, text="🔓 Şifreli Dosyayı Seç ve Çöz", width=300, height=40, fg_color="#2980b9", hover_color="#3498db", font=("Roboto", 15, "bold"), command=decrypt_file)
btn_decrypt_file.pack(pady=20)

app.mainloop()