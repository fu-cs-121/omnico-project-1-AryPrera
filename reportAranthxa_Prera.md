# Euphoria User Engagement Analysis Report

**Author:** [Aranthxa Prera]  
**Date:** [March 13th]

---

## Introduction

This analysis explores user engagement with different  algorithms in Euphoria csv data. By examining session duration, happiness ratings, and session frequency, I could understand which algorithms are most effective and how users interact with them.

## Methodology

1. Data Collection & Preprocessing

I accessed the dataset stored in euphoria_data.csv, which contained user session details, including the algorithm used, session duration, and happiness rating.

I read the data line by line, cleaning and structuring it into a list format for easy processing.

2. Categorizing Data by Algorithm

I created a dictionary to track engagement statistics for each algorithm: JoyStream, SerenityFlow, and DeepPulse.

I initialized metrics such as total happiness rating, total session duration, and session count for each algorithm.

3. Computing Key Metrics

For each session recorded in the dataset, I performed the following calculations:

Total number of sessions per algorithm: Counted occurrences of each algorithm in the dataset.

Total session duration per algorithm: Summed up session durations for each algorithm.

Total happiness rating per algorithm: Summed up happiness ratings provided by users for each algorithm.

Using the aggregated data, I then calculated:

Average happiness rating per algorithm
​Average session duration per algorithm
Highest and lowest performers: Identified the algorithm with the highest average happiness and the one with the longest average session duration.

4. Data Validation & Interpretation

To ensure accuracy, I verified that all session counts, durations, and happiness ratings matched the dataset.

The results were analyzed to understand user preferences, engagement trends, and any anomalies in the data.

## Results

- **Average Happiness Rating per Algorithm**

  - JoyStream: 8.50
  - SerenityFlow: 7.00
  - DeepPulse: 5.00

- **Total Number of Sessions per Algorithm**

  - JoyStream: 4
  - SerenityFlow: 3
  - DeepPulse: 3

- **Average Session Duration per Algorithm**

  - JoyStream: 37.50 minutes
  - SerenityFlow: 30.00 minutes
  - DeepPulse: 45.00 minutes

- **Highest and Lowest Performers**
  - Highest Average Happiness Rating: 8.5
  - Longest Average Session Duration: 45 minutes

## Observations and Insights

JoyStream has the highest happiness rating, making it the most effective in improving user mood.

DeepPulse has the longest session duration (45 min) but the lowest happiness rating (5.00). This suggests that users might continue using it in search of better results, but it doesn’t seem to deliver the desired emotional impact.

SerenityFlow falls somewhere in between, maintaining a moderate balance between happiness and session duration.

## Conclusions and Recommendations

recomendations:

Refining DeepPulse – Since users spend the most time on it despite lower happiness, I need to investigate whether it's due to frustration, curiosity, or something else

Expanding JoyStream’s Impact – Given its effectiveness in increasing happiness, it could be:

Recommended as the default algorithm for new users.

conclusions:

From this analysis, JoyStream is the most effective for boosting happiness, while DeepPulse keeps users engaged the longest but may need optimization to improve satisfaction. Moving forward, I plan to refine the user experience to align with the goal of enhancing well-being.



---

_This report contains confidential information proprietary to OmniCo. Unauthorized use or disclosure is strictly prohibited._


