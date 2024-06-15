# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 22:02:06 2022

@author: 91995
"""

import pandas as pd
df = pd.read_csv("bank-full.csv",sep=";")
df
df.head()
list(df)
df.dtypes

df["pdays"]


df.duplicated()
df[df.duplicated()]
df.columns.duplicated()

df.isna()
df.isna().sum()


########################################################################################3

Y = df["y"]
X = df.iloc[:,0:16]

############################################################################################

import matplotlib.pyplot as plt
plt.figure(figsize=(30,10))
plt.scatter(X["age"],X["day"],color = "black")
plt.show()
plt.figure(figsize=(30,7))

plt.scatter(X["duration"],X["day"],color = "black")
plt.scatter(X["campaign"],X["day"],color = "black")
plt.scatter(X["previous"],X["day"],color = "black")


plt.scatter(X["day"],X["previous"],color = "black")


###################################################################################################



from  sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
df["y"] = LE.fit_transform(df["y"])

df.boxplot(column="age",vert = False)

###################################################################################################

import numpy as np
Q1 = np.percentile(df["age"],25)
Q1
Q2 = np.percentile(df["age"],50)
Q3 = np.percentile(df["age"],75)
IQR = Q3-Q1
IQR
LW = Q1 - (1.5*IQR)
UW = Q3 + (1.5*IQR)

df[df["age"]<LW]
df[df["age"]>UW]

len(df[(df["age"]<LW) | (df["age"]>UW)])

df["age"]=np.where(
    df["age"]>UW,
    UW,
    np.where(
    df["age"]<LW,
    LW,
   df["age"]
   )
    )


import numpy as np
Q1 = np.percentile(df["balance"],25)
Q1
Q2 = np.percentile(df["balance"],50)
Q3 = np.percentile(df["balance"],75)
IQR = Q3-Q1
IQR
LW = Q1 - (1.5*IQR)
UW = Q3 + (1.5*IQR)

df[df["balance"]<LW]
df[df["balance"]>UW]

len(df[(df["balance"]<LW) | (df["balance"]>UW)])

df["balance"]=np.where(
    df["balance"]>UW,
    UW,
    np.where(
    df["balance"]<LW,
    LW,
   df["balance"]
   )
    )
df.boxplot(column="campaign",vert = False)


import numpy as np
Q1 = np.percentile(df["campaign"],25)
Q1
Q2 = np.percentile(df["campaign"],50)
Q3 = np.percentile(df["campaign"],75)
IQR = Q3-Q1
IQR
LW = Q1 - (1.5*IQR)
UW = Q3 + (1.5*IQR)

df[df["campaign"]<LW]
df[df["campaign"]>UW]

len(df[(df["campaign"]<LW) | (df["campaign"]>UW)])

df["campaign"]=np.where(
    df["campaign"]>UW,
    UW,
    np.where(
    df["campaign"]<LW,
    LW,
   df["campaign"]
   )
    )



import numpy as np
Q1 = np.percentile(df["previous"],25)
Q1
Q2 = np.percentile(df["previous"],50)
Q3 = np.percentile(df["previous"],75)
IQR = Q3-Q1
IQR
LW = Q1 - (1.5*IQR)
UW = Q3 + (1.5*IQR)

df[df["previous"]<LW]
df[df["previous"]>UW]

len(df[(df["previous"]<LW) | (df["previous"]>UW)])

df["previous"]=np.where(
    df["previous"]>UW,
    UW,
    np.where(
    df["previous"]<LW,
    LW,
   df["previous"]
   )
    )

df.boxplot(column="previous",vert = False)


#====================================================================
import numpy as np
Q1 = np.percentile(df["duration"],25)
Q1
Q2 = np.percentile(df["duration"],50)
Q3 = np.percentile(df["duration"],75)
IQR = Q3-Q1
IQR
LW = Q1 - (1.5*IQR)
UW = Q3 + (1.5*IQR)

df[df["duration"]<LW]
df[df["duration"]>UW]

len(df[(df["duration"]<LW) | (df["duration"]>UW)])

df["duration"]=np.where(
    df["duration"]>UW,
    UW,
    np.where(
    df["duration"]<LW,
    LW,
   df["duration"]
   )
    )


df
df.boxplot(column="duration",vert = False)


#====================================================================


import numpy as np
Q1 = np.percentile(df["day"],25)
Q1
Q2 = np.percentile(df["day"],50)
Q3 = np.percentile(df["day"],75)
IQR = Q3-Q1
IQR
LW = Q1 - (1.5*IQR)
UW = Q3 + (1.5*IQR)

df[df["day"]<LW]
df[df["day"]>UW]

len(df[(df["day"]<LW) | (df["day"]>UW)])

df["day"]=np.where(
    df["day"]>UW,
    UW,
    np.where(
    df["day"]<LW,
    LW,
   df["day"]
   )
    )

df.boxplot(column="day",vert = False)


#############################################################3

import numpy as np
Q1 = np.percentile(df["pdays"],25)
Q1
Q2 = np.percentile(df["pdays"],50)
Q3 = np.percentile(df["pdays"],75)
IQR = Q3-Q1
IQR
LW = Q1 - (1.5*IQR)
UW = Q3 + (1.5*IQR)

df[df["pdays"]<LW]
df[df["pdays"]>UW]

len(df[(df["pdays"]<LW) | (df["pdays"]>UW)])

df["pdays"]=np.where(
    df["pdays"]>UW,
    UW,
    np.where(
    df["pdays"]<LW,
    LW,
   df["pdays"]
   )
    )

df.boxplot(column="pdays",vert = False)

######################################3######################################




df.groupby("job").size()
t1 = df.groupby("job").size()

t1.plot(kind = "bar")

#################################################################################3

from  sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
X["job"] = LE.fit_transform(df["job"])
X["marital"] = LE.fit_transform(df["marital"])
X["education"] = LE.fit_transform(df["education"])

X["default"] = LE.fit_transform(df["default"])
X["housing"] = LE.fit_transform(df["housing"])


X["loan"] = LE.fit_transform(df["loan"])

X["contact"] = LE.fit_transform(df["contact"])


X["month"] = LE.fit_transform(df["month"])


X["poutcome"] = LE.fit_transform(df["poutcome"])


X["y"] = LE.fit_transform(df["y"])


X.dtypes
#############################################################################################3


from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,train_size = 0.7)

X_train.shape,X_test.shape,Y_train.shape,Y_test.shape

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train,Y_train)
Y_pred_train = logreg.predict(X_train)
Y_pred_test = logreg.predict(X_test)


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_train,Y_pred_train)
cm = confusion_matrix(Y_test,Y_pred_test)
cm




from sklearn.metrics import accuracy_score
print("Training accuracy",accuracy_score(Y_train,Y_pred_train).round(3))

print("Test accuracy",accuracy_score(Y_test,Y_pred_test).round(3))



d1 = pd.DataFrame(Y_pred_train)

pd.concat([Y,d1],axis = 1)















