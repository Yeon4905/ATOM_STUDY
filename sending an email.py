# -*- coding: utf-8 -*-
"""
Created on Thu May 13 22:28:12 2021

@author: HYU
"""

import smtplib as smtp
import pandas as pd

if __name__ == "__main__":
    try:
        a = pd.read_csv("Z:\\STL_LAB_NAS\DTG\GYEONGGI\BUS_15\date\\DTG_15_171201.csv")
        s = smtp.SMTP('smtp.gmail.com', 587)
        s.starttls()  
        from_user = r"oev3900@gmail.com"
        to_user = r"lisa9780@hanyang.ac.kr"
        password = "dmsdnjf05463900"  
        s.login(from_user, password)
        subject = "Finally"
        text = "Running is done"
        message = f"Subject: {subject}\n\n{text}"
        s.sendmail(from_user, to_user, message);
    except Exception as ex:
        s = smtp.SMTP('smtp.gmail.com', 587)
        s.starttls()  
        from_user = r"oev3900@gmail.com"
        to_user = r"lisa9780@hanyang.ac.kr"
        password = "dmsdnjf05463900"  
        s.login(from_user, password)
        subject = "Uh oh"
        text = "You've got an error message! it's because of\n" + str(ex)
        message = f"Subject: {subject}\n\n{text}"
        s.sendmail(from_user, to_user, message);