## MultiFlow - Optical Flow estimation using Deep Neural Networks

 - This repository contains the implementation of my Master Thesis titled: MultiFlow - Optical Flow estimation using Deep Neural Networks
 - Optical flow is termed as the apparent motion of pixels that is caused due to the relative motion between the camera and the object between two consecutive images.
 - The MultiFlow model extends on this idea and uses 3 images rather than 2 images for optical flow estimation.
 - The model is adapted from the FlowNetC [5] model and extended to 3 images.
 
## MutiFlow Model Architecture
 - Contractive Network
 ![enter image description here](https://github.com/Anshul12256/MultiFlow-Optical-Flow-Estimation-Using-Deep-Neural-Networks/blob/main/Model%20Architecture/multiflow_contractive.png)
 - Refinement Network
![enter image description here](https://github.com/Anshul12256/MultiFlow-Optical-Flow-Estimation-Using-Deep-Neural-Networks/blob/main/Model%20Architecture/refinement_multiflow.png)

## Results

| Models | MPI Sintel Final Train AEPE (px) | MPI Sintel Final Train AEPE (px) |
|:-:|:-:|:-:|
| PWC-Fusion [1] | N/A | 4.566 |
| MultiFlow | 4.020 | 4.970 |
| ProFlow [2] | N/A | 5.017 |
| TIMCflow [3] | N/A | 5.049 |
| MR-Flow [4] | 3.590 | 5.380 |
| FlowNetC+ft+v [5] | 4.830 | 7.880 |
| FlowNetC+ft [5] | 5.280 | 8.510 |

 - The MPI Sintel [6] dataset contains 23 different scenes. 
 - The MultiFlow models is a scene-specific model. 
 - Each scene is evaluated separately and  the final AEPE is the average of the 23 scene-specific models.


 <p float="center">
  <img src="https://github.com/Anshul12256/MultiFlow-Optical-Flow-Estimation-Using-Deep-Neural-Networks/blob/main/Results/alley1_images.png" width="275" />
  <img src="https://github.com/Anshul12256/MultiFlow-Optical-Flow-Estimation-Using-Deep-Neural-Networks/blob/main/Results/alley1_ground_truth.png" width="275" /> 
  <img src="https://github.com/Anshul12256/MultiFlow-Optical-Flow-Estimation-Using-Deep-Neural-Networks/blob/main/Results/alley1_prediction.png" width="275" />
</p>

## Dataset - MPI Sintel 
  - Results obtained on the Final render of the MPI Sintel Dataset.
  - The dataset can be downloaded from - http://sintel.is.tue.mpg.de/downloads (Download the MPI-Sintel-complete.zip).
  - Extract the folder and use the images from the final folder and .flo files from the flow folder.


## Code Execution

### Dataframe Creation
- The MultiFlow model uses tf.data API to pass the data to the model. 
- To map the data values to the tf.data API and map function is used.
- This map function takes the inpt images from the dataframe.
- To create dataframe use - **Dataframe_Creation.py**
- In File - Enter path for dataset storage location in variables - **folder,  flow_path**.
- A random sampling process with 0.1 factor is used to create two separate train and test dataframes.


### MultiFlow Model Execution on Google Colab
- Upload the dataset on Google Drive.
- Upload the dataframes on Google Drive.
- Upload the jupyter notebook **MultiFlow_Sintel_Final.ipynb** on Google drive and open with Colab notebook environment.
- Link Google Drive Storage with Colab Notebooks using the command:  
``` from google.colab import drive ```
``` drive.mount('/content/gdrive') ```

### Making predictions
- Enter train dataframes path in variable **df**.
-  Upload the model checkpoints file on Google Drive and enter the path in variable **checkpoint_path** for each model.
-  Do not execute the two Train function cells.
-  Enter location to store flow visualizations in function ``` visualize_flow_train() ``` and ``` visualize_flow_test() ```
-  Enter test dataframes path in variable **test_df**.
-  All other instructions are commented in the notebook.

## Installation
These installation steps are for executing the Mutiflow model on the local system
- Install TensorFlow GPU - ``` pip3 install tensorflow-gpu==2.1.0```
- Install TensorFlow addons - ``` pip3 install tensorflow-addons==0.8.2```
- Install JupyterLab - ``` pip3 install jupyterlab```
- Run Jupyter Notebook - ``` jupyter notebook```
- In addition to installing the above mentioned packages, also install the required python packages such as pandas, numpy given in the notebook for successful execution of the file.
- Load the jupyter notebook **MultiFlow_Sintel_Final.ipynb** and make predictions.
- The steps for making predictions on the local system are same as above.

## References

<a id="1">[1]</a> Ren, Zhile; Gallo, Orazio; Sun, Deqing; Yang, Ming-Hsuan; Sudderth, Erik; Kautz, Jan: A fusion approach for multi-frame optical flow estimation. 

<a id="1">[2]</a> Maurer, Daniel; Bruhn, Andres: ProFlow: Learning to Predict Optical Flow.

<a id="1">[3]</a> Yang, Fei; Cheng, Yongmei; Van De Weijer, Joost; Mozerov, Mikhail G.: Improved Discrete Optical Flow Estimation With Triple Image Matching Cost.

<a id="1">[4]</a> Wulff, Jonas; Sevilla-Lara, Laura; Black, Michael J.: Optical flow in mostly rigid scenes.

<a id="1">[5]</a> Dosovitskiy, Alexey; Fischer, Philipp; Ilg, Eddy; Hausser, Philip; Hazirbas, Caner; Golkov, Vladimir; Van Der Smagt, Patrick; Cremers, Daniel; Brox, Thomas: Flownet: Learning optical flow with convolutional networks.

<a id="1">[6]</a> Butler, Daniel J.; Wulff, Jonas; Stanley, Garrett B.; Black, Michael J.: A naturalistic open source movie for optical flow evaluation.


 