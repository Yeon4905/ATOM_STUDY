"""C-ITS 한 폴더 내 한 파일씩 평균속도 구하기
    구한 평균속도 한 파일로 묶어 저장하기"""

import os
import pandas as pd

to_dir = ("Z:\\STL_LAB_NAS\\C-ITS\\simrun_fzp\\")
# dir1 = ("1. 경부선_첨두시(7-9시)\\result\\")
dir2 = ("2. 경부선_비첨두시(12-14시)\\resultsbyvehnum\\")
dir3 = ("3. 경부선_1개차로 block\\resultsbyvehnum\\")
dir4 = ("4. 경부선_2개차로 block\\resultsbyvehnum\\")
dir5 = ("5. 중부내륙선_첨두시(16-18시)\\resultsbyvehnum\\")
dir6 = ("6. 중부내륙선_비첨두시(6-8시)\\resultsbyvehnum\\")
dir7 = ("7. 중부내륙선_1개차로 block\\resultsbyvehnum\\")
to_dir = [dir2, dir3, dir4, dir5, dir6,dir7]
# ,
for d in to_dir:
    df1 = []
    for i in range(1,131):
        with open(d + "\\resultsbyvehnum_"+str(i)) as d_i:
            lines = d_i.readlines()[1:]
            num_lines = len(lines)
            sum_mean_spd = 0

            for line in lines:
                mean_speed = float(line.strip().split(';')[5])
                sum_mean_spd += mean_speed
            tot_mean_spd = sum_mean_spd / num_lines
            data = {'num': [num_lines],
                   'mean_spd': [tot_mean_spd]}
            df = pd.DataFrame(data)
        df1.append(df)
    datacom = pd.concat(df1, axis = 0)
    datacom.to_csv(d + "\\resultsbyvehnum.csv",encoding='utf-8')
    #     df = pd.DataFrame(df)
    #     lines = df.readlines()[1:]
    #     num_lines = len(lines)
        #mean_speed = sum(lines[5])/num_lines
        #df1 = pd.DataFrame(num_lines, mean_speed)
        #pd.to_csv(df1)
