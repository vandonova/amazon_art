# Overview

Most people not trained in the arts have trouble distinguishing between a masterpiece and really good art. They are often perplexed by what makes one piece of art sell for hundreds of thousands, and another seemingly similar, for $200. In this project, I will analyze prints sold on Amazon Art and predict their price based on their symmetry, hue, saturation, pixel value, size, description, and artist.

My objective is to determine if there are underlying characteristics of the photographs that influence their price the most and if so, to identify what those characteristics are. 

# Methodology
1. Create a script and use AWS to scrape Amazon Art prints, extracting the work’s title, size, price, description, and artist.
2. Clean the data and create a "Price per Square Inch" feature to use as the outcome.
3. Create seven "Price per Square Inch" bins to classify each print into.
4. Get dummies for each artist and run a Logistic Regression and a Naive Bayes Classifier to analyze the predictive power of photographer on price per square inch.
5. Use OpenCV to perform edge detection and feature extraction of each photo. Properties such as symmetry, hue, saturation, pixel value, and average RGB values will be extracted.
6. Use text vectorization to turn the description of each artwork into a feature matrix to be predicted on. The description will act as a proxy for the image content as content analysis is beyond the scope of this project.
5. Create a Random Forest and train it on the description and the extracted image properties in order to see if the predictive power of the photographer on price is improved by adding image properties.

# Deliverables
- Jupyter notebook documenting data exploration
- Jupyter notebook documenting feature analysis
- Jupyter notebook documenting modeling
- Research paper describing work
- Presentation distilling research

# Dataset
The "final_df.csv" dataset can be found in the data folder of this repository. The data folder also includes the cleaned dataset.

# Hypothesis
While style and content matter significantly in determining the price of a photograph, the photographer’s popularity ultimately drives the amount paid for a piece of art.

# Results
The Naive Bayes model which predicted the price per square inch of the artwork based solely on the artist classified each price with an accuracy of 78.4%. The final Random Forest model based on the vectorized description and image properties was able to classify the price per square inch of the prints in the test dataset with 80.3% accuracy. 

# Next Steps
- Continue to refine the dataset and scrape more data
- Incorporate Google’s content analysis API
- Incorporate a metric for artist popularity
- Use this project as a basis for building a recommendation engine for new photographers in order to determine where and for how much they should sell their prints.
