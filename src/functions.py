import savReaderWriter as sr
import numpy as np
import pandas as pd

    
def spss_read(path):
    file = path
    info=sr.SavReader(file,returnHeader=True,recodeSysmisTo=np.nan)
    df=pd.DataFrame(info[0:],columns=info.header)
    df.columns=[i.decode('latin').lower() for i in df.columns]
    return(df)




class weighted(pd.core.frame.DataFrame):
    
    '''
    This class makes weighted Pandas DataFrames 
    '''
    
    def __init__(self, DataFrame, balance, weights=1):
        super(weighted, self).__init__(DataFrame)
        self.balance = balance
        self.weights = weights
    
    def obtain_weights(self, bias=0.001):
        '''
        This method gives the weights to compensate the sample.

        Parameters:
        -----------
        bias: float, default=0.001
                 We iterate until our error is smaller than epsilon.
        
        Returns:
        --------
                This method modifies the atribute weights of the object.
                
                It also creates a new column in the DataFrame that contains 
                exactly the same vector of weights.
        '''
        
        # Initialization of the VP      
        if not ('_VP_' in self.columns):
            print('Creating a default VP...')
            self['_VP_'] = 1

        variables = self.balance.keys()

        # In each iteration we adapt our sample to the expected values of the variables
        for variable in variables:
            compensed = self.groupby(variable)['_VP_'].sum()
            PCT = compensed/compensed.sum()*100
            table = self.balance[variable]/ PCT
            for i in table.index:
                self.loc[self[variable]==i,'_VP_']=self.loc[self[variable]==i,'_VP_']*table[i]

        # We compute the error of the weighted sample with all of the expected values.
        repeat = False
        error_list = []
        for variable in variables:
            compensed = self.groupby(variable)['_VP_'].sum()
            error = max(abs(self.balance[variable]-(compensed/compensed.sum()*100)))
            error_list.append(error)
            if (error>bias):
                repeat = True
        print("The error is fitted by:",max(error_list))

        if repeat == True:
            print('Iterating...')
            #recursivity:
            return weighted.obtain_weights(self, bias = bias)

        else:
            
            print("Process completed")
            self.weights = self['_VP_']
            return self.weights

    def print_txt(self, path):
        '''
        Given a path this method prints the weights that we computed in a .txt

        Parameters:
        -----------
        path: The path where we want to save the .txt

        Returns:
        --------
        Nothing.
        '''
        with open(path+"/weights.txt", 'a') as f:
            for i in range(len(self)):
                print(self.weights[i], file=f)
            # print(self.weights.values, file=f)
          
        
