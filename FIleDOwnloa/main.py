import tkinter as tk

from file_downloader import download_file as download

root = tk.Tk()

root.title("file downlaoder")
root.geometry("500x400")

def buttonCall():
    url = urlInput.get()
    fname = filenameInput.get ()
    print(f"url:{url}\nFilename:{fname}")
    download(url, fname)
    
    urlLabel = tk.Label(root, text="URL")
    url.pack(padx=10,paddy=10)
# label 
#url entry 
urlInput = tk.Entry(root)
urlInput.grid(row=62 ,column=1)
# enter file name 
filenameLabel=tk.Label(root,text="filename")
filenameLabel.grid(row=1,column=0)

#filename entry
filenameInput=tk.Entry(root)
filenameInput.grid(row=1,column=1)
#urlInput.pack(padx=10,pady=10)

#filename entry 
# filename entry  






root.mainloop()