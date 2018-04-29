#!/usr/bin/env python
import os
import cv2
import sys

import time

import pickle 
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.style as sty
print(sys.argv)
inDir=sys.argv[1]
f=open(inDir,"r")
##read header 
linesRead=0
IDS=[]
Frames=[]
for line in f:
    parts=line.strip("\n").split(',')
    if(linesRead!=0):
        IDS.append(int(parts[1]))
        Frames.append(int(parts[3][:-4])-int(parts[2][:-4]))
    linesRead+=1
f.close()
Result={}
Result["A"]={}
Result["B"]={}
Result["A"]["Slow"]={}
Result["A"]["Slow"]["ID"]=[]
Result["A"]["Slow"]["Frames"]=[]
Result["A"]["Slow"]["Colour"]=(0,0,1,1)
Result["A"]["Fast"]={}
Result["A"]["Fast"]["ID"]=[]
Result["A"]["Fast"]["Frames"]=[]
Result["A"]["Fast"]["Colour"]=(1,0,0,1)
Result["A"]["Medium"]={}
Result["A"]["Medium"]["ID"]=[]
Result["A"]["Medium"]["Frames"]=[]
Result["A"]["Medium"]["Colour"]=(0,1,0,1)

Result["B"]["Slow"]={}
Result["B"]["Slow"]["ID"]=[]
Result["B"]["Slow"]["Frames"]=[]
Result["B"]["Slow"]["Colour"]=(0,0,1,1)
Result["B"]["Fast"]={}
Result["B"]["Fast"]["ID"]=[]
Result["B"]["Fast"]["Frames"]=[]
Result["B"]["Fast"]["Colour"]=(1,0,0,1)
Result["B"]["Medium"]={}
Result["B"]["Medium"]["ID"]=[]
Result["B"]["Medium"]["Frames"]=[]
Result["B"]["Medium"]["Colour"]=(0,1,0,1)




###filter by speed
medThresh=600
fastThresh=300

for i in range(0,len(IDS)):
    if(Frames[i]>medThresh):
        speed="Slow"
    elif(Frames[i]<fastThresh):
        speed="Fast"
    else:
        speed="Medium"
    Result["A"][speed]["ID"].append(IDS[i])
    Result["A"][speed]["Frames"].append(Frames[i])

inDir=sys.argv[2]
f=open(inDir,"r")
##read header 
linesRead=0
IDS=[]
Frames=[]
for line in f:
    print(line)
    parts=line.strip("\n").split(',')
    if(linesRead!=0):
        IDS.append(int(parts[1]))
        Frames.append(int(parts[3][:-4])-int(parts[2][:-4]))
    linesRead+=1
f.close()

medThresh=1200
fastThresh=700

for i in range(0,len(IDS)):
    if(Frames[i]>medThresh):
        speed="Slow"
    elif(Frames[i]<fastThresh):
        speed="Fast"
    else:
        speed="Medium"
    Result["B"][speed]["ID"].append(IDS[i])
    Result["B"][speed]["Frames"].append(Frames[i])

fig, (ax1,ax2) = plt.subplots(1,2)
ax1.set_xlabel("Loop ID")
ax2.set_xlabel("Loop ID")
ax1.set_ylabel("Total Frames for Completion")
fig.suptitle(("A Bar graph Illustrating the Number of Frames in Each Loop"+
"Grouped by Speed"),weight='bold')

dataset="A"
for bar in Result[dataset].keys():
    print(len(Result[dataset][bar]["ID"]),len(Result[dataset][bar]["Frames"]))
    print(Result[dataset][bar]["ID"],Result[dataset][bar]["Frames"])
    ax1.bar(Result[dataset][bar]["ID"],Result[dataset][bar]["Frames"],
            color=Result[dataset][bar]["Colour"],label=dataset+"_"+bar)
    # ax.bar(Result[dataset][bar]["ID"],Result[dataset][bar]["Frames"],
    #         color=Result[dataset][bar]["Colour"],label="A_"+bar)
ax1.legend()

dataset="B"
for bar in Result[dataset].keys():
    print(len(Result[dataset][bar]["ID"]),len(Result[dataset][bar]["Frames"]))
    print(Result[dataset][bar]["ID"],Result[dataset][bar]["Frames"])
    ax2.bar(Result[dataset][bar]["ID"],Result[dataset][bar]["Frames"],
            color=Result[dataset][bar]["Colour"],label=dataset+"_"+bar)
    # ax.bar(Result[dataset][bar]["ID"],Result[dataset][bar]["Frames"],
    #         color=Result[dataset][bar]["Colour"],label="A_"+bar)
ax2.legend()

# for dataset in Result.keys():
#     for bar in Result[dataset].keys():
#         print(len(Result[dataset][bar]["ID"]),len(Result[dataset][bar]["Frames"]))
#         print(Result[dataset][bar]["ID"],Result[dataset][bar]["Frames"])
#         ax.bar(Result[dataset][bar]["ID"],Result[dataset][bar]["Frames"],
#                 color=Result[dataset][bar]["Colour"],label=dataset+"_"+bar)
#         # ax.bar(Result[dataset][bar]["ID"],Result[dataset][bar]["Frames"],
#         #         color=Result[dataset][bar]["Colour"],label="A_"+bar)
#     ax.legend()

# for bar in Result["A"].keys():
#     print(len(Result["A"][bar]["ID"]),len(Result["A"][bar]["Frames"]))
#     print(Result["A"][bar]["ID"],Result["A"][bar]["Frames"])
#     ax1.bar(Result["A"][bar]["ID"],Result["A"][bar]["Frames"],
#             color=Result["A"][bar]["Colour"],label="A_"+bar)
#     ax1.bar(Result["A"][bar]["ID"],Result["A"][bar]["Frames"],
#             color=Result["A"][bar]["Colour"],label="A_"+bar)
# ax.legend()


# rects1 = ax.bar(index, means_men, bar_width,
#                 alpha=opacity, color='b',
#                 yerr=std_men, error_kw=error_config,
#                 label='Men')

# rects2 = ax.bar(index + bar_width, means_women, bar_width,
#                 alpha=opacity, color='r',
#                 yerr=std_women, error_kw=error_config,
#                 label='Women')

# ax.set_xlabel('Group')
# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
# ax.set_xticks(index + bar_width / 2)
# ax.set_xticklabels(('A', 'B', 'C', 'D', 'E'))
# ax.legend()

# fig.tight_layout()
# plt.show()

sty.use("seaborn")

plt.show()