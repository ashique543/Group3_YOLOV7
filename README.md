# Object Detection and Tracking using Yolov7 and implementing Hadoop

# Abstract
```yaml
This project explores implementing YOLO v7, a state-of-the-art real-time object detection algorithm, for practical use. We aim to train it on a custom/public dataset, optimise it for a chosen hardware platform, and evaluate its performance in terms of accuracy, speed, and resource efficiency. Additionally, a comparison with other object detection algorithms might be conducted. The project seeks to develop an efficient and optimised YOLO v7 system with valuable insights into its capabilities and limitations for real-world applications.
```

# Introduction
```yaml
DOMAIN DESCRIPTION : 

o Yolov7

The YOLOv7 object tracking and detection project represents a significant advancement in the field of computer vision, offering a powerful solution for real-time object detection and tracking in videos. YOLOv7, an evolution of the YOLO (You Only Look Once) series, is renowned for its speed and accuracy, making it an ideal choice for applications requiring rapid analysis of video streams. The project's goal is to leverage the capabilities of YOLOv7 to detect and track objects across frames, enabling the monitoring and analysis of dynamic scenes in real time.

One of the key features of YOLOv7 is its ability to process video streams with remarkable speed, making it suitable for applications where real-time performance is crucial. This is achieved through a single neural network that predicts bounding boxes and class probabilities directly from full images in one evaluation, eliminating the need for complex multi-stage processing pipelines. This approach allows YOLOv7 to achieve impressive detection speeds, making it well-suited for applications such as surveillance, traffic monitoring, and robotics, where real-time object detection and tracking are essential.

In addition to its speed, YOLOv7 also offers high accuracy in object detection, thanks to its advanced architecture and training techniques. The model is trained on large datasets containing annotated images, allowing it to learn to recognize a wide range of objects with high precision. This high level of accuracy is critical for applications where the reliable detection of objects, even in challenging conditions, is paramount. By combining speed and accuracy, YOLOv7 offers a compelling solution for real-time object detection in video streams.



o Hadoop

Hadoop is an open-source framework for distributed storage and processing of large datasets across clusters of computers. It was initially developed by Doug Cutting and Mike Cafarella in 2005, inspired by Google's MapReduce and Google File System (GFS) papers. Named after a toy elephant, Hadoop has become a cornerstone technology in the big data ecosystem due to its scalability, fault tolerance, and flexibility.

At its core, Hadoop consists of two main components:
Hadoop Distributed File System (HDFS): HDFS is a distributed file system that provides high-throughput access to application data. It divides large files into smaller blocks and distributes them across multiple nodes in a cluster, ensuring redundancy and fault tolerance.
MapReduce: MapReduce is a programming model and processing engine for distributed computing on large datasets. It divides tasks into two phases: the map phase, where data is processed in parallel across nodes, and the reduce phase, where results are aggregated. This paradigm allows for efficient processing of vast amounts of data across a cluster of machines.

Hadoop also includes other complementary tools and projects, such as:
YARN (Yet Another Resource Negotiator): YARN is a resource management layer that allows different data processing engines to run on top of the Hadoop cluster, enabling more diverse workloads beyond MapReduce, such as Apache Spark and Apache Flink.

Hadoop has revolutionised the way organisations handle big data, enabling them to store, process, and analyse massive volumes of structured and unstructured data more efficiently and cost-effectively than ever before. Its ecosystem continues to evolve, with ongoing developments and integrations with other technologies to address the ever-changing demands of the big data landscape.



MOTIVATION :

This project investigates YOLO v7's potential for real-time object detection. Its impressive accuracy, speed, and efficiency make it a promising candidate for pushing the boundaries of this technology, potentially impacting fields like self-driving cars, robotics, and security. We aim to explore its capabilities, optimise it for practical use, and compare it to alternatives, ultimately contributing to advancements in real-time object detection.


SCOPE OF WORK :

This project implements and evaluates YOLO v7 for real-time object detection, focusing on -

Training: Choose/train YOLO v7 on a suitable dataset.
Implementation: Optimise the model for a chosen hardware platform.
Evaluation: Analyse accuracy, speed, and resource efficiency.
Comparison (optional): Compare YOLO v7 with other algorithms.
Deliverables: Optimised YOLO v7 implementation & evaluation report.
Exclusions: Custom application development, production deployment, extensive hardware optimization

Hadoop is further used to store files after detection and tracking -

Data Storage: Hadoop provides a distributed file system (HDFS) that can store vast amounts of data across a cluster of machines. 
Data Processing: Hadoop enables parallel processing of large datasets using the MapReduce programming model or other distributed computing frameworks like Apache Spark or Apache Flink.

The scope of YOLOv7 lies in efficient real-time object detection and tracking, offering high accuracy across diverse environments. On the other hand, Hadoop's scope encompasses scalable storage and processing of vast datasets, ensuring fault tolerance and facilitating real-time and batch analytics. Combining YOLOv7 with Hadoop allows for the seamless integration of cutting-edge object detection capabilities with the robust infrastructure required to handle and analyse large-scale video data, enabling applications in surveillance, monitoring, and analytics at scale.



SIGNIFICANCE OF THE STUDY:

- Advancement in Computer Vision: By developing techniques for object detection and tracking, our project contributes to the advancement of computer vision technologies. This field has numerous real-world applications, including surveillance, autonomous vehicles, and augmented reality.

- Practical Applications: The ability to detect and track objects in videos has practical implications across various industries. For instance, in surveillance, it can enhance security by automatically identifying and tracking suspicious activities. In retail, it can be used for customer tracking and behaviour analysis.

- Data Management and Analysis: Creating CSV files with object coordinates provides structured data that can be further analysed. This data can offer insights into object movements, patterns, and behaviours over time. By uploading this data into Hadoop, you enable scalable storage and processing, facilitating large-scale data analysis.

- Big Data Integration: Integrating object coordinates into Hadoop demonstrates the project's scalability and compatibility with big data technologies. This allows for the integration of object tracking data with other sources of information for comprehensive analysis and decision-making.

- Video Analysis: Providing a video of detected objects enhances the usability of the system by offering visual confirmation of the object detection and tracking capabilities. This feature can be valuable for stakeholders who prefer visual representation over raw data.

- Contribution to Research: our project adds to the body of research in the field of object detection and tracking. It may introduce novel methodologies, algorithms, or improvements to existing techniques, thereby enriching the academic and scientific community's understanding of computer vision.

- Scalability: Hadoop's distributed file system (HDFS) allows for the storage and processing of massive amounts of data across a cluster of commodity hardware. When dealing with video streams, especially high-resolution ones or streams from multiple cameras, the volume of data can be enormous. Using Hadoop ensures that the system can scale seamlessly to handle this data influx.

- Integration with Other Data: Hadoop's flexibility allows for easy integration with other data sources and types. For example, alongside object coordinates, additional metadata such as timestamps, camera IDs, or environmental conditions can be stored and analyzed together, providing richer insights and context.

- Cost-effectiveness: Hadoop's open-source nature and ability to run on commodity hardware make it a cost-effective solution for storing and processing large-scale data. By leveraging Hadoop, the project can potentially reduce infrastructure costs compared to proprietary or cloud-based solutions.
```
# Device Configuration
Hardware:
```
GPU: A modern GPU with significant memory (at least 4GB) is highly recommended for training and inference, especially for larger YOLO v7 variants. CPUs can work for smaller models and inference on edge devices, but expect slower performance.
CPU: A multi-core CPU with decent clock speed is essential, even with GPUs.
Memory: RAM requirements depend on model size and dataset size. 16GB RAM is a good starting point, but expect higher needs for larger models and datasets.
```

 Software:
