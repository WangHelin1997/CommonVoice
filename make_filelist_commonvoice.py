import os
import random
import csv

LANGUAGES = ['ab', 'af', 'am', 'ar', 'as', 'ast', 'az', 'ba', 'bas', 'be', 'bg', 'bn', 'br', 'ca', 'ckb', 'cnh', 'cs', 'cv', 'cy', 'da', 'de', 'dv', 'dyu', 'el', 'en', 'eo', 'es', 'et', 'eu', 'fa', 'fi', 'fr', 'fy-NL', 'ga-IE', 'gl', 'gn', 'ha', 'he', 'hi', 'hsb', 'ht', 'hu', 'hy-AM', 'ia', 'id', 'ig', 'is', 'it', 'ja', 'ka', 'kab', 'kk', 'kmr', 'ko', 'ky', 'lg', 'lij', 'lo', 'lt', 'ltg', 'lv', 'mdf', 'mhr', 'mk', 'ml', 'mn', 'mr', 'mrj', 'mt', 'myv', 'nan-tw', 'ne-NP', 'nhi', 'nl', 'nn-NO', 'nso', 'oc', 'or', 'os', 'pa-IN', 'pl', 'ps', 'pt', 'quy', 'rm-sursilv', 'rm-vallader', 'ro', 'ru', 'rw', 'sah', 'sat', 'sc', 'sk', 'skr', 'sl', 'sq', 'sr', 'sv-SE', 'sw', 'ta', 'te', 'th', 'ti', 'tig', 'tk', 'tok', 'tr', 'tt', 'tw', 'ug', 'uk', 'ur', 'uz', 'vi', 'vot', 'yi', 'yo', 'yue', 'zgh', 'zh-CN', 'zh-HK', 'zh-TW', 'zu', 'zza']

metapath = "/data/lmorove1/hwang258/data/commonvoice/metadata" # TODO: change this dir (dir to save processed metadata)
all_data = {}

for k in LANGUAGES:
    print(k)
    # check gender
    if os.path.exists(os.path.join(metapath, k+'_male.csv')):
        with open(os.path.join(metapath, k+'_male.csv'), mode='r', newline='') as file:
            reader = csv.reader(file)
            data1 = list(reader)
            for data in data1:
                name = data[0]
                tag = data[1]
                if name in all_data.keys():
                    all_data[name][0] = tag
                else:
                    all_data[name] = ['','','']
                    all_data[name][0] = tag
            
    if os.path.exists(os.path.join(metapath, k+'_female.csv')):
        with open(os.path.join(metapath, k+'_female.csv'), mode='r', newline='') as file:
            reader = csv.reader(file)
            data2 = list(reader)
            for data in data2:
                name = data[0]
                tag = data[1]
                if name in all_data.keys():
                    all_data[name][0] = tag
                else:
                    all_data[name] = ['','','']
                    all_data[name][0] = tag
        
    # check age
    if os.path.exists(os.path.join(metapath, k+'_old.csv')):
        with open(os.path.join(metapath, k+'_old.csv'), mode='r', newline='') as file:
            reader = csv.reader(file)
            data3 = list(reader)
            for data in data3:
                name = data[0]
                tag = data[1]
                if name in all_data.keys():
                    all_data[name][1] = tag
                else:
                    all_data[name] = ['','','']
                    all_data[name][1] = tag
    
    if os.path.exists(os.path.join(metapath, k+'_young.csv')):
        with open(os.path.join(metapath, k+'_young.csv'), mode='r', newline='') as file:
            reader = csv.reader(file)
            data4 = list(reader)
            for data in data4:
                name = data[0]
                tag = data[1]
                if name in all_data.keys():
                    all_data[name][1] = tag
                else:
                    all_data[name] = ['','','']
                    all_data[name][1] = tag
            
    if os.path.exists(os.path.join(metapath, k+'_mid.csv')):
        with open(os.path.join(metapath, k+'_mid.csv'), mode='r', newline='') as file:
            reader = csv.reader(file)
            data5 = list(reader)
            for data in data5:
                name = data[0]
                tag = data[1]
                if len(tag) > 0:
                    if name in all_data.keys():
                        all_data[name][1] = tag
                    else:
                        all_data[name] = ['','','']
                        all_data[name][1] = tag
            
    if os.path.exists(os.path.join(metapath, k+'_accent.csv')):
        with open(os.path.join(metapath, k+'_accent.csv'), mode='r', newline='') as file:
            reader = csv.reader(file)
            data6 = list(reader)
            for data in data6:
                name = data[0]
                tag = data[1]
                if name in all_data.keys():
                    all_data[name][2] = tag
                else:
                    all_data[name] = ['','','']
                    all_data[name][2] = tag

out = []
for k in all_data.keys():
    x = [*[k], *all_data[k]]
    out.append(x)

with open(os.path.join(metapath, 'alldata_TODO.csv'), mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(out)
