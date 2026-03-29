import re


pattern=r"[a-z]+yclone"


text='''
 qagfsjlsfkalmklmklkmkalmmklasmlkmklamklmf;lgkrk;mfs;la;l;lsalm;llkg;skgla;l;ask;ka;lk
 cyclone dyclone akpokkapokpoakpokaprkkkrkokkfammmapookrpkpoaokpokrpokakkaoakpokrpokpok;fmapkpooakkmajpooapokrkerpokpookrkepakapoapjappooekeoak;laempokaepokaepookapookerook
[kkaperpooja'jjaiejrklmgajajijiaje;aojpokire[alpokpokerkljeaaeawaiohriojioieajiojaioerijiotjaiojioajojtijajehtiuteiojetenhiuerhoegkl;nhiuhyererojioermerio8uerwk;liou8oetnernioeruiot5mk;l09ouetwe;lri909etwmpoj9ou09ererlmkljpofi-wiklmeri;ojiojugtmegkljioju'''
matches=re.finditer(pattern,text)
for match in matches:
    print(match)
