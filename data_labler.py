import streamlit as st 
import numpy as np 
import pandas as pd
import os
from datetime import datetime



st.title('Create dataset for budgeting app')
path = os.getcwd()



with st.sidebar:
    add_radio = st.radio(
        "Home Menu",
        ("Add entry", "View Entry")
    )

if add_radio=="Add entry":
    type_obj = st.radio(label='Do you want to upload or take picture',options =['upload','take picture'])
    if type_obj=='take picture':
        pic = st.camera_input("Click image (preferable with product identification features included in picture)")
        cost = st.number_input("What is the cost of item")
        pic_description = st.text_input("Add description of item")
        click_pic_button = st.button("Submit")
        if click_pic_button ==True:
            click_button_click_time = datetime.now()
            img_path = path + "/tagged_data/"+pic_description+"_"+str(int(cost))+"_"+str(click_button_click_time)+".jpg"
            #pic = pic.save(img_path)
            pic_bytes = pic.read()
            with open(img_path, 'wb') as f: 
                f.write(pic_bytes)
            
            if os.path.isfile(path+"/expense.csv"):
                df = pd.read_csv(path+"/expense.csv")

            else:
                print(datetime.now())
                print("Creating new df")
                df = pd.DataFrame(columns=['datetime','type','cost','description','image_path'])
            df.loc[len(df.index)] = [click_button_click_time, 'shopping',cost,pic_description,img_path]
            df.to_csv(path+"expense.csv")
            st.text(pic_description+" worth "+str(int(cost))+ " added to budget under shopping category")
    elif type_obj=='upload':
        pic = st.file_uploader("Upload image (preferable with product identification features included in picture)")
        cost = st.number_input("What is the cost of item")
        pic_description = st.text_input("Add description of item")
        upload_pic_button = st.button("Submit")
        if upload_pic_button ==True:
            upload_button_click_time = datetime.now()
            img_path = path + "/tagged_data/"+pic_description+"_"+str(int(cost))+"_"+str(upload_button_click_time)+".jpg"
            pic_bytes = pic.read()
            with open(img_path, 'wb') as f: 
                f.write(pic_bytes)
            #pic = pic.save(img_path)
            if os.path.isfile(path+"/expense.csv"):
                df = pd.read_csv(path+"/expense.csv")

            else:
                print(datetime.now())
                print("Creating new df")
                df = pd.DataFrame(columns=['datetime','type','cost','description','image_path'])
            df.loc[len(df.index)] = [upload_button_click_time, 'shopping',cost,pic_description,img_path]
            x = df.to_csv(path+"/expense.csv",index=False)
            st.text(pic_description+" worth "+str(int(cost))+ " added to budget under shopping category")
if add_radio=="View Entry":
    df = pd.read_csv(path+"/expense.csv")
    st.dataframe(df)


