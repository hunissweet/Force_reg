from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import os
import glob
import numpy as np
import time
import pickle
from statistics import mean













def plotting_Normal_Force(pickle_path,save_name,save_fig,i,Title,NAME_LABEL,Color):
    with open(pickle_path, 'rb') as pickle_file:
        loaded_data = pickle.load(pickle_file)
    Time1=loaded_data['Time1']
    Time2=loaded_data['Time2']
    Time3=loaded_data['Time3']
    TOTAL1=loaded_data['TOTAL1']
    TOTAL2=loaded_data['TOTAL2']
    TOTAL3=loaded_data['TOTAL3']
    DATA_NAME1=loaded_data['DATA_NAME1']
    DATA_NAME2=loaded_data['DATA_NAME2']
    DATA_NAME3=loaded_data['DATA_NAME3']
    Slip_point1=loaded_data['Slip_point1']
    Slip_point2=loaded_data['Slip_point2']
    Slip_point3=loaded_data['Slip_point3']
    #NAME_LABEL=loaded_data['NAME_LABEL']
    ##
    
    ICRA_plotting_force(save_name,save_fig,Time1,TOTAL1, DATA_NAME1,Slip_point1,Time2,TOTAL2, DATA_NAME2,Slip_point2,Time3,TOTAL3, DATA_NAME3,Slip_point3,NAME_LABEL,i,Title,Color)
    
