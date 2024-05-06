import os
import random
import csv

LANGUAGES = ['ab', 'af', 'am', 'ar', 'as', 'ast', 'az', 'ba', 'bas', 'be', 'bg', 'bn', 'br', 'ca', 'ckb', 'cnh', 'cs', 'cv', 'cy', 'da', 'de', 'dv', 'dyu', 'el', 'en', 'eo', 'es', 'et', 'eu', 'fa', 'fi', 'fr', 'fy-NL', 'ga-IE', 'gl', 'gn', 'ha', 'he', 'hi', 'hsb', 'ht', 'hu', 'hy-AM', 'ia', 'id', 'ig', 'is', 'it', 'ja', 'ka', 'kab', 'kk', 'kmr', 'ko', 'ky', 'lg', 'lij', 'lo', 'lt', 'ltg', 'lv', 'mdf', 'mhr', 'mk', 'ml', 'mn', 'mr', 'mrj', 'mt', 'myv', 'nan-tw', 'ne-NP', 'nhi', 'nl', 'nn-NO', 'nso', 'oc', 'or', 'os', 'pa-IN', 'pl', 'ps', 'pt', 'quy', 'rm-sursilv', 'rm-vallader', 'ro', 'ru', 'rw', 'sah', 'sat', 'sc', 'sk', 'skr', 'sl', 'sq', 'sr', 'sv-SE', 'sw', 'ta', 'te', 'th', 'ti', 'tig', 'tk', 'tok', 'tr', 'tt', 'tw', 'ug', 'uk', 'ur', 'uz', 'vi', 'vot', 'yi', 'yo', 'yue', 'zgh', 'zh-CN', 'zh-HK', 'zh-TW', 'zu', 'zza']

metapath = "/data/lmorove1/hwang258/data/commonvoice/metadata" # TODO: change this dir (dir to save processed metadata)
all_data1_train = []
all_data1_test = []
all_data2_train = []
all_data2_test = []

for k in LANGUAGES:
    print(k)
    # check gender
    if os.path.exists(os.path.join(metapath, k+'_male.csv')) and os.path.exists(os.path.join(metapath, k+'_female.csv')):
        
        with open(os.path.join(metapath, k+'_male.csv'), mode='r', newline='') as file:
            reader = csv.reader(file)
            data1 = list(reader)
        
        with open(os.path.join(metapath, k+'_female.csv'), mode='r', newline='') as file:
            reader = csv.reader(file)
            data2 = list(reader)
        
        leng = min(len(data1), len(data2))
        leng_ = int(leng * 0.05)
        random.shuffle(data1)
        random.shuffle(data2)
        data1 = data1[:leng]
        data2 = data2[:leng]
        all_data1_test = [*all_data1_test, *data1[:leng_]]
        all_data1_train = [*all_data1_train, *data1[leng_:]]
        all_data1_test = [*all_data1_test, *data2[:leng_]]
        all_data1_train = [*all_data1_train, *data2[leng_:]]
    
    # check age
    data3, data4, data5 = [], [], []
    if os.path.exists(os.path.join(metapath, k+'_old.csv')):
        with open(os.path.join(metapath, k+'_old.csv'), mode='r', newline='') as file:
            reader = csv.reader(file)
            data3 = list(reader)
    
    if os.path.exists(os.path.join(metapath, k+'_young.csv')):
        with open(os.path.join(metapath, k+'_young.csv'), mode='r', newline='') as file:
            reader = csv.reader(file)
            data4 = list(reader)
            
    if os.path.exists(os.path.join(metapath, k+'_mid.csv')):
        with open(os.path.join(metapath, k+'_mid.csv'), mode='r', newline='') as file:
            reader = csv.reader(file)
            data5_ = list(reader)
        data5 = [x for x in data5_ if len(x[1]) > 1]
            
    leng = max(len(data3), len(data4))
    if leng > 0:
        leng_ = int(leng * 0.05)
        random.shuffle(data5)
        data5 = data5[:leng]
        all_data2_test = [*all_data2_test, *data5[:leng_]]
        all_data2_train = [*all_data2_train, *data5[leng_:]]
        if len(data3) > 0:
            leng = len(data3)
            leng_ = int(leng * 0.05)
            all_data2_test = [*all_data2_test, *data3[:leng_]]
            all_data2_train = [*all_data2_train, *data3[leng_:]]
        if len(data4) > 0:
            leng = len(data4)
            leng_ = int(leng * 0.05)
            all_data2_test = [*all_data2_test, *data4[:leng_]]
            all_data2_train = [*all_data2_train, *data4[leng_:]]
                
with open(os.path.join(metapath, 'age_train.csv'), mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(all_data2_train)
    
with open(os.path.join(metapath, 'age_test.csv'), mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(all_data2_test)

with open(os.path.join(metapath, 'gender_train.csv'), mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(all_data1_train)
    
with open(os.path.join(metapath, 'gender_test.csv'), mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(all_data1_test)
