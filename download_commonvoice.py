from datasets import load_dataset
from tqdm import tqdm
import os
import csv
import random


# LANGUAGES = ['ab', 'af', 'am', 'ar', 'as', 'ast', 'az', 'ba', 'bas', 'be', 'bg', 'bn', 'br', 'ca', 'ckb', 'cnh', 'cs', 'cv', 'cy', 'da', 'de', 'dv', 'dyu', 'el', 'en', 'eo', 'es', 'et', 'eu', 'fa', 'fi', 'fr', 'fy-NL', 'ga-IE', 'gl', 'gn', 'ha', 'he', 'hi', 'hsb', 'ht', 'hu', 'hy-AM', 'ia', 'id', 'ig', 'is', 'it', 'ja', 'ka', 'kab', 'kk', 'kmr', 'ko', 'ky', 'lg', 'lij', 'lo', 'lt', 'ltg', 'lv', 'mdf', 'mhr', 'mk', 'ml', 'mn', 'mr', 'mrj', 'mt', 'myv', 'nan-tw', 'ne-NP', 'nhi', 'nl', 'nn-NO', 'nso', 'oc', 'or', 'os', 'pa-IN', 'pl', 'ps', 'pt', 'quy', 'rm-sursilv', 'rm-vallader', 'ro', 'ru', 'rw', 'sah', 'sat', 'sc', 'sk', 'skr', 'sl', 'sq', 'sr', 'sv-SE', 'sw', 'ta', 'te', 'th', 'ti', 'tig', 'tk', 'tok', 'tr', 'tt', 'tw', 'ug', 'uk', 'ur', 'uz', 'vi', 'vot', 'yi', 'yo', 'yue', 'zgh', 'zh-CN', 'zh-HK', 'zh-TW', 'zu', 'zza']
LANGUAGES = ['ab', 'af', 'br']
cachedir = "/data/lmorove1/hwang258/data/commonvoice" # TODO: change this dir (cache dir to save downloaded files)
savepath = "/data/lmorove1/hwang258/data/commonvoice/metadata" # TODO: change this dir (dir to save processed metadata)

os.makedirs(cachedir, exist_ok=True)
os.makedirs(savepath, exist_ok=True)

for k in LANGUAGES:
    print(k)
    cv_17 = load_dataset("mozilla-foundation/common_voice_17_0", k, split="validated", cache_dir=cachedir, trust_remote_code=True, num_proc=16)
    
    age_meta = cv_17['age']
    path_meta = cv_17['path']
    # print(age_meta)
    young_indices = [[path_meta[i], x] for i, x in enumerate(age_meta) if x == 'teens']
    old_indices = [[path_meta[i], x] for i, x in enumerate(age_meta) if x == 'seventies' or x == 'eighties' or x == 'nineties']
    print(len(young_indices))
    print(len(old_indices))
    if len(young_indices) > 0:
        with open(os.path.join(savepath, k+'_young.csv'), mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(young_indices)
    if len(old_indices) > 0:
        with open(os.path.join(savepath, k+'_old.csv'), mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(old_indices)
    if len(young_indices) > 0 or len(old_indices) > 0:
        mid_indices = [[path_meta[i], x] for i, x in enumerate(age_meta) if x != 'teens' and x != 'seventies' and x != 'eighties' and x != 'nineties']
        print(len(mid_indices))
        with open(os.path.join(savepath, k+'_mid.csv'), mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(mid_indices)
            
    gender_meta = cv_17['gender']
    male_indices = [[path_meta[i], x] for i, x in enumerate(gender_meta) if x == 'male_masculine']
    print(len(male_indices))
    female_indices = [[path_meta[i], x] for i, x in enumerate(gender_meta) if x == 'female_feminine']
    print(len(female_indices))
    if len(male_indices) > 0:
        with open(os.path.join(savepath, k+'_male.csv'), mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(male_indices)
    if len(female_indices) > 0:
        with open(os.path.join(savepath, k+'_female.csv'), mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(female_indices)
        
    accent_meta = cv_17['accent']
    accent_indices = [[path_meta[i], x] for i, x in enumerate(accent_meta) if len(x) > 1]
    print(len(accent_indices))
    if len(accent_indices) > 0:
        with open(os.path.join(savepath, k+'_accent.csv'), mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(accent_indices)
    

