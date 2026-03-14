import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
data={
    "size":[1000,1500,2000,2500,3000],
    "price":[200000,300000,400000,500000,600000]
    }
df=pd.DataFrame(data)
X=df[["size"]]
y=df["price"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.5)
model=LinearRegression()
model.fit(X_train,y_train)
print("Coefficient (slope):",model.coef_[0])
print("intercept:",model.intercept_)
user_size=float(input("enter the house size:"))
user_data=pd.DataFrame([[user_size]],columns=["size"])
prediction=model.predict(user_data)
print("pridicted house price:",prediction[0])
