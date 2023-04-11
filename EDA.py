import streamlit as st
import pandas as pd
import seaborn as sns
#Title and Subheader
st.title("Data Analytics")
st.subheader("Data anlysis using python & streamlit")
#File uploading command
data=st.file_uploader("Upload your dataset in CSV format ")
if data is not None:
    df1=pd.read_csv(data)
#Show the dataset   
if data is not None:    
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(df1.head())
        if st.button('Tail'):
            st.write(df1.tail())
#Datatype of the dataset
if data is not None:
    if st.checkbox("DataType of each column"):
        st.text("DataTypes")
        st.write(df1.dtypes)        
        
#shape of the dataset
if data is not None:
    if st.checkbox("Shape of the dataset"):
        st.text('shape')
        st.write(df1.shape)
                
# find the null values in the dataset
if data is not None:
    if st.checkbox("null values"):
        st.text("null values")
        st.write(df1.isnull())
        st.write("no of null values columns",df1.isnull().sum())
        st.write("no of null values row wise",df1.isnull().sum(axis=1))
        
#Null values heatmap
if data is not None:
    test=df1.isnull().values.any()
    if test == True:
        if st.checkbox('Null values in the dataset'):
            sns.heatmap(df1.isnull())
            st.pyplot()
else:
    st.success("congratualation no values")            
            
    
    
 #Find the duplicate value in the dataset
if data is not None:
    test=df1.duplicated().any()
    if test==True:
        st.warning("Having duplicated values")
        dup=st.selectbox("do you want to remove duplicate values",\
                         ("select One","yes","no"))
        if dup== "yes":
            df1=df1.drop_duplicates()
            st.text("Duplicates cvalues are removed")
        if dup=="no":
            st.text("Ok no problem")
 
#Get overall statistics
if data is not None:
    if st.checkbox("Statistics"):
        st.text("statistics of numeric column only")
        st.write(df1.describe())
        st.text("statistics of every column")
        st.write(df1.describe(include='all'))
        
#About section 
if st.button("About App"):
    st.text("Built by Streamlit")
    st.text("Thanks to Streamlit")
#By
if st.checkbox("By"):
    st.success("Kumar Aditya")    
            