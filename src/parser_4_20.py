from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from datetime import timedelta, date, datetime
from tqdm import tqdm
from collections import Counter


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def parse_4_20(start="30062017",end="20012019"):
    start_date = datetime.strptime(start,"%d%m%Y").date()
    end_date = datetime.strptime(end,"%d%m%Y").date()

    except_stopdate = ""
    results = []
    results_dict = {}

    opts = Options()
    opts.set_headless()
    assert opts.headless  # без графического интерфейса.
    browser = Firefox(options=opts)

    for single_date in tqdm(daterange(start_date, end_date), desc="PARSE 4x20"):
        handling_data = single_date.strftime("%d.%m.%Y")
        url = "https://www.stoloto.ru/4x20/archive?from={0}&to={0}&firstDraw=1&lastDraw=7&mode=date".format(handling_data)
        try:
            browser.get(url)
            results_tmp_obj = browser.find_elements_by_class_name('container')
            results_dict[handling_data]=[]
        except Exception:
            print("Error"+handling_data)
            except_stopdate = handling_data
            break
        if(len(results_tmp_obj)) == 0:
            continue
        if(len(results_tmp_obj)) == 2:
            results.append(results_tmp_obj[0].text)
            results_dict[handling_data].append(results_tmp_obj[0].text)
            continue
        if(len(results_tmp_obj)) == 4:
            results.append(results_tmp_obj[0].text)
            results.append(results_tmp_obj[2].text)
            results_dict[handling_data].append(results_tmp_obj[0].text)
            results_dict[handling_data].append(results_tmp_obj[2].text)
            continue
    browser.close()
    print(results)
    f = open("parse_4_20_{0}.txt".format(except_stopdate),"w")
    for res in results:
        f.write(res+'\n')
    f.close()
    f = open("parse_4_20_withdata_{0}.txt".format(except_stopdate),"w")
    for data in results_dict.keys():
        f.write(data+":"+" | ".join(results_dict[data])+'\n')
    f.close()

