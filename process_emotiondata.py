import os
import librosa
from tqdm import tqdm
import soundfile as sf
import csv
import random
import shutil

# datapath = '/data/lmorove1/hwang258/data/commonvoice/unified_multilingual_dataset_of_emotional_human_utterances/data/preprocessed'
# tags = ['ang', 'dis', 'sad', 'fea', 'hap', 'neu']
# savepath = '/data/lmorove1/hwang258/data/commonvoice/SpeechEmotionData/data'
# metapath = '/data/lmorove1/hwang258/data/commonvoice/SpeechEmotionData/metadata.csv'
# os.makedirs(savepath, exist_ok=True)
# count = 1
# metadata = []
# for root, dir, files in os.walk(datapath):
#     for f in tqdm(files):
#         if f.endswith('.wav'):
#             for tag in tags:
#                 if '+' + tag + '+' in f:
#                     y, _ = librosa.load(os.path.join(root, f), sr=16000, mono=True)
#                     if y.shape[0] > 16000:
#                         sf.write(os.path.join(savepath, str(count)+'.wav'), y, samplerate=16000)
#                         metadata.append([os.path.join(savepath, str(count)+'.wav'), tag])
#                         count += 1
                        
# with open(os.path.join(metapath), mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(metadata)

file_path = "/data/lmorove1/hwang258/data/commonvoice/SpeechEmotionData/metadata.csv"
datapath = "/data/lmorove1/hwang258/data/commonvoice/SpeechEmotionData"
savepath = "/data/lmorove1/hwang258/data/commonvoice/SpeechEmotionData_split"

with open(file_path, mode='r', newline='') as file:
    reader = csv.reader(file)
    data = list(reader)

for row in data:
    print(row)

random.shuffle(data)
testdata = data[:2000]
traindata = data[2000:]