## Overview ##
This repository is dedicated to the final project for the IS-477: Data Management, Curation, and Reproducibility course, Fall 2023 semester. The project encompasses a comprehensive analysis and visualization of the Car Evaluation Dataset, a well-structured dataset from the UCI Machine Learning Repository. This dataset, derived from a hierarchical decision model, is ideal for research in constructive induction and structure discovery. The analysis focuses on the application of decision tree classification to evaluate car acceptability based on various attributes like price, technical characteristics, and safety. Additionally, the project includes summary statistics and a visualization depicting the distribution of car evaluation classes, providing insights into the dataset's composition and trends.

## Contributions ##
As the sole contributor to this project, I, Deyi Zhang, have independently undertaken all aspects of the work. This includes data collection, analysis, decision tree modeling, creation of visualizations, and documentation.

## Analysis ##
The analysis of the Car Evaluation Dataset reveals interesting patterns and relationships between different car attributes and their overall acceptability. The decision tree classifier effectively identifies key factors influencing car evaluation. The summary statistics and visualizations further augment the understanding of the dataset, highlighting the distribution and variation across different car classes.

## Workflow ##
![Workflow Diagram](/Users/victordashuaibi/Desktop/is477-fall2023-final-project/workflow.png)

Reproducing
To reproduce this analysis, follow these steps:

### Clone the repository: ###

git clone https://github.com/victordashuaibi/is477-fall2023-final-project.git

### Install the necessary libraries: ###

pip install -r requirements.txt

### Execute the analysis files: ###

### Prepare the data: ###

snakemake --rulegraph prepare

### Profile the data: ###

snakemake --rulegraph profile

### Analyze the data: ###

snakemake --rulegraph analyze

## License ##

This project is licensed under the MIT License. This license was chosen for its permissiveness, allowing unrestricted use, modification, and distribution of the software, making it suitable for academic and open-source projects.

References
Dataset Information:

Bohanec, Marko. (1997). Car Evaluation. UCI Machine Learning Repository. https://doi.org/10.24432/C5JP48.
Dataset License:

Creative Commons Attribution 4.0 International (CC BY 4.0).
The dataset is open for sharing and adaptation for any purpose, with appropriate credit.