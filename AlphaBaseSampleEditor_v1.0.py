import tkinter as tk
import os
from pydub import AudioSegment
from pydub.playback import play

version = 1.0

# Import sample folder
all_samples = {}

AB_stock_samples_keylist = []
for file in os.listdir('sample_files/AlphaBaseWaves/'):
    if file[-4::].lower() == '.raw':
        print('Loading a raw file')
        string = 'sample_files/AlphaBaseWaves/' + file
        AB_stock_samples_keylist.append(string)
        all_samples[string] = AudioSegment.from_file(
                                    f'sample_files/AlphaBaseWaves/{file}',
                                    'raw',
                                    frame_rate=48000,
                                    channels=1,
                                    sample_width=2
                                )[:2700]
    else:
        print('Found something else: not a raw file')
        print(file)
AB_stock_samples_keylist.sort()

JB_stock_samples_keylist = []
for file in os.listdir('sample_files/JazRawSamples/'):
    if file[-4::].lower() == '.raw':
        print('Loading a raw file')
        string = 'sample_files/JazRawSamples/' + file
        JB_stock_samples_keylist.append(string)
        all_samples[string] = AudioSegment.from_file(
                                    f'sample_files/JazRawSamples/{file}',
                                    'raw',
                                    frame_rate=24000,
                                    channels=1,
                                    sample_width=2
                                )[:2700]
    else:
        print('Found something else: not a raw file')
        print(file)
JB_stock_samples_keylist.sort()

WB_stock_samples_keylist = []
for file in os.listdir('sample_files/drw_xb/'):
    if file[-4::].lower() == '.wav':
        print('Loading a wav file')
        string = 'sample_files/drw_xb/' + file
        WB_stock_samples_keylist.append(string)
        all_samples[string] = AudioSegment.from_wav(
                                    f'sample_files/drw_xb/{file}'
                                )[:2700]
    else:
        print('Found something else: not a wav file')
        print(file)
WB_stock_samples_keylist.sort()

TB_stock_samples_keylist = []
for folder in os.listdir('sample_files/TokToksounds/'):
    if folder != '.DS_Store': #TODO: find better method
        for file in os.listdir(f'sample_files/TokToksounds/{folder}'):
            if file[-4::].lower() == '.wav':
                print('Loading a wav file')
                string = 'sample_files/TokToksounds/' + folder + '/' + file
                TB_stock_samples_keylist.append(string)
                all_samples[string] = AudioSegment.from_wav(
                                            f'sample_files/TokToksounds/{folder}/{file}'
                                        )[:2700]
            else:
                print('Found something else: not a wav file')
                print(file)
TB_stock_samples_keylist.sort()

print('\nDone loading stock samples!')


############################ GUI ############################

root = tk.Tk()
root.title(f'Alpha Base Sample Editor v{version}')

frame_LoadSamples = tk.Frame(root)

labelframe_StockSamples = tk.LabelFrame(frame_LoadSamples, text='Stock Samples')
labelframe_StockSamples.pack(side='top')

labelframe_AlphaBaseSamples = tk.LabelFrame(labelframe_StockSamples, text='Alpha Base Stock Samples')
labelframe_AlphaBaseSamples.pack(side='top')
AlphaBaseList = tk.Listbox(labelframe_AlphaBaseSamples, width=50, height=5)
AlphaBaseList.pack(side='left')

labelframe_JazBaseSamples = tk.LabelFrame(labelframe_StockSamples, text='888/999 JazBase03 Stock Samples')
labelframe_JazBaseSamples.pack(side='top')
JazBaseList = tk.Listbox(labelframe_JazBaseSamples, width=50, height=5)
JazBaseList.pack(side='left')

labelframe_WalkerBaseSamples = tk.LabelFrame(labelframe_StockSamples, text='888/999 Dr. Walker XBase Stock Samples')
labelframe_WalkerBaseSamples.pack(side='top')
WalkerBaseList = tk.Listbox(labelframe_WalkerBaseSamples, width=50, height=5)
WalkerBaseList.pack(side='left')

labelframe_ToktokBaseSamples = tk.LabelFrame(labelframe_StockSamples, text='888/999 TokTok XBase Stock Samples')
labelframe_ToktokBaseSamples.pack(side='top')
ToktokBaseList = tk.Listbox(labelframe_ToktokBaseSamples, width=50, height=5)
ToktokBaseList.pack(side='left')

labelframe_PersonalSamples = tk.LabelFrame(frame_LoadSamples, text='Personal Samples')
labelframe_PersonalSamples.pack(side='top')
PersonalSamplesList = tk.Listbox(labelframe_PersonalSamples, width=50, height=10)
PersonalSamplesList.pack(side='left')

labelframe_writelist = tk.LabelFrame(root, text='My Sample Set')
rightList = tk.Listbox(labelframe_writelist, width=50, height=40)
rightList.pack(side='left')

for item in AB_stock_samples_keylist:
    AlphaBaseList.insert(tk.END, item)

for item in JB_stock_samples_keylist:
    JazBaseList.insert(tk.END, item)
    
for item in WB_stock_samples_keylist:
    WalkerBaseList.insert(tk.END, item)
    
for item in TB_stock_samples_keylist:
    ToktokBaseList.insert(tk.END, item)

def moveTo(fromList, toList):
    indexList = fromList.curselection()
    if indexList:
        index = indexList[0]
        val = fromList.get(index)
        toList.insert(tk.END, val)

def clearFrom(List):
    indexList = List.curselection()
    index = indexList[0]
    List.delete(index)

def audioOnClick(event):
    indexList = event.widget.curselection()
    index = indexList[0]
    audio_file = event.widget.get(index)
    play(all_samples[audio_file])

AlphaBaseList.bind("<<ListboxSelect>>", lambda event: audioOnClick(event))
JazBaseList.bind("<<ListboxSelect>>", lambda event: audioOnClick(event))
WalkerBaseList.bind("<<ListboxSelect>>", lambda event: audioOnClick(event))
ToktokBaseList.bind("<<ListboxSelect>>", lambda event: audioOnClick(event))
rightList.bind("<<ListboxSelect>>", lambda event: audioOnClick(event))

buttonFrame1 = tk.LabelFrame(root)
buttonRight = tk.Button(buttonFrame1, text='>', command = lambda: [moveTo(AlphaBaseList, rightList),
                                                        moveTo(JazBaseList, rightList),
                                                        moveTo(WalkerBaseList, rightList),
                                                        moveTo(ToktokBaseList, rightList)])
buttonX = tk.Button(buttonFrame1, text='X', command = lambda: clearFrom(rightList))
buttonRight.pack(side='top')
buttonX.pack(side='top')

buttonFrame2 = tk.LabelFrame(root)
buttonUp = tk.Button(buttonFrame2, text='ʌ')
buttonDown = tk.Button(buttonFrame2, text='v')
buttonUp.pack(side='top')
buttonDown.pack(side='top')

frame_LoadSamples.pack(side='left', fill=tk.BOTH, expand=1)
buttonFrame1.pack(side='left')
labelframe_writelist.pack(side='left')
buttonFrame2.pack(side='left')

root.mainloop()