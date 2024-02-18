import os
import csv

def read_object_info(frame_path):
    # Read object information from the TXT file
    object_info = []
    with open(frame_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            object_id = int(parts[0])
            object_info.append(object_id)
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
    csv_file_name = csv_file_name+'_frame_info.csv'
    parent_folder_path = os.path.dirname(frames_folder)
    
    csv_file_path = os.path.join(parent_folder_path, csv_file_name)

    # Initialize CSV writer
    with open(csv_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Frame number', 'objects entered', 'objects exited'])

        all_object_ids = set()
        previous_objects = []
        # Process each frame
        i = 1
        for frame_file in frame_files:
            frame_path = os.path.join(frames_folder, frame_file)
            current_objects = read_object_info(frame_path)
            
            added = ''
            for obj in current_objects: 
                if obj not in all_object_ids:
                    if added=='':
                        added = int(obj)
                        added = str(added)
                    else:
                        added = added + ', ' + str(obj)
            
            exited = ''
            for obj in previous_objects:
                if obj not in current_objects:
                    if exited=='':
                        exited = int(obj)
                        exited = str(exited)
                    else:
                        exited = exited + ', ' + str(obj)

            if (i!=1):
                csv_writer.writerow([i-1, prev_added, exited])


            # Collect all object IDs
            all_object_ids.update(current_objects)
            previous_objects = current_objects
            i+=1
            prev_added = added

        # temp = "".join(str(current_objects))
        # temp = temp.replace("[","").replace("]","")
        csv_writer.writerow([i, added, exited])
        
    print("\nResults saved to "+csv_file_name)
    
if __name__ == '__main__':
    # Replace 'frames_folder' with the path to your frame TXT files folder
    frames_folder = input("Enter the path where coordinates are saved - ")

    # Classify objects and save results to CSV
    classify_objects(frames_folder)

    