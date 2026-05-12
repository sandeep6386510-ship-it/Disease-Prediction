#!/usr/bin/env python
# coding: utf-8

# In[169]:


import numpy as np
import math
from sklearn.ensemble import VotingClassifier
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import  accuracy_score,precision_score,classification_report,recall_score,f1_score,confusion_matrix,roc_auc_score,roc_curve
import joblib

l1= ['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue','weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat','irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation','redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails','swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)','depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling','silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']
print(l1)


# In[3]:


l2=[]
for x in range(0,len(l1)):
  l2.append(0)


# In[4]:


disease=['(vertigo) Paroymsal Positional Vertigo',
         'AIDS',
'Acne',
'Alcoholic hepatitis',
'Allergy',
'Arthritis',
'Bronchial Asthma',
'Cervical spondylosis',
'Chicken pox',
'Chronic cholestasis',
'Common Cold',
'Dengue',
'Diabetes',
'Dimorphic hemmorhoids(piles)',
'Drug Reaction',
'Fungal infection',
'GERD',
'Gastroenteritis',
'Heart attack',
'Hepatitis B',
'Hepatitis C',
'Hepatitis D',
'Hepatitis E',
'Hypertension',
'Hyperthyroidism',
'Hypoglycemia',
'Hypothyroidism',
'Impetigo',
'Jaundice',
'Malaria',
'Migraine',
'Osteoarthristis',
'Paralysis (brain hemorrhage)',
'Peptic ulcer diseae',
'Pneumonia',
'Psoriasis',
'Tuberculosis',
'Typhoid',
'Urinary tract infection',
'Varicose veins',
'hepatitis A'] 


# In[5]:


print(disease)


# In[6]:


print(l2)


# In[7]:


data=pd.read_csv('/Users/shubh/Downloads/training.csv')
data.head(15)


# In[8]:


data.dtypes


# In[9]:


data.shape


# In[10]:


data['prognosis'].value_counts()


# In[11]:





# In[12]:


data.head(15)


# In[13]:


data['prognosis'].value_counts()


# In[14]:


data['prognosis']


# In[15]:


data['prognosis'].unique()


# In[16]:


X_train=data.drop('prognosis', axis=1)


# In[17]:


y_train=data['prognosis']


# In[18]:


X_train.head()


# In[19]:


y_train


# In[ ]:





# In[20]:


te=RandomForestClassifier(n_estimators = 1000,n_jobs = 5, criterion= 'entropy',random_state = 42)
te = te.fit(X_train.values,y_train.values.ravel())


# In[21]:


y_train_pred = te.predict(X_train.values)
print(y_train_pred)


# In[22]:


model_train_accuracy=accuracy_score(y_train,y_train_pred)
model_train_f1=f1_score(y_train,y_train_pred,average='weighted')
model_train_precision=precision_score(y_train,y_train_pred,average='weighted')
model_train_recall=recall_score(y_train,y_train_pred,average='weighted')
#model_train_rocauc_score=roc_auc_score(y_train,y_train_pred,multi_class='ovo')
print(model_train_accuracy)
print(model_train_f1)
print(model_train_precision)
print(model_train_recall)
#print(model_train_rocauc_score)


# In[23]:


test=pd.read_csv('/Users/shubh/Downloads/testing.csv')
test


# In[24]:



test


# In[25]:


y_test=test['prognosis']
y_test


# In[26]:


X_test=test.drop('prognosis', axis=1)
X_test


# In[27]:


y_test_pred = te.predict(X_test.values) 


# In[28]:


print(y_test_pred)


# In[29]:


model_test_accuracy=accuracy_score(y_test,y_test_pred)
model_test_f1=f1_score(y_test,y_test_pred,average='weighted')
model_test_precision=precision_score(y_test,y_test_pred,average='weighted')
model_test_recall=recall_score(y_test,y_test_pred,average='weighted')
#model_train_rocauc_score=roc_auc_score(y_train,y_train_pred,multi_class='ovo')
print(model_test_accuracy)
print(model_test_f1)
print(model_test_precision)
print(model_test_recall)
#print(model_train_rocauc_score)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[44]:


