# Overview

Most people not trained in the arts have trouble distinguishing between a masterpiece and really good art. They are often perplexed by what makes one piece of art sell for hundreds of thousands, and another seemingly similar, for $200. In this project, I will analyze photographs sold on Amazon Art, extracting information about symmetry, hue, saturation, value, size, description, and price.

My objective is to determine if there is an underlying characteristics of the most valuable photographs and if so to identify what those characteristics are. 

# Methodology
1. Create a script and use AWS to scrape Amazon Art photographs and extract the photo’s title, size, price, descriptuion, and photographer.
2. Clean the data and create a "Price per Sq Inch" feature to use as the outcome.
2. Get dummies for each artist and run a logistic reression to compare the predictive power of photographer on price per sq inch.
3. Use a count vectorizer and K-means to create clusters and split the photos into categorys. Manually analyze what the characteristics of each category are and give them a label. Check if price can be predicted by knowing which category an image falls into.
4. Use OpenCV to extract image properties for each photo. Properties such as symmetry and color hue, saturation, and value will be extracted.
5. Create a random forrest and train it on description and the extracted image properties in order to see if the predictive power of photographer and price is improved by adding image properties.

# Deliverables
*Jupyter notebook documenting data exploration
*Jupyter notebook documenting feature analysis
*Jupyter notebook documenting modeling
*Research paper describing work
*Presentation distilling research

# Dataset

The "final_df.csv" dataset can be found in the data folder of this repository. The data folder also includes the cleaned dataset.