def statistic_4_20(file):
    lottery_str = open(file,"r").read()
    ###
    lottery_lst_withoutspace = lottery_str.replace(" ", "").split("\n")
    stat_1 = {"":0,"01":0, "02":0, "03":0, "04":0,"05":0,"06":0,"07":0,"08":0,"09":0,"10":0,"11":0, "12":0, "13":0, "14":0,"15":0,"16":0,"17":0,"18":0,"19":0,"20":0}
    stat_2 = {"":0,"01":0, "02":0, "03":0, "04":0,"05":0,"06":0,"07":0,"08":0,"09":0,"10":0,"11":0, "12":0, "13":0, "14":0,"15":0,"16":0,"17":0,"18":0,"19":0,"20":0}
    stat_3 = {"":0,"01":0, "02":0, "03":0, "04":0,"05":0,"06":0,"07":0,"08":0,"09":0,"10":0,"11":0, "12":0, "13":0, "14":0,"15":0,"16":0,"17":0,"18":0,"19":0,"20":0}
    stat_4 = {"":0,"01":0, "02":0, "03":0, "04":0,"05":0,"06":0,"07":0,"08":0,"09":0,"10":0,"11":0, "12":0, "13":0, "14":0,"15":0,"16":0,"17":0,"18":0,"19":0,"20":0}
    stat_5 = {"":0,"01":0, "02":0, "03":0, "04":0,"05":0,"06":0,"07":0,"08":0,"09":0,"10":0,"11":0, "12":0, "13":0, "14":0,"15":0,"16":0,"17":0,"18":0,"19":0,"20":0}
    stat_6 = {"":0,"01":0, "02":0, "03":0, "04":0,"05":0,"06":0,"07":0,"08":0,"09":0,"10":0,"11":0, "12":0, "13":0, "14":0,"15":0,"16":0,"17":0,"18":0,"19":0,"20":0}
    stat_7 = {"":0,"01":0, "02":0, "03":0, "04":0,"05":0,"06":0,"07":0,"08":0,"09":0,"10":0,"11":0, "12":0, "13":0, "14":0,"15":0,"16":0,"17":0,"18":0,"19":0,"20":0}
    stat_8 = {"":0,"01":0, "02":0, "03":0, "04":0,"05":0,"06":0,"07":0,"08":0,"09":0,"10":0,"11":0, "12":0, "13":0, "14":0,"15":0,"16":0,"17":0,"18":0,"19":0,"20":0}
    stat_1234 = {}
    stat_5678 = {}
    count_symbols_pos = len(lottery_lst_withoutspace)
    count_symbols_all = count_symbols_pos*8

    for lottery in lottery_lst_withoutspace:
        stat_1[lottery[0:2]] += 1
        stat_2[lottery[2:4]] += 1
        stat_3[lottery[4:6]] += 1
        stat_4[lottery[6:8]] += 1
        stat_5[lottery[8:10]] += 1
        stat_6[lottery[10:12]] += 1
        stat_7[lottery[12:14]] += 1
        stat_8[lottery[14:16]] += 1
        if (stat_1234.get(lottery[0:8])==None):
            stat_1234[lottery[0:8]] = 1
        else:
            stat_1234[lottery[0:8]] += 1
        if (stat_5678.get(lottery[8:16])==None):
            stat_5678[lottery[8:16]] = 1
        else:
            stat_5678[lottery[8:16]] += 1

    stat_firstpart = dict(Counter(stat_1)+Counter(stat_2)+Counter(stat_3)+Counter(stat_4))
    stat_secondpart = dict(Counter(stat_5)+Counter(stat_6)+Counter(stat_7)+Counter(stat_8))
    stat_all = dict(Counter(stat_firstpart)+Counter(stat_secondpart))


    f_all = open("stat_all_symbols.txt","w")
    f_firstpart = open("stat_firstpart_symbols.txt", "w")
    f_secondpart = open("stat_secondpart_symbols.txt", "w")
    f_1 = open("stat_pos1_symbols.txt", "w")
    f_2 = open("stat_pos2_symbols.txt", "w")
    f_3 = open("stat_pos3_symbols.txt", "w")
    f_4 = open("stat_pos4_symbols.txt", "w")
    f_5 = open("stat_pos5_symbols.txt", "w")
    f_6 = open("stat_pos6_symbols.txt", "w")
    f_7 = open("stat_pos7_symbols.txt", "w")
    f_8 = open("stat_pos8_symbols.txt", "w")
    for symb in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]:
        f_all.write("{0}:{1}:{2}%\n".format(symb,str(stat_all[symb]), to_perc(stat_all[symb],count_symbols_all)))
        f_firstpart.write("{0}:{1}:{2}%\n".format(symb, str(stat_firstpart[symb]), to_perc(stat_firstpart[symb], count_symbols_pos*4)))
        f_secondpart.write("{0}:{1}:{2}%\n".format(symb, str(stat_secondpart[symb]), to_perc(stat_secondpart[symb], count_symbols_pos * 4)))
        f_1.write("{0}:{1}:{2}%\n".format(symb, str(stat_1[symb]), to_perc(stat_1[symb],count_symbols_pos)))
        f_2.write("{0}:{1}:{2}%\n".format(symb, str(stat_2[symb]), to_perc(stat_2[symb], count_symbols_pos)))
        f_3.write("{0}:{1}:{2}%\n".format(symb, str(stat_3[symb]), to_perc(stat_3[symb], count_symbols_pos)))
        f_4.write("{0}:{1}:{2}%\n".format(symb, str(stat_4[symb]), to_perc(stat_4[symb], count_symbols_pos)))
        f_5.write("{0}:{1}:{2}%\n".format(symb, str(stat_5[symb]), to_perc(stat_5[symb], count_symbols_pos)))
        f_6.write("{0}:{1}:{2}%\n".format(symb, str(stat_6[symb]), to_perc(stat_6[symb], count_symbols_pos)))
        f_7.write("{0}:{1}:{2}%\n".format(symb, str(stat_7[symb]), to_perc(stat_7[symb], count_symbols_pos)))
        f_8.write("{0}:{1}:{2}%\n".format(symb, str(stat_8[symb]), to_perc(stat_8[symb], count_symbols_pos)))

    f_all.close()
    f_firstpart.close()
    f_secondpart.close()
    f_1.close()
    f_2.close()
    f_3.close()
    f_4.close()
    f_5.close()
    f_6.close()
    f_7.close()
    f_8.close()

    f_1234 = open("stat_seq1234.txt", "w")
    for seq in stat_1234.keys():
        if stat_1234[seq]>1:
            f_1234.write("{0}:{1} BIGGER 1 !!!!!!!!!!!!!!\n".format(seq,stat_1234[seq]))
        else:
            f_1234.write("{0}:{1}\n".format(seq, stat_1234[seq]))

    f_5678 = open("stat_seq5678.txt", "w")
    for seq in stat_5678.keys():
        if stat_5678[seq]>1:
            f_5678.write("{0}:{1} BIGGER 1 !!!!!!!!!!!!!!\n".format(seq,stat_5678[seq]))
        else:
            f_5678.write("{0}:{1}\n".format(seq, stat_5678[seq]))

    f_1234.close()
    f_5678.close()

def statistic_4_20_deeper(file):
    '''
    lottery_str = open(file, "r").read()
    lottery_lst_withoutspace = lottery_str.replace(" ", "").split("\n")
    stat_1 = {"": 0, "01": 0, "02": 0, "03": 0, "04": 0, "05": 0, "06": 0, "07": 0, "08": 0, "09": 0, "10": 0, "11": 0,
              "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0, "18": 0, "19": 0, "20": 0}
    first_lotothrone = ""
    second_lotothrone = ""

    for lottery in lottery_lst_withoutspace:
        first_lotothrone += " {0} {1} {2} {3}".format(lottery[0:2], lottery[2:4], lottery[4:6], lottery[6:8])
        second_lotothrone += " {0} {1} {2} {3}".format(lottery[8:10], lottery[10:12], lottery[12:14], lottery[14:16])
    open("first_lotothrone.txt", "w").write(first_lotothrone)
    open("second_lotothrone.txt", "w").write(second_lotothrone)
    '''





def to_perc(count, all):
    return str(round((float(count)/float(all))*100, 2))