#finding the best paramteres since the prediction on test data set is 100% accurate that means there is a problem of overfitting so finding best paramters for the model.


# In[45]:


#finding the best parameters for the model
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['auto', 'sqrt'],
    'bootstrap': [True, False]
}

 #Initialize the RandomForestClassifier
rf = RandomForestClassifier()

 #Perform grid search to find the best parameters
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5)
grid_search.fit(X_train.values, y_train.values.ravel())

 #Get the best parameters
best_params = grid_search.best_params_
print("Best Parameters:", best_params)


# In[171]:


ge= RandomForestClassifier(bootstrap=True, 
                            max_depth=None, 
                            max_features='sqrt', 
                            min_samples_leaf=1, 
                            min_samples_split=2, 
                            n_estimators=50)
ge = ge.fit(X_train.values,y_train.values.ravel())
with open('random_forest_model.pkl', 'wb') as f:
    pickle.dump(ge, f)


# In[50]:


y_train_preds = ge.predict(X_train.values)
print(y_train_preds)


# In[51]:


model_train_accuracy=accuracy_score(y_train,y_train_pred)
model_train_f1=f1_score(y_train,y_train_pred,average='weighted')
model_train_precision=precision_score(y_train,y_train_pred,average='weighted')
model_train_recall=recall_score(y_train,y_train_pred,average='weighted')
#model_train_rocauc_score=roc_auc_score(y_train,y_train_pred,multi_class='ovo')
print(model_train_accuracy)
print(model_train_f1)
print(model_train_precision)
print(model_train_recall)
#print(model_train_rocauc_score)


# In[52]:


y_test_preds = ge.predict(X_test.values) 


# In[53]:


print(y_test_preds)


# In[54]:


model_test_accuracys=accuracy_score(y_test,y_test_preds)
model_test_f1s=f1_score(y_test,y_test_preds,average='weighted')
model_test_precisions=precision_score(y_test,y_test_preds,average='weighted')
model_test_recalls=recall_score(y_test,y_test_preds,average='weighted')
#model_train_rocauc_score=roc_auc_score(y_train,y_train_pred,multi_class='ovo')
print(model_test_accuracys)
print(model_test_f1s)
print(model_test_precisions)
print(model_test_recalls)
#print(model_train_rocauc_score)


# In[55]:


from sklearn.naive_bayes import MultinomialNB
gnb=MultinomialNB()
gnb=gnb.fit(X_train.values,y_train.values.ravel())


# In[56]:


y_train_pred2 = gnb.predict(X_train.values)
print(y_train_pred2)


# In[57]:


model_train_accuracy2=accuracy_score(y_train,y_train_pred2)
model_train_f12=f1_score(y_train,y_train_pred2,average='weighted')
model_train_precision2=precision_score(y_train,y_train_pred2,average='weighted')
model_train_recall2=recall_score(y_train,y_train_pred2,average='weighted')
#model_train_rocauc_score=roc_auc_score(y_train,y_train_pred,multi_class='ovo')
print(model_train_accuracy2)
print(model_train_f12)
print(model_train_precision2)
print(model_train_recall2)
#print(model_train_rocauc_score)


# In[58]:


y_test_pred2 =gnb.predict(X_test.values) 
print(y_test_pred2)


# In[59]:


model_test_accuracy2=accuracy_score(y_test,y_test_pred2)
model_test_f12=f1_score(y_test,y_test_pred2,average='weighted')
model_test_precision2=precision_score(y_test,y_test_pred2,average='weighted')
model_test_recall2=recall_score(y_test,y_test_pred2,average='weighted')
#model_train_rocauc_score=roc_auc_score(y_train,y_train_pred,multi_class='ovo')
print(model_test_accuracy2)
print(model_test_f12)
print(model_test_precision2)
print(model_train_recall2)
#print(model_train_rocauc_score)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[126]:


# Define the parameter grid
param_grid2 = {'alpha': [0.1, 0.5, 1.0, 5.0, 10.0]}

# Initialize the MultinomialNB classifier
mnb = MultinomialNB()

# Perform grid search to find the best parameters
grid_search2 = GridSearchCV(estimator=mnb, param_grid=param_grid2, cv=5)
grid_search2.fit(X_train.values, y_train.values.ravel())

# Get the best parameters and best score
best_params2 = grid_search2.best_params_
best_score2 = grid_search2.best_score_

print("Best Parameters:", best_params2)
print("Best Score:", best_score2)


# In[172]:


mnb=MultinomialNB(alpha= 0.1)
mnb=mnb.fit(X_train.values,y_train.values.ravel())
with open('multinomial_nb_model.pkl', 'wb') as f:
    pickle.dump(mnb, f)


# In[62]:


y_train_pred2s = mnb.predict(X_train.values)
print(y_train_pred2s)


# In[63]:


model_train_accuracy2s=accuracy_score(y_train,y_train_pred2s)
model_train_f12s=f1_score(y_train,y_train_pred2s,average='weighted')
model_train_precision2s=precision_score(y_train,y_train_pred2s,average='weighted')
model_train_recall2s=recall_score(y_train,y_train_pred2s,average='weighted')
#model_train_rocauc_score=roc_auc_score(y_train,y_train_pred,multi_class='ovo')
print(model_train_accuracy2s)
print(model_train_f12s)
print(model_train_precision2s)
print(model_train_recall2s)


# In[64]:


y_test_pred2s =mnb.predict(X_test.values) 
print(y_test_pred2s)


# In[65]:


model_test_accuracy2s=accuracy_score(y_test,y_test_pred2s)
model_test_f12s=f1_score(y_test,y_test_pred2s,average='weighted')
model_test_precision2s=precision_score(y_test,y_test_pred2s,average='weighted')
model_test_recall2s=recall_score(y_test,y_test_pred2s,average='weighted')
#model_train_rocauc_score=roc_auc_score(y_train,y_train_pred,multi_class='ovo')
print(model_test_accuracy2s)
print(model_test_f12s)
print(model_test_precision2s)
print(model_train_recall2s)
#print(model_train_rocauc_score)


# In[66]:


from sklearn import svm
clf=svm.SVC(kernel='linear',C=1)
clf.fit(X_train.values,y_train.values.ravel())


# In[67]:


y_train_pred3 = clf.predict(X_train.values)
print(y_train_pred3)


# In[68]:


model_train_accuracy3=accuracy_score(y_train,y_train_pred3)
model_train_f13=f1_score(y_train,y_train_pred3,average='weighted')
model_train_precision3=precision_score(y_train,y_train_pred3,average='weighted')
model_train_recall3=recall_score(y_train,y_train_pred3,average='weighted')
#model_train_rocauc_score=roc_auc_score(y_train,y_train_pred,multi_class='ovo')
print(model_train_accuracy3)
print(model_train_f13)
print(model_train_precision3)
print(model_train_recall3)
#print(model_train_rocauc_score)


# In[69]:


y_test_pred3 =clf.predict(X_test.values) 
print(y_test_pred3)


# In[145]:


model_test_accuracy3=accuracy_score(y_test,y_test_pred3)
model_test_f13=f1_score(y_test,y_test_pred3,average='weighted')
model_test_precision3=precision_score(y_test,y_test_pred3,average='weighted')
model_test_recall3=recall_score(y_test,y_test_pred3,average='weighted')
#model_train_rocauc_score=roc_auc_score(y_train,y_train_pred,multi_class='ovo')
print(model_test_accuracy3)
print(model_test_f13)
print(model_test_precision3)
print(model_test_recall3)
#print(model_train_rocauc_score)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[136]:


from sklearn.model_selection import GridSearchCV
from sklearn import svm