```
Operating System: While YOLO v7 generally works on major operating systems (Linux, Windows, macOS), specific OS versions and configurations might influence performance.
Python Version: Python 3.6 or later is recommended.
Deep Learning Frameworks: Ensure compatibility with your chosen framework (PyTorch or TensorFlow) and its version requirements.
JDK 1.8 and Hadoop
```

Overall Recommendations:
```
Start with a smaller YOLO v7 variant like YOLOv7-Tiny on a GPU with at least 4GB memory and 16GB RAM.
Use Python 3.6+ and compatible deep learning framework versions.
Consider optimising your model and training process for specific resource constraints.
Explore cloud platforms or specialised hardware (TPUs) for demanding tasks and large models.
```

# Detection and Tracking

### Steps to run Code

- Clone the repository.
```
git clone 
```
- Goto the cloned folder.
```
cd yolov7-object-tracking
```
- Create a virtual envirnoment (Recommended, If you dont want to disturb python packages)
```
### For Linux Users
python3 -m venv yolov7objtracking
source yolov7objtracking/bin/activate

### For Window Users
python3 -m venv yolov7objtracking
cd yolov7objtracking
cd Scripts
activate
cd ..
cd ..
```
- Upgrade pip with mentioned command below.
```
pip install --upgrade pip
```
- Install requirements with mentioned command below.
```
pip install -r requirements.txt
```
- Run the code with mentioned command below (by default, pretrained [yolov7](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt) weights will be automatically downloaded into the working directory if they don't already exist).

#for saving tracks centroid, track id and bbox coordinates
```
python detect_and_track.py --weights yolov7.pt --source "your video.mp4" --save-txt --save-bbox-dim
```

- Output file, along with text files containing coordinates will be created with original filename in the directory
```
working-dir/runs/detect/obj-tracking
``` 
### Results of detected and tracked files
<table>
  <tr>
    <td>for video 1</td>
    <td>for video 2</td>
    <td>for video 3</td>
  </tr>
  <tr>
    <td><img src="screenshots for readme\v1.png"></td>
    <td><img src="screenshots for readme\v2.png"></td>
     <td><img src="screenshots for readme\v3.png"></td>
  </tr>
  <tr>
    <td>directory containing the output video along with coordinates directory</td> 
  </tr>
  <tr>
    <td><img src="screenshots for readme\ss1.png"></td> 
  </tr>
 </table>

 ### Results of coordinates
 Here, each frame is represented by the frame number positioned at the end of text file. Each frame contains several objects, whose coordinates are computed and stored in the text files along with object's number (id).
<table>
  <tr>
    <td>Inside the coordinate folder</td>
    <td>Inside a text file of coordinate folder</td>
  </tr>
  <tr>
    <td><img src="screenshots for readme\ss4.png"></td>
    <td><img src="screenshots for readme\footage_1.png"></td>
  </tr>
 </table>

# Python Codes to run on the results

- To check if the objects of a particular videos are moving or still,along with the entry frame and exit frame of every objects, run
```
python moving_still_final.py
``` 
&emsp;&emsp;&emsp;Then you will be asked to enter the directories folder for the coordinates.\
&emsp;&emsp;&emsp;Output will be given as a csv file inside the working-dir/runs/detect/obj-tracking with the name : ```<video_source_name>_output_status_all_objects.csv``` 

- To check the objects that entered or exited from individual frames, run
```
python frame_info.py
```
&emsp;&emsp;&emsp;Then you will be asked to enter the directories folder for the coordinates.\
&emsp;&emsp;&emsp;Output will be given as a csv file with the name : ```video-source_frame_info.csv```

### Results of CSV files
<table>
  <tr>
    <td>directory containing the new csv files</td> 
  </tr>
  <tr>
    <td><img src="screenshots for readme\ss2.png"></td> 
  </tr>
  <tr>
    <td>CSV for the details of object</td>
    <td>CSV for the details of frames</td>
  </tr>
  <tr>
    <td><img src="screenshots for readme\footage_frame_info_ss.png" height=250></td>
    <td><img src="screenshots for readme\footage_output_status_all_objects_ss.png" height=250></td>
  </tr>
 </table>

# Using Hadoop

- To upload the coordinates in Hadoop follow the steps :
```
# Install java jdk 8 in your system. Then inside the directory where jdk 1.8 is saved, open ```bin``` and copy the path and set is as environment variable.
# Install Hadoop in your system. Open the directory where hadoop is saved, 
    open ```bin``` and copy the path and set is as environment variable.
    open ```sbin``` and copy the path and set is as environment variable.
```

- open cmd, then run the following 
```
hdfs namenode -format
```

- open cmd from the sbin directory of hadoop, then run the following to enable hadoop
```
start-dfs.cmd
start-yarn.cmd
```
&emsp;&emsp;&emsp;2 command windows will open for start-dfs : namenode and datanode\
&emsp;&emsp;&emsp;2 command windows will again open for start-yarn : Resource manager and Node manager\
&emsp;&emsp;&emsp;We can check if the nodes are open, by running ```jps```

- To create a directory of your choice in hadoop, run the code in cmd
```
hadoop fs -mkdir /<directory_in_hadoop>
```

- To upload the coordinate folder (where the coordinates of objects in each frame is present in the form of txt file), run the following
```
hadoop fs -put <path_of_local_directory> /<directory_in_hadoop>
```

- To delete a particular directory if you want, run the following
```
hadoop fs -rm -r /<directory_in_hadoop>
```

- To view the created hadoop directory and uploaded files in hadoop, do the following
```
1. Open Browser 
2. type "localhost:9870"
3. Go to "Utilities" tab 
4. select "Browse the file system"

Here, you can find the directory and click it to view the uploaded files
```
<table>
  <tr>
    <td>Directory in Hadoop containing the uploaded text files</td> 
  </tr>
  <tr>
    <td><img src="screenshots for readme\ss3.png"></td> 
  </tr>
 </table>

# detect_and_track.py
This python program is used to get the tracked video. This program also provides the coordinates of each object framewise in the same directory, where the tracked video is saved. The program analyses the coordinates and saves them as text files. These text files are further used for other programs.

# moving_still_final.py
This python program analyses all the text files that stores coordinates of each object in each frame. Then it computes which object is moving and which ones are still by comparing from the previous frame. This program also displays in which frame the particular object has entered and exited.\
The output is created as CSV file\
<img src="screenshots for readme\footage_output_status_all_objects_ss.png">


# frame_info.py
This python program is used to find out the objects that has entered and exited with respect to frames. It displays the frame number, along with the objects that has entered and exited in that particular frame.\
The output is created as CSV file\
<img src="screenshots for readme\footage_frame_info_ss.png">

# Bibliography
- https://github.com/RizwanMunawar/yolov7-object-tracking
- https://github.com/theos-ai/easy-yolov7
- https://github.com/WongKinYiu/yolov7
- https://www.oracle.com/in/java/technologies/javase/javase8-archive-downloads.html
- https://hadoop.apache.org/
- https://www.youtube.com/watch?v=knAS0w-jiUk