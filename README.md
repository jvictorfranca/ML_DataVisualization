# ML_DataVisualization
# Introduction

This repository sums many examples of Data Exploration for Machine learning. It is intended as a future repository for my consult, and stores lessons learned, exercices, and projects. Data Exploration is a important step in Machine learning, this technique involves describing, visualizing and analyzing data in order to better understand it. With this process we can answer some questions, such as:

 - How many rows and columns there are on the dataset?
 - What are the data types given in this problem?
 - Are there missing, inconsistent or duplicate values in the data?
 - How different features relate to each other?

Even with some complex statistical analyses, some problems are better understood with the visualization approach. With this method one can create images of graphs, charts and plots to see more clearly the data structure and distribution. There are 4 main types of visualization:

 - Comparison: Illustrate difference between two or more items, in a period of time. Example: Boxplot.
    - Provides insights, such as the importance of a feature; variation, median and mean values of subgroups; and outliers.

 - Relationship: Illustrate correlation between two or more variables. Scatter plots or line charts are the most common examples.
    - Also shows feature significance, and presence of outliers.

 - Distribution: Shows statistical distribution of values of a feature. The most frequently used is the histogram, that shows the most common values of a feature. Can visualize spread or skewedness of data.
    - Highlight presence of outliers, and symmetry of the data.

 - Composition: Shows a component makeup of the data. The most commonly used are stacked bar charts, grouped bar charts and pie charts. It can show how much a subgroup contribute to the whole.
    - Can also illustrate relative and absolute change of a subgroup over time.



    # Dependencies

This repository will use dependencies to generate plots, and their documentation can be checked for more info. 
 - [Matplotlib](https://matplotlib.org/3.5.3/index.html) : Graphs created with seaborn will have a _sns sulfix.
 - [Seaborn](https://seaborn.pydata.org/) : Graphs created with seaborn will have a _sns sulfix.
 - [Plotly](https://plotly.com/python/) : Graphs created with plotly will have a _px sulfix.
 - [Pandas](https://pandas.pydata.org/) : Graphs created with plotly will have a _pd sulfix.

# Using this project
## To start project:

````
python -m venv venv

.\venv\Scripts\Activate.ps1

pip install -r requirements.txt
````

## To exit virtual environment:

````
deactivate
````

## To install dependency:

````
pip install dependency
pip freeze > requirements.txt
````