import numpy as np



"""
Know that any task you take is to improve your skills (hard/soft)
so don't use any AI model to answer you
either asking a supporter or search about it
===========================================
There is 3 main levels and 2 Bonus
DO NOT use any AI Model to solve the task
Turn off the AI assistant (Autocomplete)
"""



# ==========================================
# LEVEL 1: The Basics (Required)
# Goal: Create arrays and access elements
# ==========================================

# TODO: Create a 1D array with numbers from 10 to 50
arr_1d =np.array([10,11,12,...,50])     #np.arange(10,51)

# TODO: Create a 3x3 matrix with values from 0 to 8
mat_3x3 = np.array([[0,1,2],[3,4,5],[6,7,8]]) #or np.arange(9).reshape(3,3)

# TODO: Access the element at the 2nd row, 3rd column of mat_3x3
element_2_3 =mat_3x3[1,2]


# ==========================================
# LEVEL 2: Slicing & Math (Required)
# Goal: Extract data and perform basic operations
# ==========================================

data = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

# TODO: Extract the subarray [[20, 30], [60, 70]]
center_slice = data[0:2,1:3]

# TODO: Add 100 to every element in the 'data' array
data_plus_100 =data+100


# ==========================================
# LEVEL 3: Weighted Grades (Required)
# Goal: Calculate weighted averages using aggregation
# ==========================================

# Scores for 3 students in 4 subjects
grades = np.array([
    [85, 90, 88, 92],
    [70, 80, 75, 85],
    [90, 95, 92, 98]
])

# Weights for the 4 subjects (must sum to 1.0)
weights = np.array([0.2, 0.3, 0.2, 0.3])

# TODO: Calculate the weighted average for each student
weighted_averages = np.sum(grades*weights,axis=1) #   # or weighted_averages = grades @ weights  


"""
The next part is Bonus and you may need to search about the answer
DO NOT USE any AI Model to search or complete it
"""


# ==========================================
# LEVEL 4: Outlier Detection (Bonus)
# Goal: Use boolean indexing and statistics
# ==========================================

# A dataset with some random values
dataset = np.array([10, 12, 12, 13, 12, 11, 14, 13, 100, 12, 11, 10, 150])

# TODO: Calculate the mean and standard deviation of the dataset
mean_val = np.mean(dataset)               
std_dev = np.std(dataset)#by search

# TODO: Create a mask for values that are more than 2 standard deviations away from the mean
# Hint: It's a boolean array of the same shape as dataset
outlier_mask =np.abs(dataset-mean_val)>2*std_dev
#away from the mean=abs(dataset-mean_val)

# TODO: Extract the outliers using the mask
outliers =dataset[outlier_mask]
#print the true value

# ==========================================
# LEVEL 5: Distance Matrix (Bonus)
# Goal: Advanced broadcasting
# ==========================================

# We have 5 points on a line
points = np.array([1, 4, 10, 15, 20])
# TODO: Calculate the distance matrix where entry (i, j) is absolute value of (points[i] - points[j])
n=len(points)
for i in range(n):
   for j in range(n):
      distance_matrix = abs(points[i]-points[j])
print(distance_matrix)
#or  by using broadcasting by numpy by search.
points = np.array([1, 4, 10, 15, 20])
point=np.array([[1],
                [4],
                [10],
                [15],
                [20]])
distance_matrix = abs(points-point)
print(distance_matrix)