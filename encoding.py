import pandas as pd

painting_data = pd.read_csv('painting_data.csv')

def ordinal(painting_data):   
    cat_col = []
    for i in range(len(painting_data.columns)):
        cat_col.append(i)

    uni_cat_col = []
    for a in range(len(cat_col)):
        col = cat_col[a]
        uni_cat_col.append(painting_data[col].unique())

    
    num_val = [j for j in range(len(uni_cat_col))]

    for k in range(len(uni_cat_col)):
        painting_data[col] = painting_data[col].replace(uni_cat_col[k], num_val[k])

    print(painting_data)



def one_hot(painting_data):
    cat_cols_1 = []
    for col_1 in range(len(painting_data.columns)):
            cat_cols_1.append(col_1)
   
    for i in range(len(cat_cols_1)) :
        col = cat_cols_1[i]
        lst = list(painting_data[col].unique())

     
        for j in range(len(lst)) :
            for k in range(len(painting_data[col_1])) :
                if lst[j] == painting_data[cat_cols_1[i]].iloc[k] :
                    painting_data.loc[painting_data.index[k], lst[j]] = 1

                else :
                    painting_data.loc[painting_data.index[k], lst[j]] = 0


    painting_data.drop(columns = cat_cols_1 , inplace = True)
    print(painting_data)


print(f"Orignal Dataset is: ",painting_data)

# Just run whatever encoding function with the parameter (painting_data) by calling it.



