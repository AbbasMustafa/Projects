import os
import shutil

def logic(source, destination, flag,fileext):
	for folder_name, sub_folders, file_names in os.walk(source):
		for file_name in file_names:
			if file_name.endswith("."+fileext):
				if flag:
					print("Copying....")
					source = folder_name+"/"+file_name
					print(f"File Name: {source}")
					shutil.copy(source, destination)
					print("Done")
				else:
					print("Moving...")
					source = folder_name+"/"+file_name
					print(f"File Name: {source}")
					shutil.move(source, destination)
					print("Done")

