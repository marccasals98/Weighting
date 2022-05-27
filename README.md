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

### Reading the .sav

For reading the .sav we only need to use the function spss_read(). 

```
df = functions.spss_read(r"C:\Users\m.casals\Desktop\EG_7C.sav")
```
The r in the begining of the path is because in Python the path are written with this slashes "/" and not this "\" so, for not changing all the slashes of the path, one must only write an r.

r"C:\Users\m.casals\Desktop\EG_7C.sav" = "C:/Users/m.casals/Desktop/EG_7C.sav"

So now df will be a Pandas DataFrame which will contain all the information that can be seen in SPSS.

### Creating an object of weighting class.

In this step we will create an object of the class. Doing so makes it possible to use all the methods that I've created. 

First of all, we need a Dictionary with the desired values that each variable need. In this case we are weighting the sample with three variables and the values that we want.  

We want these variables to have these balances:

| 'p8tar' | 'trabr' | 'ciudad' |
|---------|---------|----------|
| 50%     | 77%     | 42%      |
| 30%     | 23%     | 20%      |
| 20%     |         | 14%      |
|         |         | 5%       |
|         |         | 9%       |
|         |         | 2%       |
|         |         | 2%       |
|         |         | 6%       |

For balancing our sample this way we need to create a Python Dictionary:

```
dic = {'p8tar':[50,30,20],
      'trabr':[77,23],
      'ciudad':[42,20,14,5,9,2,2,6]}    
```

Now we can create the new object!

```
df_wei = functions.weighted(df, balance = dic )
```

### Computing the weights and saving them in a .txt file:

For computing the weights we need to call the method:

```
df_wei.obtain_weights()
```
for saving them in a text file we need to do:

```
path ="C:/Users/m.casals/Desktop"
df_wei.print_txt(path)
```
In this case we didn't put the 'r' in front of the path, we only changed the slashes.

## Results:

The following file is unblanced:
| 'p8tar' | 'trabr' | 'ciudad' |
|---------|---------|----------|
| 57.1%   | 87.3%   | 29.7%    |
| 22.9%   | 12.7%   | 6.5%     |
| 20%     |         | 19%      |
|         |         | 5.7%     |
|         |         | 20%      |
|         |         | 7.2%     |
|         |         | 6.5%     |
|         |         | 5.5%     |

We want to achieve:
| 'p8tar' | 'trabr' | 'ciudad' |
|---------|---------|----------|
| 50%     | 77%     | 42%      |
| 30%     | 23%     | 20%      |
| 20%     |         | 14%      |
|         |         | 5%       |
|         |         | 9%       |
|         |         | 2%       |
|         |         | 2%       |
|         |         | 6%       |

The results that are obtained are:
| 'p8tar' | 'trabr' | 'ciudad' |
|---------|---------|----------|
| 50%     | 76.999% | 42%      |
| 29.999% | 23%     | 20%      |
| 20%     |         | 14%      |
|         |         | 5%       |
|         |         | 9%       |
|         |         | 2%       |
|         |         | 2%       |
|         |         | 6%       |