# Define the expanded parameter grid
#param_grid3 = {  
   # 'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000],  
   # 'kernel': ['linear', 'poly', 'rbf', 'sigmoid'],
   # 'gamma': ['scale', 'auto'],  # 'scale' is default; 'auto' uses 1 / n_features
   # 'degree': [2, 3, 4, 5],  # Only applicable for poly kernel
    #'coef0': [0.0, 0.1, 0.5, 1.0]  # Only applicable for poly and sigmoid kernels
#}

# Initialize the SVM classifier
#svm_classifier = svm.SVC()

# Perform grid search to find the best parameters
#grid_search3 = GridSearchCV(estimator=svm_classifier, param_grid=param_grid3, cv=5)
#grid_search3.fit(X_train.values, y_train.values.ravel())

# Get the best parameters and best score
#best_params3 = grid_search3.best_params_
#best_score3= grid_search3.best_score_

#print("Best Parameters:", best_params3)
#print("Best Score:", best_score3)


# In[104]:


#from sklearn.model_selection import RandomizedSearchCV
##from sklearn import svm
#from scipy.stats import uniform

# Define the parameter distribution
#param_dist4 = {
    #'C': uniform(0.001, 1000),  # Uniform distribution over a wide range
    #'gamma': ['scale', 'auto'] + list(uniform(0.001, 10).rvs(10)),  # Scale and auto, plus random values
    #'kernel': ['linear', 'poly', 'rbf', 'sigmoid']
#}

# Initialize the SVM classifier
##svm_classifier = svm.SVC()

# Perform random search to find the best parameters
##random_search4 = RandomizedSearchCV(estimator=svm_classifier, param_distributions=param_dist4, n_iter=100, cv=5)
#random_search4.fit(X_train.values, y_train.values.ravel())

# Get the best parameters and best score
#best_params4 = random_search4.best_params_
#best_score4 = random_search4.best_score_

#print("Best Parameters:", best_params4)
#print("Best Score:", best_score4)


# In[173]:


from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from bayes_opt import BayesianOptimization

# Define the objective function to optimize
def svm_cv_accuracy(C, gamma):
    svm_model = SVC(C=C, gamma=gamma, kernel='rbf')
    svm_model.fit(X_train.values, y_train.values.ravel())
    y_pred = svm_model.predict(X_test.values)
    return accuracy_score(y_test.values.ravel(), y_pred)

# Define the search space for hyperparameters
pbounds = {'C': (0.001, 100), 'gamma': (0.0001, 10)}

# Initialize Bayesian optimization
optimizer = BayesianOptimization(
    f=svm_cv_accuracy,
    pbounds=pbounds,
    random_state=42,
)

# Perform optimization
optimizer.maximize(
    init_points=10,  # Number of initial random points
    n_iter=20,  # Number of optimization iterations
)

# Get the best hyperparameters
best_params = optimizer.max['params']
best_C = best_params['C']
best_gamma = best_params['gamma']

print("Best Hyperparameters:", best_params)

# Train the final SVM model with the best hyperparameters
final_svm_model = SVC(C=best_C, gamma=best_gamma, kernel='rbf')
final_svm_model.fit(X_train.values, y_train.values.ravel())

# Evaluate the final model on the test set
y_test_pred3s = final_svm_model.predict(X_test.values)
test_accuracy = accuracy_score(y_test,y_test_pred3s)
print("Test Accuracy:", test_accuracy)
with open('svm_model.pkl', 'wb') as f:
    pickle.dump(final_svm_model, f)


# In[140]:


#from sklearn import svm

# Initialize the SVM classifier with the best parameters
##het = svm.SVC(C= 0.001, coef0= 0.0, degree= 2, gamma='scale', kernel= 'linear')

# Fit the classifier to the training data
#het.fit(X_train.values, y_train.values.ravel())


# In[97]:


#from sklearn.feature_selection import RFE

# Initialize SVM classifier
#svm_classifier = svm.SVC(C=0.001, coef0=0.0, degree=2, gamma='scale', kernel='linear')

# Perform feature selection with RFE
#rfe = RFE(estimator=svm_classifier, n_features_to_select=10, step=1)
#rfe.fit(X_train.values, y_train.values.ravel())

