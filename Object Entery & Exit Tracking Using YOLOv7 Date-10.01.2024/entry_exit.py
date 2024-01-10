import os
import pandas as pd
import re

#to sort the files based on numeric part
def extract_number(filename):
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else float('inf')
    
def find_entry_exit_frames(input_folder, output_csv_path):
    data = []

    all_objects = set()
    entry_frames = {}
    exit_frames = {}

    for file_name in sorted(os.listdir(input_folder),key=extract_number):
        if file_name.endswith(".txt"):
            
            # csv_file_name = ''
            # for a in file_name[0]:
            #     if (a!='_'):
            #         csv_file_name = csv_file_name+a
            #     else:
            #         break
            # csv_file_name = csv_file_name+'_frame_info.csv'

            frame_num = int(file_name.split('_')[-1].split('.')[0])   #extracting frame number
            file_path = os.path.join(input_folder, file_name)

            with open(file_path, 'r') as file:
                lines = file.readlines()
            frame_objects = [line.split()[0] for line in lines]   #extracting object ID
            #for i in frame_objects:
            #    print(file_path,i)
            all_objects.update(frame_objects)

            for obj_num in frame_objects:
                if obj_num not in entry_frames:
                    entry_frames[obj_num] = frame_num

            for obj_num in all_objects:
                if obj_num not in frame_objects and obj_num not in exit_frames:
                    exit_frames[obj_num] = frame_num

    for obj_num in sorted(all_objects, key=int):
        data.append({'Entry_frame': entry_frames.get(obj_num), 'Exit_frame': exit_frames.get(obj_num, '-')})
    
    df = pd.read_csv(output_csv_path)

    new_df = pd.DataFrame(data)
    df = pd.concat([df, new_df], axis=1)
    df.to_csv(output_csv_path, index=False)

input_folder_path = input("Enter the path of coordinate folder - ")
for file_name in sorted(os.listdir(input_folder_path),key=extract_number):
    if file_name.endswith(".txt"):
            
        csv_file_name = ''
        for a in file_name:
            if (a!='_'):
                csv_file_name = csv_file_name+a
            else:
                break
        csv_file_name = csv_file_name+'.csv'
    
        
output_csv_path = csv_file_name
find_entry_exit_frames(input_folder_path, output_csv_path)