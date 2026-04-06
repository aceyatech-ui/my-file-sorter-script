import os                                                                                                      
                                                                                                               
os.makedirs("text_files", exist_ok=True)                                                                       
                                                                                                               
files = os.listdir()                                                                                           
                                                                                                               
for file in files:                                                                                             
        if file.endswith(".txt"):                                                                              
                os.rename(file, f"text_files/{file}")                                                          
                print(f"moved {file} to text_files folder") 
                