# Select features based on RFE
#X_train_selected = rfe.transform(X_train.values)
#X_test_selected = rfe.transform(X_test.values)

# Fit the classifier to the selected features
#svm_classifier.fit(X_train_selected, y_train.values.ravel())


# In[148]:


y_train_pred3s = final_svm_model.predict(X_train.values)
print(y_train_pred3s)


# In[149]:


model_train_accuracy3s=accuracy_score(y_train,y_train_pred3s)
model_train_f13s=f1_score(y_train,y_train_pred3s,average='weighted')
model_train_precision3s=precision_score(y_train,y_train_pred3s,average='weighted')
model_train_recall3s=recall_score(y_train,y_train_pred3s,average='weighted')
#model_train_rocauc_score=roc_auc_score(y_train,y_train_pred,multi_class='ovo')
print(model_train_accuracy3s)
print(model_train_f13s)
print(model_train_precision3s)
print(model_train_recall3s)
#print(model_train_rocauc_score)


# In[150]:


y_test_pred3ss =final_svm_model.predict(X_test.values) 
print(y_test_pred3ss)


# In[151]:


model_test_accuracy3s=accuracy_score(y_test,y_test_pred3ss)
model_test_f13s=f1_score(y_test,y_test_pred3ss,average='weighted')
model_test_precision3s=precision_score(y_test,y_test_pred3ss,average='weighted')
model_test_recall3s=recall_score(y_test,y_test_pred3ss,average='weighted')
#model_train_rocauc_score=roc_auc_score(y_train,y_train_pred,multi_class='ovo')
print(model_test_accuracy3s)
print(model_test_f13s)
print(model_test_precision3s)
print(model_test_recall3s)
#print(model_train_rocauc_score)


# In[ ]:


#logistic regression


# In[122]:


from sklearn.linear_model import LogisticRegression


# In[129]:


lrr=LogisticRegression()
lrr.fit(X_train.values, y_train.values.ravel())


# In[130]:


y_train_pred4 = lrr.predict(X_train.values)
print(y_train_pred4)
model_train_accuracy4=accuracy_score(y_train,y_train_pred4)
model_train_f14=f1_score(y_train,y_train_pred4,average='weighted')
model_train_precision4=precision_score(y_train,y_train_pred4,average='weighted')
model_train_recall4=recall_score(y_train,y_train_pred4,average='weighted')
#model_train_rocauc_score=roc_auc_score(y_train,y_train_pred,multi_class='ovo')
print(model_train_accuracy4)
print(model_train_f14)
print(model_train_precision4)
print(model_train_recall4)
#print(model_train_rocauc_score)


# In[131]:


y_test_pred4 =lrr.predict(X_test.values) 
print(y_test_pred4)
model_test_accuracy4=accuracy_score(y_test,y_test_pred4)
model_test_f14=f1_score(y_test,y_test_pred4,average='weighted')
model_test_precision4=precision_score(y_test,y_test_pred4,average='weighted')
model_test_recall4=recall_score(y_test,y_test_pred4,average='weighted')
#model_train_rocauc_score=roc_auc_score(y_train,y_train_pred,multi_class='ovo')
print(model_test_accuracy4)
print(model_test_f14)
print(model_test_precision4)
print(model_test_recall4)
#print(model_train_rocauc_score)


# In[132]:


from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression

# Define the parameter grid
param_grid5 = {
    'C': [0.001, 0.01, 0.1, 1, 10, 100],  # Regularization strength
    'penalty': ['l1', 'l2'],  # Penalty type
    'solver': ['liblinear', 'saga']  # Solver algorithm
}

# Initialize the logistic regression classifier
log_reg = LogisticRegression()

# Perform grid search to find the best parameters
grid_search5 = GridSearchCV(estimator=log_reg, param_grid=param_grid5, cv=5)
grid_search5.fit(X_train.values, y_train.values.ravel())

# Get the best parameters and best score
best_params5= grid_search5.best_params_
best_score5= grid_search5.best_score_

