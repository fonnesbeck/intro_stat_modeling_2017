# Introduction to Statistical Modeling with Python

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/fonnesbeck/intro_stat_modeling_2017)

**Wednesday, May 17, 2017 1:20 p.m.–4:40 p.m.**

Christopher Fonnesbeck  
Vanderbilt University Medical Center

## Description

This intermediate-level tutorial will provide students with hands-on experience applying practical Bayesian statistical modeling methods on real data. Unlike many introductory statistics courses, we will not be applying "cookbook" methods that are easy to teach, but often inapplicable; instead, we will learn some foundational statistical methods that can be applied generally to a wide variety of problems: comparing two groups with continuous and binary outcomes, linear regression, generalized linear models, model selection, and other useful techniques. The tutorial will start with a short introduction on data manipulation and cleaning using pandas, before proceeding on to simple concepts like fitting data to statistical distributions, and how to use optimization and simulation for data analysis. By using and modifying hand-coded implementations of these techniques, students will gain an understanding of how each method works. Students will come away with knowledge of how to deal with very practical statistical problems, such as how to deal with missing data, how to check a statistical model for appropriateness, and how to properly express the uncertainty in the quantities estimated by statistical methods.

## Outline

1. Introduction *(1:20-1:40)*
2. Data cleaning with Pandas *(1:40 - 2:10)*
3. Basic Bayesian inference *(2:10 - 3:10)*
4. Fitting Regression models *(3:15 - 4:15)*
5. Dealing with missing data *(4:15 - 4:40)*

## Software requirements

This tutorial is based on **Python 3**. I cannot guarantee that the materials will work well with Python 2 or earlier, so ensure Python 3.5 or greater is installed on your system.

I recommend installing the [Anaconda](https://www.continuum.io/downloads) distribution of Python 3, as it allows for the easy automation of package installation and virtual environment creation (see instructions below).

## Getting the tutorial materials

Clone this repository into a directory of your choice.

    git clone https://github.com/fonnesbeck/intro_stat_modeling_2017.git

If you are not familiar with Git and GitHub, you can simply download the zip file of the repository at the top of the main repository page.

Then, move to the directory created by the clone/zip file:

    cd intro_stat_modeling_2017

and install everything using `conda`:

    conda config --add channels conda-forge
    conda env create -f environment.yml
    
This will create an **environment** called `stat_pycon` that includes the packages required for the course.    
    
If you are not using the Anaconda Python distribution, you will need to manually install the packages listed in `environment.yml` using `pip`.

Which you probably don't want to do.

So [install Anaconda](https://www.continuum.io/downloads).

To use the environment, you may type:

    source activate stat_pycon
