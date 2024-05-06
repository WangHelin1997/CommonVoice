import os
import csv
import random

with open('/data/lmorove1/hwang258/data/commonvoice/DreamVoiceDB/merged_speaker_ratings.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    data1 = list(reader)

meta1 = []
meta2 = []
for i in range(len(data1)):
    spk = data1[i][0]
    inf1 = data1[i][3]
    inf2 = data1[i][4]
    if len(inf1) > 0:
        meta1.append([spk, inf1])
    if len(inf2) > 0:
        meta2.append([spk, inf2])

meta1 = meta1[1:]
meta2 = meta2[1:]
print(len(meta1))
print(len(meta2))

random.shuffle(meta1)
random.shuffle(meta2)

with open('/data/lmorove1/hwang258/data/commonvoice/DreamVoiceDB/bright_speakers.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(meta1)

with open('/data/lmorove1/hwang258/data/commonvoice/DreamVoiceDB/smooth_speakers.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(meta2)

test_num = 25

test_meta1 = meta1[:test_num]
train_meta1 = meta1[test_num:]

test_meta2 = meta2[:test_num]
train_meta2 = meta2[test_num:]

librispeech_basepath = '/data/lmorove1/hwang258/librimix/LibriSpeech'
subdirs = ['dev-clean', 'dev-other', 'test-clean', 'test-other', 'train-clean-100', 'train-clean-360', 'train-other-500']
vctk_basepath = '/data/lmorove1/hwang258/data/commonvoice/VCTK-Corpus/wav48'

found_spks = []
test_meta1_files = []
for line in test_meta1:
    spk = line[0]
    label = line[1]
    for subdir in subdirs:
        if os.path.isdir(os.path.join(librispeech_basepath, subdir, spk)):
            # TO DO
            found_spks.append(spk)
            
            for root, dirs, files in os.walk(os.path.join(librispeech_basepath, subdir, spk)):
                for f in files:
                    if f.endswith('.flac') or f.endswith('.wav'):
                        test_meta1_files.append([os.path.join(root, f), label])
                
    if os.path.isdir(os.path.join(vctk_basepath, spk)):
        found_spks.append(spk)
        
        for root, dirs, files in os.walk(os.path.join(vctk_basepath, spk)):
            for f in files:
                if f.endswith('.flac') or f.endswith('.wav'):
                    test_meta1_files.append([os.path.join(root, f), label])

print(len(found_spks), len(test_meta1))
print(len(test_meta1_files))

found_spks = []
test_meta2_files = []
for line in test_meta2:
    spk = line[0]
    label = line[1]
    for subdir in subdirs:
        if os.path.isdir(os.path.join(librispeech_basepath, subdir, spk)):
            # TO DO
            found_spks.append(spk)
            for root, dirs, files in os.walk(os.path.join(librispeech_basepath, subdir, spk)):
                for f in files:
                    if f.endswith('.flac') or f.endswith('.wav'):
                        test_meta2_files.append([os.path.join(root, f), label])
                
    if os.path.isdir(os.path.join(vctk_basepath, spk)):
        found_spks.append(spk)
        
        for root, dirs, files in os.walk(os.path.join(vctk_basepath, spk)):
            for f in files:
                if f.endswith('.flac') or f.endswith('.wav'):
                    test_meta2_files.append([os.path.join(root, f), label])

print(len(found_spks), len(test_meta2))
print(len(test_meta2_files))

found_spks = []
train_meta1_files = []
for line in train_meta1:
    tag = True
    spk = line[0]
    label = line[1]
    for subdir in subdirs:
        if os.path.isdir(os.path.join(librispeech_basepath, subdir, spk)):
            # TO DO
            found_spks.append(spk)
            tag=False
            for root, dirs, files in os.walk(os.path.join(librispeech_basepath, subdir, spk)):
                for f in files:
                    if f.endswith('.flac') or f.endswith('.wav'):
                        train_meta1_files.append([os.path.join(root, f), label])
                        
    if os.path.isdir(os.path.join(vctk_basepath, spk)):
        found_spks.append(spk)
        tag=False
        for root, dirs, files in os.walk(os.path.join(vctk_basepath, spk)):
            for f in files:
                if f.endswith('.flac') or f.endswith('.wav'):
                    train_meta1_files.append([os.path.join(root, f), label])
    if tag: print(spk)

print(len(found_spks), len(train_meta1))
print(len(train_meta1_files))

found_spks = []
train_meta2_files = []
for line in train_meta2:
    tag = True
    spk = line[0]
    label = line[1]
    for subdir in subdirs:
        if os.path.isdir(os.path.join(librispeech_basepath, subdir, spk)):
            # TO DO
            found_spks.append(spk)
            
            for root, dirs, files in os.walk(os.path.join(librispeech_basepath, subdir, spk)):
                for f in files:
                    if f.endswith('.flac') or f.endswith('.wav'):
                        train_meta2_files.append([os.path.join(root, f), label])
            tag=False
    if os.path.isdir(os.path.join(vctk_basepath, spk)):
        found_spks.append(spk)
        tag=False
        for root, dirs, files in os.walk(os.path.join(vctk_basepath, spk)):
            for f in files:
                if f.endswith('.flac') or f.endswith('.wav'):
                    train_meta2_files.append([os.path.join(root, f), label])
    
    if tag: print(spk)

print(len(found_spks), len(train_meta2))
print(len(train_meta2_files))

with open('/data/lmorove1/hwang258/data/commonvoice/DreamVoiceDB/bright_train.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(train_meta1_files)
    
with open('/data/lmorove1/hwang258/data/commonvoice/DreamVoiceDB/bright_test.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(test_meta1_files)

with open('/data/lmorove1/hwang258/data/commonvoice/DreamVoiceDB/smooth_train.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(train_meta2_files)
    
with open('/data/lmorove1/hwang258/data/commonvoice/DreamVoiceDB/smooth_test.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(test_meta2_files)
