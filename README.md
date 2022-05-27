# Weighting
The purpose of this package is to store some functions that will be used when weighting unbalanced samples.

### spss_read()
This function reads a .sav file given a path.

## Class weighted

This class is a subclass from Pandas DataFrame and inherits it's structure. The new things that are implemented are two methods.

### obtain_weights()

Given an unbalanced sample from two or more non-independent variables, this method allow us to balanced it iteratively.

### print_txt() 

This method prints the output weights in a .txt file.



## Example:

In this example we are going to see the procedure that have to be followed for installing and using this file.

### Installing and importing packages.

First of all an installation of Python == 3, Pip and Git is needed.

Then, in order to install the package, input the following command to the console:

```
pip install git+https://github.com/marccasals98/Weighting
```

Then for importing the package:

```
import weighting 
```



