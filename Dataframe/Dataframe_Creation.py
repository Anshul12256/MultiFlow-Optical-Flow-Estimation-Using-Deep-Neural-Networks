import pandas as pd
import os

# Input path for image frames location
folder = '/Users/anshulbansal/Downloads/MPI-Sintel-complete/training'
flow_path = '/Users/anshulbansal/Downloads/MPI-Sintel-complete/training'
data1 = []

files1 = [f for f in os.listdir(folder + '/final/alley_1/')]  # Change folder name for creating df
files1.sort()
files2 = [f for f in os.listdir(flow_path + '/flow/alley_1/')]  # Change folder name for creating df
files2.sort()
for i in range(len(files1) - 2):
    curr = ["alley1/" + files1[i], "alley1/" + files1[i + 1], "alley1/" + files1[i + 2], "alley1/" + files2[i]]
    data1.append(curr)

df1 = pd.DataFrame(data1, columns=["img1", "img2", "img3", "flow"])
df1.to_csv("alley1.csv")

# Randomly selects the df from the whole df
test_df = df1.sample(frac=0.1, random_state=44)
test_df.to_csv("alley1_test.csv")

# Removing test df from the complete df to obtain train df
test_img_1_list = test_df['img1'].tolist()
test_img_2_list = test_df['img2'].tolist()
test_img_3_list = test_df['img3'].tolist()
test_flow_list = test_df['flow'].tolist()

for i in range(len(test_flow_list)):
    df1 = df1[df1['flow'] != test_flow_list[i]]
df1.to_csv("alley1_train.csv")
