### Before executing you should copy folder with already translated text from
### https://github.com/Workbench-Team/space-station-14/tree/master-ru/Resources/Locale/ru-RU
### Then you have to specify path to this folder in arumoon_dir
### You also have to specify path to same folder 
### from nyanotrasen in nyanotrasen_dir
###
### After execution script will create folder named "autotranslate"
### You should manualy replace folder "ru-RU" in "Resources/Locale/" 
### with "ru-RU" from "autotranslate"

arumoon_dir = './arumoon/ru-RU/'
nyanotrasen_dir = './nyano/ru-RU/'

import os
 
# writes file dirs for aromoon locale
arumoon_files = []
for root, dirs, files in os.walk(arumoon_dir):
    for filename in files:
        arumoon_files.append(os.path.join(root, filename))

# writes file dirs for nyano locale
nyanotrasen_files = []
for root, dirs, files in os.walk(nyanotrasen_dir):
    for filename in files:
        nyanotrasen_files.append(os.path.join(root, filename))


# parse fluent data into dict
def parser(f):
    data = {}
    txt = f.readlines()
    key = ''
    val = ''
    tmp_key = ''
    tmp_val = ''
    for line in txt:
        if ' =' in line and line[0] != ' ':
            if line.split('=')[1] == '':
                tmp_key = line.strip('=') 
                tmp_val = ''
                val = ''                     
            else:
                tmp = line.split('=', 1)
                tmp_key = tmp[0]
                tmp_val = tmp[1]
                val = ''
        else:
            tmp_val = line
        
        key = tmp_key.strip()
        val += tmp_val
        if len(key) > 0:
            data[key] = val
    return data


# writes data to memory from aromoon locale
data_arumoon = {}
for _ in arumoon_files:
    with open(_) as f:
        parsed_data = parser(f)
        for k, v in parsed_data.items():
            data_arumoon[k] = v

# writes data to memory from nyano locale
for _ in nyanotrasen_files:
    with open(_) as f:
        data_nyanotrasen = parser(f)
        
        addition = _.split('ru-RU')[1]
        
        # check if folder constructed from this script
        if addition.split('/')[1] == 'arumoon':
            addition = addition.split('arumoon', 1)[1]
        elif addition.split('/')[1] == 'nyanotrasen':
            addition = addition.split('nyanotrasen', 1)[1]
        
        # setting up working dirs
        base_dir = './autotranslate/ru-RU/'        
        file_name = addition.split('/')[-1]
        work_dir = addition[:len(file_name) * -1]
        aru = 'arumoon/'
        nya = 'nyanotrasen/' 

        # writes folder & files in "./autotranslate/ru-RU/"
        for k in data_nyanotrasen:
            if k in data_arumoon:
                data_nyanotrasen[k] = data_arumoon[k]
                if  not os.path.exists(base_dir + aru + work_dir):
                    os.makedirs(base_dir + aru + work_dir)
                with open(base_dir + aru + work_dir + file_name, 'a') as f0:
                    print(k, ' =', data_nyanotrasen[k], file=f0, end='', sep='')
            else:
                if not os.path.exists(base_dir + nya + work_dir):
                    os.makedirs(base_dir + nya + work_dir)
                with open(base_dir + nya + work_dir + file_name, 'a') as f0:
                    print(k, ' =', data_nyanotrasen[k], file=f0, end='', sep='')     

                    