import statsmodels.api as sm
import statsmodels.formula.api as sf
import pandas as pd

def logit(y,x):
    result,fail=[]
    # 1~10 사이의 값을
    for num in y.unique():
        temp={}
        x=sm.add_constant(x)
        #카테고리형 x는 get_dummies
        fit=sm.Logit(endog=y.apply(lambda x:1 if x==num else 0),exog=pd.get_dummies(sm.add_constant(x),drop_first=True,dtype='int')).fit()
        temp["accuracy"]=(fit.pred_table()[0,0]+fit.pred_table()[1,1])/fit.pred_table().sum()
        temp["aic"]=fit.aic
        temp["model"]=fit
        result.append(temp)
    return result