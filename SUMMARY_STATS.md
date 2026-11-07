# Amazon Bestsellers Analysis - Summary Metrics

## 1. Overall Statistics

|       |   User Rating |   Reviews |   Price |
|:------|--------------:|----------:|--------:|
| count |        147    |     147   |  147    |
| mean  |          4.68 |   27186   |   11.55 |
| std   |          0.19 |   23034.4 |    5.82 |
| min   |          3.8  |    2052   |    3    |
| 25%   |          4.6  |   14331   |    8    |
| 50%   |          4.7  |   23308   |   11    |
| 75%   |          4.8  |   28534.5 |   15    |
| max   |          4.9  |  154200   |   52    |

## 2. Fiction vs Non-Fiction Comparison

| Genre       |   Total_Books |   Avg_Rating |   Median_Rating |   Avg_Price |   Median_Price |   Avg_Reviews |
|:------------|--------------:|-------------:|----------------:|------------:|---------------:|--------------:|
| Fiction     |            74 |         4.66 |            4.75 |       11.42 |            9.5 |       29739.9 |
| Non Fiction |            73 |         4.69 |            4.7  |       11.68 |           12   |       24597.2 |

## 3. Correlation Matrix

|             |   User Rating |   Reviews |   Price |   Year |
|:------------|--------------:|----------:|--------:|-------:|
| User Rating |         1     |    -0.108 |  -0.076 |  0.14  |
| Reviews     |        -0.108 |     1     |   0.104 |  0.389 |
| Price       |        -0.076 |     0.104 |   1     | -0.085 |
| Year        |         0.14  |     0.389 |  -0.085 |  1     |