def ICRA_plotting_force(save_name,save_fig,Time1,TOTAL1, DATA_NAME1,Slip_point1,Time2,TOTAL2, DATA_NAME2,Slip_point2,Time3,TOTAL3, DATA_NAME3,Slip_point3,NAME_LABEL,i,Title,Color):
    '''
    Arag
    '''
    p1=round(len(Time1)/2*2.5/22)
    p2=round(len(Time2)/2*2.5/22)
    p3=round(len(Time3)/2*2.5/22)
    
    q1=round(len(Time1)/2*10/22)
    q2=round(len(Time2)/2*10/22)
    q3=round(len(Time3)/2*10/22)
    
    '''
    plt.figure()
    plt.subplot(1,3,1)
    plt.scatter(TOTAL1[1][2][:p1],TOTAL1[2][2][:p1],c='blue',alpha=0.2,label=NAME_LABEL[0]) # Fy, FZ
    plt.scatter(TOTAL2[1][2][:p2],TOTAL2[2][2][:p2],c='orange',alpha=0.2,label=NAME_LABEL[1])
    plt.scatter(TOTAL3[1][2][:p3],TOTAL3[2][2][:p3],c='black',alpha=0.2,label=NAME_LABEL[2])
    plt.legend(fontsize="11",loc='upper left')
    plt.xlabel('Fy')
    plt.ylabel('Fz')
    plt.xlim((0, 20))
    plt.ylim((-10, 10))
    plt.grid()
    plt.subplot(1,3,2)
    plt.scatter(TOTAL1[1][2][p1:q1],TOTAL1[2][2][p1:q1],c='blue',alpha=0.2,label=NAME_LABEL[0]) # Fy, FZ
    plt.scatter(TOTAL2[1][2][p2:q2],TOTAL2[2][2][p2:q2],c='orange',alpha=0.2,label=NAME_LABEL[1])
    plt.scatter(TOTAL3[1][2][p3:q3],TOTAL3[2][2][p3:q3],c='black',alpha=0.2,label=NAME_LABEL[2])
    plt.legend(fontsize="11",loc='upper left')
    plt.xlim((0, 20))
    plt.ylim((-10, 10))
    plt.xlabel('Fy')
    plt.ylabel('Fz')
    plt.grid()
    
    plt.subplot(1,3,3)
    plt.scatter(TOTAL1[1][2][q1:],TOTAL1[2][2][q1:],c='blue',alpha=0.2,label=NAME_LABEL[0]) # Fy, FZ
    plt.scatter(TOTAL2[1][2][q2:],TOTAL2[2][2][q2:],c='orange',alpha=0.2,label=NAME_LABEL[1])
    plt.scatter(TOTAL3[1][2][q3:],TOTAL3[2][2][q3:],c='black',alpha=0.2,label=NAME_LABEL[2])
    plt.legend(fontsize="11",loc='upper left')
    plt.xlim((0, 20))
    plt.ylim((-10, 10))
    plt.xlabel('Fy')
    plt.ylabel('Fz')
    plt.grid()
    
    lw=1.5
    leng1=round(len(Time1)/2)
    leng2=round(len(Time2)/2)
    leng3=round(len(Time3)/2)
    plt.xlim((0, 20))
    plt.ylim((-10, 10))
    plt.figure()
    plt.subplot(3,1,1)

    plt.plot(Time3[:leng3]*pow(10,-9), TOTAL3[0][2][:leng3], label=NAME_LABEL[2], color=Color,linestyle='solid',lw=lw)
    #plt.fill_between(Time1[:leng1]*pow(10,-9), TOTAL1[i][1][:leng1], TOTAL1[i][0][:leng1], alpha=0.4, color='blue',linestyle='solid',lw=lw)
    plt.plot(Time2[:leng2]*pow(10,-9), TOTAL2[0][2][:leng2], label=NAME_LABEL[1], color=Color,linestyle='dashed',lw=lw)
    #plt.fill_between(Time3[:leng3]*pow(10,-9), TOTAL3[i][1][:leng3], TOTAL3[i][0][:leng3], alpha=0.4, color='blue',linestyle='dotted',lw=lw)
    plt.plot(Time1[:leng1]*pow(10,-9), TOTAL1[0][2][:leng1], label=NAME_LABEL[0], color=Color,linestyle='dotted',lw=lw)
    #plt.fill_between(Time2[:leng2]*pow(10,-9), TOTAL2[i][1][:leng2], TOTAL2[i][0][:leng2], alpha=0.4, color='blue',linestyle='dashed',lw=lw)
    moving=Slip_point3[0]*pow(10,-9)
    plt.vlines(x = moving,ymin = 20, ymax =0,color = 'black',linewidth = 1, linestyle ="--")
    plt.xlabel('Time[s]',fontsize="11")
    plt.xticks(ticks=[0,moving,5,10,15,20],labels=[0,'Move',5,10,15,20],fontsize="11")
    plt.yticks(ticks=[0,5,10,15,20],fontsize="11")
    plt.ylim((-0.5, 20))
    plt.ylabel('Friction')
    plt.subplot(3,1,2)
'''

    lw=1.5
    leng1=round(len(Time1)/2)
    leng2=round(len(Time2)/2)
    leng3=round(len(Time3)/2)
    plt.figure(figsize=(20,4))
    plt.subplot(1,5,1)#y
    plt.title('Fy')
    plt.plot(Time1[:leng1]*pow(10,-9), TOTAL1[1][2][:leng1], label=NAME_LABEL[2], color=Color,linestyle='solid',lw=lw)
    #plt.fill_between(Time1[:leng1]*pow(10,-9), TOTAL1[i][1][:leng1], TOTAL1[i][0][:leng1], alpha=0.4, color='blue',linestyle='solid',lw=lw)
    plt.plot(Time3[:leng3]*pow(10,-9), TOTAL3[1][2][:leng3], label=NAME_LABEL[1], color=Color,linestyle='dashed',lw=lw)
    #plt.fill_between(Time3[:leng3]*pow(10,-9), TOTAL3[i][1][:leng3], TOTAL3[i][0][:leng3], alpha=0.4, color='blue',linestyle='dotted',lw=lw)
    plt.plot(Time2[:leng2]*pow(10,-9), TOTAL2[1][2][:leng2], label=NAME_LABEL[0], color=Color,linestyle='dotted',lw=lw)
    #plt.fill_between(Time2[:leng2]*pow(10,-9), TOTAL2[i][1][:leng2], TOTAL2[i][0][:leng2], alpha=0.4, color='blue',linestyle='dashed',lw=lw)
    plt.legend(fontsize="11",loc='upper right')
    plt.subplot(1,5,2)#z
    plt.title('Fz')
    plt.plot(Time1[:leng1]*pow(10,-9), TOTAL1[2][2][:leng1], label=NAME_LABEL[2], color=Color,linestyle='solid',lw=lw)
    #plt.fill_between(Time1[:leng1]*pow(10,-9), TOTAL1[i][1][:leng1], TOTAL1[i][0][:leng1], alpha=0.4, color='blue',linestyle='solid',lw=lw)
    plt.plot(Time3[:leng3]*pow(10,-9), TOTAL3[2][2][:leng3], label=NAME_LABEL[1], color=Color,linestyle='dashed',lw=lw)
    #plt.fill_between(Time3[:leng3]*pow(10,-9), TOTAL3[i][1][:leng3], TOTAL3[i][0][:leng3], alpha=0.4, color='blue',linestyle='dotted',lw=lw)
    plt.plot(Time2[:leng2]*pow(10,-9), TOTAL2[2][2][:leng2], label=NAME_LABEL[0], color=Color,linestyle='dotted',lw=lw)
    #plt.fill_between(Time2[:leng2]*pow(10,-9), TOTAL2[i][1][:leng2], TOTAL2[i][0][:leng2], alpha=0.4, color='blue',linestyle='dashed',lw=lw)
    plt.legend(fontsize="11",loc='upper right')
    plt.subplot(1,5,3)#normal
    plt.title('normal')
    plt.plot(Time1[:leng1]*pow(10,-9), np.sqrt((TOTAL1[1][2])*(TOTAL1[1][2])+(TOTAL1[2][2])*(TOTAL1[2][2]))[:leng1], label=NAME_LABEL[2], color=Color,linestyle='solid',lw=lw)
    #plt.fill_between(Time1[:leng1]*pow(10,-9), np.sqrt((TOTAL1[1][1])*(TOTAL1[1][1])+(TOTAL1[2][1])*(TOTAL1[2][1]))[:leng1], np.sqrt((TOTAL1[1][0])*(TOTAL1[1][0])+(TOTAL1[2][0])*(TOTAL1[2][0]))[:leng1], alpha=0.4, color='blue')
    plt.plot(Time3[:leng3]*pow(10,-9), np.sqrt((TOTAL3[1][2])*(TOTAL3[1][2])+(TOTAL3[2][2])*(TOTAL3[2][2]))[:leng3], label=NAME_LABEL[1], color=Color,linestyle='dashed',lw=lw)
    #plt.fill_between(Time3[:leng3]*pow(10,-9),  np.sqrt((TOTAL3[1][1])*(TOTAL3[1][1])+(TOTAL3[2][1])*(TOTAL3[2][1]))[:leng3], np.sqrt((TOTAL3[1][0])*(TOTAL3[1][0])+(TOTAL3[2][0])*(TOTAL3[2][0]))[:leng3], alpha=0.4, color='black')
    plt.plot(Time2[:leng2]*pow(10,-9), np.sqrt((TOTAL2[1][2])*(TOTAL2[1][2])+(TOTAL2[2][2])*(TOTAL2[2][2]))[:leng2], label=NAME_LABEL[0], color=Color,linestyle='dotted',lw=lw)
    #plt.fill_between(Time2[:leng2]*pow(10,-9),  np.sqrt((TOTAL2[1][1])*(TOTAL2[1][1])+(TOTAL2[2][1])*(TOTAL2[2][1]))[:leng2], np.sqrt((TOTAL2[1][0])*(TOTAL2[1][0])+(TOTAL2[2
    plt.legend(fontsize="11",loc='upper right')
    
    plt.subplot(1,5,4)#Tangential
    plt.title('Tangential, Fx')
    plt.plot(Time1[:leng1]*pow(10,-9), TOTAL1[0][2][:leng1], label=NAME_LABEL[2], color=Color,linestyle='solid',lw=lw)
    #plt.fill_between(Time1[:leng1]*pow(10,-9), TOTAL1[i][1][:leng1], TOTAL1[i][0][:leng1], alpha=0.4, color='blue',linestyle='solid',lw=lw)
    plt.plot(Time3[:leng3]*pow(10,-9), TOTAL3[0][2][:leng3], label=NAME_LABEL[1], color=Color,linestyle='dashed',lw=lw)
    #plt.fill_between(Time3[:leng3]*pow(10,-9), TOTAL3[i][1][:leng3], TOTAL3[i][0][:leng3], alpha=0.4, color='blue',linestyle='dotted',lw=lw)
    plt.plot(Time2[:leng2]*pow(10,-9), TOTAL2[0][2][:leng2], label=NAME_LABEL[0], color=Color,linestyle='dotted',lw=lw)
    #plt.fill_between(Time2[:leng2]*pow(10,-9), TOTAL2[i][1][:leng2], TOTAL2[i][0][:leng2], alpha=0.4, color='blue',linestyle='dashed',lw=lw)
    plt.legend(fontsize="11",loc='upper right')
    plt.subplot(1,5,5)#coeffi
    plt.title('Fric_coeffi')
    leng1=round(len(Time1)/2)
    leng2=round(len(Time2)/2)
    leng3=round(len(Time3)/2)

    TEMP_Fc1=TOTAL1[0][2]/np.sqrt((TOTAL1[1][2])*(TOTAL1[1][2])+(TOTAL1[2][2])*(TOTAL1[2][2]))
    TEMP_Fc2=TOTAL2[0][2]/np.sqrt((TOTAL2[1][2])*(TOTAL2[1][2])+(TOTAL2[2][2])*(TOTAL2[2][2]))
    TEMP_Fc3=TOTAL3[0][2]/np.sqrt((TOTAL3[1][2])*(TOTAL3[1][2])+(TOTAL3[2][2])*(TOTAL3[2][2]))
    TOTAL_TEMP=TEMP_Fc1[:leng1],TEMP_Fc2[:leng1],TEMP_Fc3[:leng1]
    
    plt.plot(Time1[:leng1]*pow(10,-9), np.mean(np.array(TOTAL_TEMP), axis=0)[:leng1],label=NAME_LABEL[2],color=Color,linestyle='dashed') # mean value FX/ mean Value Fy
    plt.plot(Time1[:leng1]*pow(10,-9), np.max(np.array(TOTAL_TEMP), axis=0)[:leng1],label=NAME_LABEL[1],color=Color,linestyle='solid') # mean value FX/ mean Value Fy
    plt.plot(Time1[:leng1]*pow(10,-9), np.min(np.array(TOTAL_TEMP), axis=0)[:leng1],label=NAME_LABEL[0],color=Color,linestyle='dotted') # mean value FX/ mean Value Fy
    plt.legend(fontsize="11",loc='upper right') 
