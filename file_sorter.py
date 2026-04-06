import os                                                                                                      
                                                                                                               
os.makedirs("text_files", exist_ok=True)                                                                       
                                                                                                               
files = os.listdir()                                                                                           
                                                                                                               
for file in files:                                                                                             
        if file.endswith(".txt"):                                                                              
                os.rename(file, f"text_files/{file}")
                print(f"Moved {file} to text_files/{file}")

        if file.endswith(".jpg") or file.endswith(".png"):                                                                        
                os.rename(file, f"image_files/{file}")
                print(f"Moved {file} to image_files/{file}")    

        if file.endswith(".pdf"):                                                                             
                os.rename(file, f"pdf_files/{file}")
                print(f"Moved {file} to pdf_files/{file}")

        if file.endswith(".docx"):                                                                            
                os.rename(file, f"docx_files/{file}")
                print(f"Moved {file} to docx_files/{file}")

        if file.endswith(".xlsx"):                                                                            
                os.rename(file, f"xlsx_files/{file}")
                print(f"Moved {file} to xlsx_files/{file}")

        if file.endswith(".pptx"):                                                                            
                os.rename(file, f"pptx_files/{file}")
                print(f"Moved {file} to pptx_files/{file}")

        if file.endswith(".mp3") or file.endswith(".wav"):
                os.rename(file, f"audio_files/{file}")
                print(f"Moved {file} to audio_files/{file}")

        if file.endswith(".mp4") or file.endswith(".avi"):
                os.rename(file, f"video_files/{file}")
                print(f"Moved {file} to video_files/{file}")

        if file.endswith(".zip") or file.endswith(".rar"):
                os.rename(file, f"archive_files/{file}")
                print(f"Moved {file} to archive_files/{file}")

        if file.endswith(".py"): 
                os.rename(file, f"python_files/{file}")
                print(f"Moved {file} to python_files/{file}")

        if file.endswith(".css"):
                os.rename(file, f"css_files/{file}")
                print(f"Moved {file} to css_files/{file}")

        if file.endswith(".html"):
                os.rename(file, f"html_files/{file}")
                print(f"Moved {file} to html_files/{file}")

        if file.endswith(".js"):
                os.rename(file, f"js_files/{file}")
                print(f"Moved {file} to js_files/{file}")

        if file.endswith(".json"):
                os.rename(file, f"json_files/{file}")
                print(f"Moved {file} to json_files/{file}")

        if file.endswith(".xml"):
                os.rename(file, f"xml_files/{file}")
                print(f"Moved {file} to xml_files/{file}")

        if file.endswith(".csv"):
                os.rename(file, f"csv_files/{file}")
                print(f"Moved {file} to csv_files/{file}")

        if file.endswith(".log"):
                os.rename(file, f"log_files/{file}")
                print(f"Moved {file} to log_files/{file}")