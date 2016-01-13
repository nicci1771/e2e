#!/usr/bin/env python

import matplotlib.pyplot as plt
import os, sys, cv2

if __name__ == '__main__':

    a6l=['218','48']
    accord=['269','460','480','4','526','633','687','704','1936','1961','2566']
    buick=['1179','385','612','677','679','681','683','814','818','887','935']
    byd=['1006','1087','1139','1162','1167','1171','1188','1203','1205','319','341','421','470','486','491','57','665','817','819','81','821','897','899','925']
    corolla=['10','140','152','157','167','199','203','266','274','275','278','281','289','290','291','2','312','342','367','388','392','56','79','92','93','98']
    cruze=['1016','1223','1247','1250','1391','1392','1393','1409','1413','1415','1417','1434','1440','1441','1529','1536','1537','1554','1566','1567','1585','1586','1587','1601','1606','1607','1608','1609','1625','1708','1709','1736','1737','1738','1739','178','1893','1915','1922','1980','1984','199','2009','2010','2025','202','2039','2042','205','207','258','285','286','301','32','418','419','426','477','730','748','755','756','773','775','780','781','797','798','802','803','819','832','833','834','835','836','837','840','880','885']
    faw=['144','799','852']
    satana=['1859','1936','2312','547', '574','577','578','582','583','599','600','605','608']

    output = open('add_train.txt','w')
    for num in a6l:
       output.write('a6l'+num+'\n') 
    for num in accord:
       output.write('accord'+num+'\n') 
    for num in buick:
       output.write('buick'+num+'\n') 
    for num in byd:
       output.write('byd'+num+'\n') 
    for num in corolla:
       output.write('corolla'+num+'\n') 
    for num in cruze:
       output.write('cruze'+num+'\n') 
    for num in faw:
       output.write('faw'+num+'\n') 
    for num in satana:
       output.write('satana'+num+'\n') 
            
    import IPython
    IPython.embed()
