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
my_files = []
for root, dirs, files in os.walk(arumoon_dir):
    for filename in files:
        my_files.append(os.path.join(root, filename))

# writes data from aromoon locale
data_a = {}
for _ in my_files:
    with open(_) as f:
        txt = f.readlines()
        key = ''
        val = ''
        tmp_key = ''
        tmp_val = ''
        for i in txt:
            if ' =' in i and i[0] != ' ':
                if i.split('=')[1] == '':                      
                    tmp_key = i.strip('=')  
                    tmp_val = ''
                    val = ''                  
                else:                    
                    tmp = i.split('=', 1)
                    tmp_key = tmp[0]
                    tmp_val = tmp[1]
                    val = ''
            else:
                tmp_val = i

            key = tmp_key.strip()
            val += tmp_val
            if len(key) > 0:
                data_a[key] = val


# writes file dirs for nyano locale
my_files = []
for root, dirs, files in os.walk(nyanotrasen_dir):
    for filename in files:
        my_files.append(os.path.join(root, filename))

# writes data from nyano locale
for _ in my_files:
    with open(_) as f:
        data_n = {}
        txt = f.readlines()
        key = ''
        val = ''
        tmp_key = ''
        tmp_val = ''
        for i in txt:
            if ' =' in i:
                if i.split('=')[1] == '':
                    tmp_key = i.strip('=') 
                    tmp_val = ''
                    val = ''                     
                else:
                    tmp = i.split('=', 1)
                    tmp_key = tmp[0]
                    tmp_val = tmp[1]
                    val = ''
            else:
                tmp_val = i
            
            key = tmp_key.strip()
            val += tmp_val
            if len(key) > 0:
                data_n[key] = val
        

        # writes folder & files in "./autotranslate/ru-RU/"
        addition = _.split('ru-RU')[1]
        base_dir = './autotranslate/ru-RU/'        
        file_name = addition.split('/')[-1]
        work_dir = addition[:len(file_name) * -1]
        aru = 'arumoon/'
        nya = 'nyanotrasen/' 
        
        for k in data_n:
            if k in data_a:
                data_n[k] = data_a[k]
                if  not os.path.exists(base_dir + aru + work_dir):
                    os.makedirs(base_dir + aru + work_dir)
                with open(base_dir + aru + work_dir + file_name, 'a') as f0:
                    print(k, '=', data_n[k], file=f0, end='')
            else:
                if not os.path.exists(base_dir + nya + work_dir):
                    os.makedirs(base_dir + nya + work_dir)
                with open(base_dir + nya + work_dir + file_name, 'a') as f0:
                    print(k, '=', data_n[k], file=f0, end='')     


        
               


