import os 

homework_id = int(input("Enter which No. of homework(ex.hw01 = 1)"))

common_file = ["./makefile","./README","./readme"]
files_ = 0
for i in range(3):
	if(os.path.exists(common_file[i])):
		print("Found "+common_file[i])
		print("Saving "+common_file[i])
		os.system("zip output "+common_file[i])
		files_ += 1


file_id = 1
while(1):
	file_path = "./hw0"+str(homework_id)+"0"+str(file_id)
	if(os.path.exists(file_path+".c")):

		print("Found "+file_path+".c")
		print("Saving "+file_path+".c")
		os.system("zip output "+file_path+".c")
		files_ += 1
		file_id += 1
	else:
		break

print("Auto-Zip Success!")
print("Total zipped "+str(files_)+" files")