'''    
    if save_name=='Contact_area':
        plt.plot(Time1[:leng1]*pow(10,-9), np.sqrt((TOTAL1[1][2])*(TOTAL1[1][2])+(TOTAL1[2][2])*(TOTAL1[2][2]))[:leng1], label=NAME_LABEL[2], color=Color,linestyle='solid',lw=lw)
        #plt.fill_between(Time1[:leng1]*pow(10,-9), np.sqrt((TOTAL1[1][1])*(TOTAL1[1][1])+(TOTAL1[2][1])*(TOTAL1[2][1]))[:leng1], np.sqrt((TOTAL1[1][0])*(TOTAL1[1][0])+(TOTAL1[2][0])*(TOTAL1[2][0]))[:leng1], alpha=0.4, color='blue')
        plt.plot(Time2[:leng2]*pow(10,-9), np.sqrt((TOTAL2[1][2])*(TOTAL2[1][2])+(TOTAL2[2][2])*(TOTAL2[2][2]))[:leng2], label=NAME_LABEL[1], color=Color,linestyle='dashed',lw=lw)
        #plt.fill_between(Time3[:leng3]*pow(10,-9),  np.sqrt((TOTAL3[1][1])*(TOTAL3[1][1])+(TOTAL3[2][1])*(TOTAL3[2][1]))[:leng3], np.sqrt((TOTAL3[1][0])*(TOTAL3[1][0])+(TOTAL3[2][0])*(TOTAL3[2][0]))[:leng3], alpha=0.4, color='black')
        plt.plot(Time3[:leng3]*pow(10,-9), np.sqrt((TOTAL3[1][2])*(TOTAL3[1][2])+(TOTAL3[2][2])*(TOTAL3[2][2]))[:leng3], label=NAME_LABEL[0], color=Color,linestyle='dotted',lw=lw)
        #plt.fill_between(Time2[:leng2]*pow(10,-9),  np.sqrt((TOTAL2[1][1])*(TOTAL2[1][1])+(TOTAL2[2][1])*(TOTAL2[2][1]))[:leng2], np.sqrt((TOTAL2[1][0])*(TOTAL2[1][0])+(TOTAL2[2
        plt.legend(fontsize="11",loc='lower right')
    elif save_name=='OFF_Z':
        plt.figure(figsize=(20,5))
        plt.subplot(1,5,1)#y
        plt.title('Fy')
        plt.plot(Time1[:leng1]*pow(10,-9), TOTAL1[1][2][:leng1], label=NAME_LABEL[2], color=Color,linestyle='solid',lw=lw)
        #plt.fill_between(Time1[:leng1]*pow(10,-9), TOTAL1[i][1][:leng1], TOTAL1[i][0][:leng1], alpha=0.4, color='blue',linestyle='solid',lw=lw)
        plt.plot(Time3[:leng3]*pow(10,-9), TOTAL3[1][2][:leng3], label=NAME_LABEL[1], color=Color,linestyle='dashed',lw=lw)
        #plt.fill_between(Time3[:leng3]*pow(10,-9), TOTAL3[i][1][:leng3], TOTAL3[i][0][:leng3], alpha=0.4, color='blue',linestyle='dotted',lw=lw)
        plt.plot(Time2[:leng2]*pow(10,-9), TOTAL2[1][2][:leng2], label=NAME_LABEL[0], color=Color,linestyle='dotted',lw=lw)
        #plt.fill_between(Time2[:leng2]*pow(10,-9), TOTAL2[i][1][:leng2], TOTAL2[i][0][:leng2], alpha=0.4, color='blue',linestyle='dashed',lw=lw)
        plt.legend(fontsize="11",loc='upper right')
        plt.subplot(1,5,2)#z
        plt.title('Fz')
        plt.plot(Time1[:leng1]*pow(10,-9), TOTAL1[2][2][:leng1], label=NAME_LABEL[2], color=Color,linestyle='solid',lw=lw)
        #plt.fill_between(Time1[:leng1]*pow(10,-9), TOTAL1[i][1][:leng1], TOTAL1[i][0][:leng1], alpha=0.4, color='blue',linestyle='solid',lw=lw)
        plt.plot(Time3[:leng3]*pow(10,-9), TOTAL3[2][2][:leng3], label=NAME_LABEL[1], color=Color,linestyle='dashed',lw=lw)
        #plt.fill_between(Time3[:leng3]*pow(10,-9), TOTAL3[i][1][:leng3], TOTAL3[i][0][:leng3], alpha=0.4, color='blue',linestyle='dotted',lw=lw)
        plt.plot(Time2[:leng2]*pow(10,-9), TOTAL2[2][2][:leng2], label=NAME_LABEL[0], color=Color,linestyle='dotted',lw=lw)
        #plt.fill_between(Time2[:leng2]*pow(10,-9), TOTAL2[i][1][:leng2], TOTAL2[i][0][:leng2], alpha=0.4, color='blue',linestyle='dashed',lw=lw)
        plt.legend(fontsize="11",loc='upper right')
        plt.subplot(1,5,3)#normal
        plt.title('normal')
        plt.plot(Time1[:leng1]*pow(10,-9), np.sqrt((TOTAL1[1][2])*(TOTAL1[1][2])+(TOTAL1[2][2])*(TOTAL1[2][2]))[:leng1], label=NAME_LABEL[2], color=Color,linestyle='solid',lw=lw)
        #plt.fill_between(Time1[:leng1]*pow(10,-9), np.sqrt((TOTAL1[1][1])*(TOTAL1[1][1])+(TOTAL1[2][1])*(TOTAL1[2][1]))[:leng1], np.sqrt((TOTAL1[1][0])*(TOTAL1[1][0])+(TOTAL1[2][0])*(TOTAL1[2][0]))[:leng1], alpha=0.4, color='blue')
        plt.plot(Time3[:leng3]*pow(10,-9), np.sqrt((TOTAL3[1][2])*(TOTAL3[1][2])+(TOTAL3[2][2])*(TOTAL3[2][2]))[:leng3], label=NAME_LABEL[1], color=Color,linestyle='dashed',lw=lw)
        #plt.fill_between(Time3[:leng3]*pow(10,-9),  np.sqrt((TOTAL3[1][1])*(TOTAL3[1][1])+(TOTAL3[2][1])*(TOTAL3[2][1]))[:leng3], np.sqrt((TOTAL3[1][0])*(TOTAL3[1][0])+(TOTAL3[2][0])*(TOTAL3[2][0]))[:leng3], alpha=0.4, color='black')
        plt.plot(Time2[:leng2]*pow(10,-9), np.sqrt((TOTAL2[1][2])*(TOTAL2[1][2])+(TOTAL2[2][2])*(TOTAL2[2][2]))[:leng2], label=NAME_LABEL[0], color=Color,linestyle='dotted',lw=lw)
        #plt.fill_between(Time2[:leng2]*pow(10,-9),  np.sqrt((TOTAL2[1][1])*(TOTAL2[1][1])+(TOTAL2[2][1])*(TOTAL2[2][1]))[:leng2], np.sqrt((TOTAL2[1][0])*(TOTAL2[1][0])+(TOTAL2[2
        plt.legend(fontsize="11",loc='upper right')
        
        plt.subplot(1,5,4)#Tangential
        plt.title('Tangential')
        plt.plot(Time1[:leng1]*pow(10,-9), TOTAL1[0][2][:leng1], label=NAME_LABEL[2], color=Color,linestyle='solid',lw=lw)
        #plt.fill_between(Time1[:leng1]*pow(10,-9), TOTAL1[i][1][:leng1], TOTAL1[i][0][:leng1], alpha=0.4, color='blue',linestyle='solid',lw=lw)
        plt.plot(Time3[:leng3]*pow(10,-9), TOTAL3[0][2][:leng3], label=NAME_LABEL[1], color=Color,linestyle='dashed',lw=lw)
        #plt.fill_between(Time3[:leng3]*pow(10,-9), TOTAL3[i][1][:leng3], TOTAL3[i][0][:leng3], alpha=0.4, color='blue',linestyle='dotted',lw=lw)
        plt.plot(Time2[:leng2]*pow(10,-9), TOTAL2[0][2][:leng2], label=NAME_LABEL[0], color=Color,linestyle='dotted',lw=lw)
        #plt.fill_between(Time2[:leng2]*pow(10,-9), TOTAL2[i][1][:leng2], TOTAL2[i][0][:leng2], alpha=0.4, color='blue',linestyle='dashed',lw=lw)
        plt.legend(fontsize="11",loc='upper right')
        plt.subplot(1,5,5)#coeffi
        plt.title('Fric_coeffi')
        leng1=round(len(Time1)/2)
        leng2=round(len(Time2)/2)
        leng3=round(len(Time3)/2)
    
        TEMP_Fc1=TOTAL1[0][2]/np.sqrt((TOTAL1[1][2])*(TOTAL1[1][2])+(TOTAL1[2][2])*(TOTAL1[2][2]))
        TEMP_Fc2=TOTAL2[0][2]/np.sqrt((TOTAL2[1][2])*(TOTAL2[1][2])+(TOTAL2[2][2])*(TOTAL2[2][2]))
        TEMP_Fc3=TOTAL3[0][2]/np.sqrt((TOTAL3[1][2])*(TOTAL3[1][2])+(TOTAL3[2][2])*(TOTAL3[2][2]))
        TOTAL_TEMP=TEMP_Fc1[:leng1],TEMP_Fc2[:leng1],TEMP_Fc3[:leng1]
        
        plt.plot(Time1[:leng1]*pow(10,-9), np.mean(np.array(TOTAL_TEMP), axis=0)[:leng1],color=Color,linestyle='dashed') # mean value FX/ mean Value Fy
        plt.plot(Time1[:leng1]*pow(10,-9), np.max(np.array(TOTAL_TEMP), axis=0)[:leng1],label=NAME_LABEL,color=Color,linestyle='solid') # mean value FX/ mean Value Fy
        plt.plot(Time1[:leng1]*pow(10,-9), np.min(np.array(TOTAL_TEMP), axis=0)[:leng1],color=Color,linestyle='dotted') # mean value FX/ mean Value Fy
        plt.legend(fontsize="11",loc='upper right')
        #plt.fill_between(Time1[:leng1]*pow(10,-9), np.max(np.array(TOTAL_TEMP), axis=0)[:leng1], np.min(np.array(TOTAL_TEMP), axis=0)[:leng1],alpha=0.1, color=Color)
            







    
    elif save_name=='OFF_Y':
        plt.plot(Time3[:leng3]*pow(10,-9), np.sqrt((TOTAL3[1][2])*(TOTAL3[1][2])+(TOTAL3[2][2])*(TOTAL3[2][2]))[:leng3], label=NAME_LABEL[2], color=Color,linestyle='solid',lw=lw)
        #plt.fill_between(Time1[:leng1]*pow(10,-9), np.sqrt((TOTAL1[1][1])*(TOTAL1[1][1])+(TOTAL1[2][1])*(TOTAL1[2][1]))[:leng1], np.sqrt((TOTAL1[1][0])*(TOTAL1[1][0])+(TOTAL1[2][0])*(TOTAL1[2][0]))[:leng1], alpha=0.4, color='blue')
        plt.plot(Time2[:leng2]*pow(10,-9), np.sqrt((TOTAL2[1][2])*(TOTAL2[1][2])+(TOTAL2[2][2])*(TOTAL2[2][2]))[:leng2], label=NAME_LABEL[1], color=Color,linestyle='dashed',lw=lw)
        #plt.fill_between(Time3[:leng3]*pow(10,-9),  np.sqrt((TOTAL3[1][1])*(TOTAL3[1][1])+(TOTAL3[2][1])*(TOTAL3[2][1]))[:leng3], np.sqrt((TOTAL3[1][0])*(TOTAL3[1][0])+(TOTAL3[2][0])*(TOTAL3[2][0]))[:leng3], alpha=0.4, color='black')
        plt.plot(Time1[:leng1]*pow(10,-9), np.sqrt((TOTAL1[1][2])*(TOTAL1[1][2])+(TOTAL1[2][2])*(TOTAL1[2][2]))[:leng1], label=NAME_LABEL[0], color=Color,linestyle='dotted',lw=lw)
        #plt.fill_between(Time2[:leng2]*pow(10,-9),  np.sqrt((TOTAL2[1][1])*(TOTAL2[1][1])+(TOTAL2[2][1])*(TOTAL2[2][1]))[:leng2], np.sqrt((TOTAL2[1][0])*(TOTAL2[1][0])+(TOTAL2[2][0])*(TOTAL2[2][0]))[:leng2], alpha=0.4, color='red')
        plt.legend(fontsize="11",loc='upper right')
    else:
        plt.plot(Time3[:leng3]*pow(10,-9), np.sqrt((TOTAL3[1][2])*(TOTAL3[1][2])+(TOTAL3[2][2])*(TOTAL3[2][2]))[:leng3], label=NAME_LABEL[2], color=Color,linestyle='solid',lw=lw)
        #plt.fill_between(Time1[:leng1]*pow(10,-9), np.sqrt((TOTAL1[1][1])*(TOTAL1[1][1])+(TOTAL1[2][1])*(TOTAL1[2][1]))[:leng1], np.sqrt((TOTAL1[1][0])*(TOTAL1[1][0])+(TOTAL1[2][0])*(TOTAL1[2][0]))[:leng1], alpha=0.4, color='blue')
        plt.plot(Time2[:leng2]*pow(10,-9), np.sqrt((TOTAL2[1][2])*(TOTAL2[1][2])+(TOTAL2[2][2])*(TOTAL2[2][2]))[:leng2], label=NAME_LABEL[1], color=Color,linestyle='dashed',lw=lw)
        #plt.fill_between(Time3[:leng3]*pow(10,-9),  np.sqrt((TOTAL3[1][1])*(TOTAL3[1][1])+(TOTAL3[2][1])*(TOTAL3[2][1]))[:leng3], np.sqrt((TOTAL3[1][0])*(TOTAL3[1][0])+(TOTAL3[2][0])*(TOTAL3[2][0]))[:leng3], alpha=0.4, color='black')
        plt.plot(Time1[:leng1]*pow(10,-9), np.sqrt((TOTAL1[1][2])*(TOTAL1[1][2])+(TOTAL1[2][2])*(TOTAL1[2][2]))[:leng1], label=NAME_LABEL[0], color=Color,linestyle='dotted',lw=lw)
        #plt.fill_between(Time2[:leng2]*pow(10,-9),  np.sqrt((TOTAL2[1][1])*(TOTAL2[1][1])+(TOTAL2[2][1])*(TOTAL2[2][1]))[:leng2], np.sqrt((TOTAL2[1][0])*(TOTAL2[1][0])+(TOTAL2[2][0])*(TOTAL2[2][0]))[:leng2], alpha=0.4, color='red')
        plt.legend(fontsize="11",loc='lower right')
    
    moving=Slip_point3[0]*pow(10,-9)
    #
    #plt.vlines(x = moving,ymin = 20, ymax =0,color = 'black',linewidth = 1, linestyle ="--")
    #plt.vlines(x = 8,ymin = 20, ymax =0,color = 'black',linewidth = 1, linestyle ="--")
    #plt.xlabel('Time[s]',fontsize="11")
    #plt.xticks(ticks=[0,moving,5,8,10,15,20],labels=[0,'$T_m$','','$T_s$',10,'',20],fontsize="11")
    #plt.yticks(ticks=[0,5,10,15,20],fontsize="11")
    #plt.ylim((-0.3, 15))
    #plt.xlim((-0, 20))
    #plt.grid()
    #lt.ylabel('Normal',fontsize="11")
    #plt.legend(fontsize="11",loc='upper left')
    

   
    plt.legend(fontsize="11",loc='upper left')
    plt.subplot(3,1,3)
    plt.plot(Time3[:leng3]*pow(10,-9), ((TOTAL3[2][2])/(TOTAL3[1][2]))[:leng3], label=NAME_LABEL[2], color='black',linestyle='solid',lw=lw)
    #plt.fill_between(Time1[:leng1]*pow(10,-9), np.sqrt((TOTAL1[1][1])*(TOTAL1[1][1])+(TOTAL1[2][1])*(TOTAL1[2][1]))[:leng1], np.sqrt((TOTAL1[1][0])*(TOTAL1[1][0])+(TOTAL1[2][0])*(TOTAL1[2][0]))[:leng1], alpha=0.4, color='blue')
    plt.plot(Time2[:leng2]*pow(10,-9), ((TOTAL2[2][2])/(TOTAL2[1][2]))[:leng2], label=NAME_LABEL[1], color='orange',linestyle='dashed',lw=lw)
    #plt.fill_between(Time3[:leng3]*pow(10,-9),  np.sqrt((TOTAL3[1][1])*(TOTAL3[1][1])+(TOTAL3[2][1])*(TOTAL3[2][1]))[:leng3], np.sqrt((TOTAL3[1][0])*(TOTAL3[1][0])+(TOTAL3[2][0])*(TOTAL3[2][0]))[:leng3], alpha=0.4, color='black')
    plt.plot(Time1[:leng1]*pow(10,-9), ((TOTAL1[2][2])/(TOTAL1[1][2]))[:leng1], label=NAME_LABEL[0], color='blue',linestyle='dotted',lw=lw)
    #plt.fill_between(Time2[:leng2]*pow(10,-9),  np.sqrt((TOTAL2[1][1])*(TOTAL2[1][1])+(TOTAL2[2][1])*(TOTAL2[2][1]))[:leng2], np.sqrt((TOTAL2[1][0])*(TOTAL2[1][0])+(TOTAL2[2][0])*(TOTAL2[2][0]))[:leng2], alpha=0.4, color='red')
    moving=Slip_point3[0]*pow(10,-9)
    #plt.vlines(x = moving,ymin = 20, ymax =0,color = 'black',linewidth = 1, linestyle ="--")
    plt.xlabel('Time[s]',fontsize="11")

    #plt.ylim((-0.5, 20))
    
    
    plt.ylabel('Nomral force direction')
    
    #print(f'TIme 1 :{len(Time1[:leng3])} | TIme 2 :{len(Time2[:leng3])} | TIme 3 :{len(Time3[:leng3])}')
    '''
    
