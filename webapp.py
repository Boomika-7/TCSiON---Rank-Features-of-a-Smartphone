# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 15:20:08 2022

@author: Boomika
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model=pickle.load(open('D:/TCSiON/trained_model.sav','rb'))

#creating a function
def ranking(input_data):
    input_array=np.array(input_data)
    input_reshape=input_array.reshape(1,-1)
    prediction=loaded_model.predict(input_reshape)
    return prediction

def main():
    
    #title
    st.title("Rank Features of a smartphone")
    
    #getting input 
    battery_power=st.text_input("Battery Power:")
    blue=st.text_input("Bluetooth (yes=1,no=0):")
    clock_speed=st.text_input("Clock speed:")
    dual_sim=st.text_input("Dual Sim (yes=1,no=0):")
    fc=st.text_input("Front Camera (in mp):")
    four_g=st.text_input("4G (yes=1,no=0):")
    int_memory=st.text_input("Internal Memory (in gb):")
    m_dep=st.text_input("Mobile Depth (in cm):")
    mobile_wt=st.text_input("Mobile weight (in g):")
    n_cores=st.text_input("Number of cores of processor:")
    pc=st.text_input("Primary Camera (in mp):")
    px_height=st.text_input("Pixel Resolution Height:")
    px_width=st.text_input("Pixel Resolution Width:")
    ram=st.text_input("RAM (in mb):")
    sc_h=st.text_input("Screen Height of mobile (in cm):")
    sc_w=st.text_input("Screen Width of mobile (in cm):")
    talk_time=st.text_input("longest time that a single battery charge will last:")
    three_g=st.text_input("3G (yes=1,no=0):")
    touch_screen=st.text_input("Touch Screen (yes=1,no=0):")
    wifi=st.text_input("Wifi (yes=1,no=0):")
    
    #code for prediction
    features=''
    
    #creating button
    if st.button("Prediction Result(Ranking 0-4):"):
        features=ranking([battery_power,blue,clock_speed,dual_sim,fc,four_g,int_memory,m_dep,mobile_wt,n_cores,pc,px_height,px_width,ram,
                          sc_h,sc_w,talk_time,three_g,touch_screen,wifi])
        print(features)
        
    st.success(features)
    
if __name__ == '__main__':
    main()