print("Best Parameters:", best_params5)
print("Best Score:", best_score5)


# In[174]:


lrrs=LogisticRegression(C=0.001, penalty='l2', solver= 'liblinear')
lrrs.fit(X_train.values, y_train.values.ravel())
with open('logistic_regression_model.pkl', 'wb') as f:
    pickle.dump(lrrs, f)


# In[175]:


y_train_pred4s= lrrs.predict(X_train.values)
print(y_train_pred4s)
model_train_accuracy4s=accuracy_score(y_train,y_train_pred4s)
model_train_f14s=f1_score(y_train,y_train_pred4s,average='weighted')
model_train_precision4s=precision_score(y_train,y_train_pred4s,average='weighted')
model_train_recall4s=recall_score(y_train,y_train_pred4s,average='weighted')
#model_train_rocauc_score=roc_auc_score(y_train,y_train_pred,multi_class='ovo')
print(model_train_accuracy4s)
print(model_train_f14s)
print(model_train_precision4s)
print(model_train_recall4s)
#print(model_train_rocauc_score)


# In[176]:


y_test_pred4s =lrrs.predict(X_test.values) 
print(y_test_pred4s)
model_test_accuracy4s=accuracy_score(y_test,y_test_pred4s)
model_test_f14s=f1_score(y_test,y_test_pred4s,average='weighted')
model_test_precision4s=precision_score(y_test,y_test_pred4s,average='weighted')
model_test_recall4s=recall_score(y_test,y_test_pred4s,average='weighted')
#model_train_rocauc_score=roc_auc_score(y_train,y_train_pred,multi_class='ovo')
print(model_test_accuracy4s)
print(model_test_f14s)
print(model_test_precision4s)
print(model_test_recall4s)
#print(model_train_rocauc_score)


# In[155]:


#Now using the concept of ensemble learning
#stacking_features = np.column_stack((y_test_preds, y_test_pred2s, y_test_pred3ss, y_test_pred4s, X_test.values))


# In[156]:


#stacking_features


# In[157]:


#meta_learner = LogisticRegression(C=0.001, penalty='l2', solver= 'liblinear')
#meta_learner.fit(stacking_features, y_test.values.ravel())


# In[159]:
#meta_preds = meta_learner.predict(stacking_features)

# Evaluate the performance of the meta-learner's predictions
#meta_accuracy = accuracy_score(y_test, meta_preds)
#print("Meta-Learner Accuracy:", meta_accuracy)
# In[160]:


import numpy as np

# Make predictions on validation/test data using the four models
y_test_preds
y_test_pred2s
y_test_pred3ss
y_test_pred4s


# Compute model performance metrics on the validation/test data (e.g., accuracy)
model_test_accuracys=accuracy_score(y_test,y_test_preds)
model_test_accuracy2s=accuracy_score(y_test,y_test_pred2s)
model_test_accuracy3s=accuracy_score(y_test,y_test_pred3ss)
model_test_accuracy4s=accuracy_score(y_test,y_test_pred4s)

#performing ensemble learning
voting_classifier = VotingClassifier(estimators=[('rf', te), 
                                                 ('lr', lrrs), 
                                                 ('nb', mnb),
                                                 ('svm', final_svm_model)], 
                                     voting='hard'
                                     )
voting_classifier.fit(X_train.values, y_train.values.ravel())
predictions = voting_classifier.predict(X_test.values)
emodel_test_accuracy=accuracy_score(y_test,predictions)
emodel_test_f1=f1_score(y_test,predictions,average='weighted')
emodel_test_precision=precision_score(y_test,predictions,average='weighted')
emodel_test_recall=recall_score(y_test,predictions,average='weighted')
conf_matrix = confusion_matrix(y_test, predictions)
print("Confusion Matrix:\n", conf_matrix)
print(emodel_test_accuracy)
print(emodel_test_f1)
print(emodel_test_precision)
print(emodel_test_recall)
with open('voting_classifier_model.pkl', 'wb') as f:
    pickle.dump(voting_classifier, f)







