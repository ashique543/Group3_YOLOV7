import os
import csv
import pandas as pd
import re

#to sort the files based on numeric part
def extract_number(filename):
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else float('inf')

def read_object_info(frame_path):
    # Read object information from the TXT file
    object_info = []
    with open(frame_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            object_id = int(parts[0])
            x1, y1, x2, y2 = map(float, parts[1:])
            average_x =(x1 + x2) / 2
            average_y =(y1 + y2) / 2
            #print(average_x,average_y)
            object_info.append((object_id, average_x, average_y))
    return object_info

def classify_objects(frames_folder):
    # List all frame files in the folder
    frame_files = sorted([f for f in os.listdir(frames_folder) if f.endswith('.txt')])

    # Collect all object IDs in the video
    all_object_ids = set()
    csv_file_name = ''
    for a in frame_files[0]:
        if (a!='_'):
            csv_file_name = csv_file_name+a
        else:
            break
    csv_file_name = csv_file_name+'_output_status_all_objects.csv'
    parent_folder_path = os.path.dirname(frames_folder)
    
    csv_file_path = os.path.join(parent_folder_path, csv_file_name)
    output_csv_path = os.path.join(parent_folder_path, csv_file_name)
    #print(csv_file_path)
    
    with open(csv_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['ObjectID', 'Status'])

        # Process each frame
        for frame_file in frame_files:
            frame_path = os.path.join(frames_folder, frame_file)
            current_objects = read_object_info(frame_path)

            # Collect all object IDs
            all_object_ids.update(obj[0] for obj in current_objects)
            
        
        previous_objects = None
        for object_id in sorted(all_object_ids):
            # Initialize status for each object
            # object_status = {'ObjectID': object_id, 'Status': 'Still'}

            # Find the object in the previous frame
            previous_obj = next((obj for obj in previous_objects if obj[0] == object_id), None) if previous_objects else None

            # Find the object in the current frame
            current_obj = next((obj for obj in current_objects if obj[0] == object_id), None)

            # Compare average IDs
            if previous_obj and current_obj and (previous_obj[1], previous_obj[2]) == (current_obj[1], current_obj[2]):
                x = 'Still'
            else:
                x = 'Moving'

            object_status = {'ObjectID': object_id, 'Status': x}
            # object_status['Status'] = 'Moving'

            # Write results to CSV only once for the entire video
            if frame_file == frame_files[-1]:
                csv_writer.writerow([object_id,x])

            previous_objects = current_objects
    
    
    data = []

    all_objects = set()
    entry_frames = {}
    exit_frames = {}

    for file_name in sorted(os.listdir(frames_folder),key=extract_number):
        if file_name.endswith(".txt"):
            frame_num = int(file_name.split('_')[-1].split('.')[0])   #extracting frame number
            file_path = os.path.join(frames_folder, file_name)

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
    print("\n\nResults saved to "+csv_file_name)

if __name__ == '__main__':
    # Replace 'frames_folder' with the path to your frame TXT files folder
    str = input("Enter the path where coordinates are saved - ")
    frames_folder = str

    # Classify objects and save results to CSV
    classify_objects(frames_folder)
    
