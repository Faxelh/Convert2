#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, sys, time, ffmpeg

try:
  import os, sys, time, re
except:
  print("\x1b[1;31m[\x1b[1;33m!\x1b[1;31m]\x1b[1;97m requests module not installed\n[!] installing module requirement")
  time.sleep(1.5)
  os.system('clear && python3 -m pip install ffmpeg; python3 '+sys.argv[0])
  sys.exit()
  
if "termux" in sys.prefix:
    try:
        os.system("termux-setup-storage")
    except:
        pass
    dir = "/sdcard/ConVideo"
else:
    dir = "ConVideo"
try:
    os.mkdir(dir)
except:
    pass

def _cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
raw_input = input
####################################################################################################
ts = .009
def Auto(a):
  for o in a + "\n":
    sys.stdout.write(o)
    sys.stdout.flush()
    time.sleep(ts)
   
def load(mot):
  home = ['/', '-', '|']
  for i in range(5):
    for x in range(len(home)):
      sys.stdout.write('\r{}{}'.format(str(mot), home[x]))
      time.sleep(.3);sys.stdout.flush()

def anime():
 f = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]",
      "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
      "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]",
      "[■■■■■■■■■■]"
      ]
 for e in range(len(f)):
  time.sleep(.5);sys.stdout.write("\r\t   " + f[e % len(f)]);sys.stdout.flush()
 print("\n")
 
def prec():
    f = "\x1b[2K"
    sys.stdout.write(f)

#raw_input("\t    \033[1;91m[\033[38;5;90m!\033[1;91m]\033[1;9;38;5;95m Hit Enter \033[1;0;1;91m[\033[38;5;9m!\033[1;91m]")

def bye():
  sys.exit()

def stop():
  _cls();Auto(Stop)
  Auto('\t\x1b[38;5;247m▒▒▒▒▒▒▒▒▒▒');print("\t\x1b[38;5;247m 0%")
  Auto('\t\x1b[38;5;197m█\x1b[38;5;247m▒▒▒▒▒▒▒▒▒');print("\t\x1b[38;5;199m 10%")
  Auto('\t\x1b[38;5;198m███\x1b[38;5;247m▒▒▒▒▒▒▒');print("\t\x1b[38;5;198m 30%")
  Auto('\t\x1b[38;5;108m█████\x1b[38;5;247m▒▒▒▒▒');print("\t\x1b[38;5;108m 50%")
  Auto('\t\x1b[38;5;107m███████\x1b[38;5;247m▒▒▒');print("\t\x1b[38;5;107m 80%")
  Auto('\t\x1b[38;5;112m██████████');print("\t\x1b[38;5;112m 100%");time.sleep(2.5)
  _cls();print(Dev_faxel)
  Auto("\x1b[1;97mBye Mec j'espere que tu as adorée ce script de\x1b[38;5;214m Mr ── \x1b[38;5;112;3;5;1mFaxel\x1b[3;0;0m")
  bye()
####################################################################################################
Dev_faxel =("""\033[1;97m╔═════════════════════════════════╗
\033[1;97m║\033[1;91m[\033[1;93m©\033[1;91m]\033[38;5;95m  Dev \033[1;97m:\033[38;5;214m Faxel ── \033[38;5;112m\033[3;5;1m@faxelh\033[3;0;0m   \033[1;91m[\033[1;93m©\033[1;91m]\033[1;97m║
\033[1;97m╚═════════════════════════════════╝ """)
Stop = ("""
   \t\x1b[38;5;247m╔══╗─────╔╗─\x1b[38;5;27m──────\x1b[38;5;29m────────╔═╗
   \t\x1b[38;5;247m║╔╗╠╦╦╦╦═╣╚╗\x1b[38;5;29m╔═╦═╦╗\x1b[38;5;27m╔═╦═╦╦╦╦╣═╣
   \t\x1b[38;5;198m║╠╣║╔╣╔╣╩╣╔╣\x1b[38;5;95m║╩╣║║║\x1b[38;5;28m║═╣╬║║║╔╬═║
   \t\x1b[38;5;198m╚╝╚╩╝╚╝╚═╩═╝\x1b[38;5;27m╚═╩╩═╝\x1b[38;5;18m╚═╩═╩═╩╝╚═╝""")
####################################################################################################
def MenuConvert():
    _cls()
    print("\033[1;97m╔" + 27 * "═" + 1 * "═╗")
    print("\033[1;97m║\033[48;5;240;38;5;199m  VIDEO \033[1;97m& \033[38;5;118mAUDIO \033[1;97mCONVERTER   \033[48;0;0;1;97m║")
    print("\033[1;97m║ \033[1;91m[\033[38;5;95m1.\033[1;91m]\033[38;5;195m Video .mkv to .mp4    \033[1;97m║")
    print("\033[1;97m║ \033[1;91m[\033[38;5;95m2.\033[1;91m]\033[38;5;120m Video .mov to .mp4    \033[1;97m║")
    print("\033[1;97m║ \033[1;91m[\033[38;5;95m3.\033[1;91m]\033[38;5;120m Video .mov to .webm   \033[1;97m║")
    print("\033[1;97m║ \033[1;91m[\033[38;5;95m4.\033[1;91m]\033[38;5;120m Video .mov to .ogg    \033[1;97m║")
    print("\033[1;97m║ \033[1;91m[\033[38;5;95m5.\033[1;91m]\033[38;5;120m Video .webm to .mp4   \033[1;97m║")
    print("\033[1;97m║ \033[1;91m[\033[38;5;95m6.\033[1;91m]\033[38;5;120m Video .wmv to .mp4    \033[1;97m║")
    print("\033[1;97m║ \033[1;91m[\033[38;5;95m7.\033[1;91m]\033[38;5;120m Image .png to .mp4    \033[1;97m║")
    print("\033[1;97m║ \033[1;91m[\033[38;5;95m8.\033[1;91m]\033[38;5;120m Video .mp4 to .wav    \033[1;97m║")
    print("\033[1;97m║ \033[1;91m[\033[38;5;95m9.\033[1;91m]\033[38;5;120m Video .mp4 to .m4a    \033[1;97m║")
    print("\033[1;97m║ \033[1;91m[\033[38;5;95mu.\033[1;91m]\033[38;5;228m Update script         \033[1;97m║")
    print("\033[1;97m║ \033[1;91m[\033[38;5;95mQ.\033[1;91m]\033[48;5;1;38;5;194m Quitter            \033[48;0;0m   \033[1;97m║")
    print("\033[1;97m╚" + 27 * "═" + 1 * "═╝")
    print("\033[1;97m║")
    choix_Convert()
def choix_Convert():
    dmd = raw_input("\033[1;97m╚═\033[1;31m▶\033[3;5;1m@\033[38;5;136mFaxel\033[3;0;0m \033[1;31m▶\033[1;33m ")
    if dmd == "":
        print("\n\t\033[1;91m[\033[1;93m!\033[1;91m]\033[1;95m Remplissez correctement ")
        MenuConvert()
    elif dmd == "1" or dmd == "01":
        MKVtoMP4()
    elif dmd == "2" or dmd == "02":
        MOVtoMP4()
    elif dmd == "3" or dmd == "03":
        MOVtoWEBM()
    elif dmd == "4" or dmd == "04":
        MOVtoOGG()
    elif dmd == "5" or dmd == "05":
        WEBMtoMP4()
    elif dmd == "6" or dmd == "06":
        WMVtoMP4()
    elif dmd == "7" or dmd == "07":
        PNGtoMP4()
    elif dmd == "8" or dmd == "08":
        MP4toWAV()
    elif dmd == "9" or dmd == "09":
        MP4toM4A()
    elif dmd == "u" or dmd == "U":
        Update()
    elif dmd == "q" or dmd == "Q":
        stop()
    else:
        print("\n\x1b[1;91m[\x1b[1;97m+\x1b[1;91m]\x1b[1;97m L'option \x1b[3;5;1;38;5;97m" + dmd + "\x1b[3;0;0;1;97m est indisponible. \x1b[1;91m[\x1b[1;97m+\x1b[1;91m]")
        raw_input("\t\033[1;91m[\033[38;5;90m-\033[1;91m]\033[1;9;38;5;95m Hit Enter \033[1;0;1;91m[\033[38;5;9m-\033[1;91m]")
        MenuConvert()
     
def MKVtoMP4():
    _cls(); print(Dev_faxel)
    print("\033[1;97m║")
    dmd = raw_input("\033[1;97m╚═\033[1;31m▶ \x1b[38;5;199mEntrer la Vidéo sans(.mkv)   \x1b[1;31m: \x1b[38;5;247m")
    print("\033[1;97m║")
    _dmd = raw_input("\033[1;97m╚═\033[1;31m▶ \x1b[38;5;195mNommé le resultat sans(.mp4) \x1b[1;31m: \x1b[38;5;247m")
    anime();prec()
    os.system(f"ffmpeg -i {dmd}.mkv -codec copy -strict -2 {_dmd}.mp4")
    os.system(f"mv -f {_dmd}.mp4 {dir}")
    print("\n \x1b[1;91m[\033[1;97m*\033[1;91m]\033[38;5;112m Vidéo convertie avec succès.")
    time.sleep(2)
    add = raw_input("\x1b[1;97m══════════════════════════════════════════════\n \033[1;91m[\033[38;5;90m©\033[1;91m] \x1b[1;97mVeux-tu convertir une autre Vidéo \x1b[1;91m(\x1b[38;5;112mo\x1b[1;91m/\x1b[38;5;111mn\x1b[1;91m) : \x1b[38;5;91m")
    if add == "o" or add == "O":
        MKVtoMP4()
    else:
        MenuConvert()

def MOVtoMP4():
    _cls();print(Dev_faxel)
    print("\033[1;97m║")
    dmd = raw_input("\033[1;97m╚═\033[1;31m▶ \x1b[38;5;199mEntrer la Vidéo sans(.mov)   \x1b[1;31m: \x1b[38;5;247m")
    print("\033[1;97m║")
    _dmd = raw_input("\033[1;97m╚═\033[1;31m▶ \x1b[38;5;195mNommé le resultat sans(.mp4) \x1b[1;31m: \x1b[38;5;247m")
    anime();prec()
    os.system(f"ffmpeg -i {dmd}.mov -vcodec h264 -acodec mp2 {_dmd}.mp4")
    os.system(f"mv -f {_dmd}.mp4 {dir}")
    print("\n \x1b[1;91m[\033[1;97m*\033[1;91m]\033[38;5;112m Vidéo convertie avec succès.")
    time.sleep(2)
    add = raw_input("\x1b[1;97m══════════════════════════════════════════════\n \033[1;91m[\033[38;5;90m©\033[1;91m] \x1b[1;97mVeux-tu convertir une autre Vidéo \x1b[1;91m(\x1b[38;5;112mo\x1b[1;91m/\x1b[38;5;111mn\x1b[1;91m) : \x1b[38;5;91m")
    if add == "o" or add == "O":
        MOVtoMP4()
    else:
        MenuConvert()


def MOVtoWEBM():
 _cls();print(Dev_faxel)
 print("\033[1;97m║")
 dmd = raw_input("\033[1;97m╚═\033[1;31m▶ \x1b[38;5;199mEntrer la Vidéo sans(.mov)   \x1b[1;31m: \x1b[38;5;247m")
 print("\033[1;97m║")
 _dmd = raw_input("\033[1;97m╚═\033[1;31m▶ \x1b[38;5;195mNommé le resultat sans(.webm) \x1b[1;31m: \x1b[38;5;247m")
 anime(); prec()
 os.system(f"ffmpeg -i {dmd}.mov -c:v libvpx -crf 10 -b:v 1M -c:a libvorbis {_dmd}.webm")
 os.system(f"mv -f {_dmd}.webm {dir}")
 print("\n \x1b[1;91m[\033[1;97m*\033[1;91m]\033[38;5;112m Vidéo convertie avec succès.")
 time.sleep(2)
 add = raw_input("\x1b[1;97m══════════════════════════════════════════════\n \033[1;91m[\033[38;5;90m©\033[1;91m] \x1b[1;97mVeux-tu convertir une autre Vidéo \x1b[1;91m(\x1b[38;5;112mo\x1b[1;91m/\x1b[38;5;111mn\x1b[1;91m) : \x1b[38;5;91m")
 if add == "o" or add == "O":
  MOVtoWEBM()
 else:
  MenuConvert()


def MOVtoOGG():
 _cls();print(Dev_faxel)
 print("\033[1;97m║")
 dmd = raw_input("\033[1;97m╚═\033[1;31m▶ \x1b[38;5;199mEntrer la Vidéo sans(.mov)   \x1b[1;31m: \x1b[38;5;247m")
 print("\033[1;97m║")
 _dmd = raw_input("\033[1;97m╚═\033[1;31m▶ \x1b[38;5;195mNommé le resultat sans(.ogg) \x1b[1;31m: \x1b[38;5;247m")
 anime(); prec()
 os.system(f"ffmpeg -i {dmd}.mov -codec:v libtheora -qscale:v 7 -codec:a libvorbis -qscale:a 5 {_dmd}.ogg")
 os.system(f"mv -f {_dmd}.ogg {dir}")
 print("\n \x1b[1;91m[\033[1;97m*\033[1;91m]\033[38;5;112m Vidéo convertie avec succès.")
 time.sleep(2)
 add = raw_input("\x1b[1;97m══════════════════════════════════════════════\n \033[1;91m[\033[38;5;90m©\033[1;91m] \x1b[1;97mVeux-tu convertir une autre Vidéo \x1b[1;91m(\x1b[38;5;112mo\x1b[1;91m/\x1b[38;5;111mn\x1b[1;91m) : \x1b[38;5;91m")
 if add == "o" or add == "O":
  MOVtoOGG()
 else:
  MenuConvert()


def WEBMtoMP4():
 _cls();print(Dev_faxel)
 print("\033[1;97m║")
 dmd = raw_input("\033[1;97m╚═\033[1;31m▶ \x1b[38;5;199mEntrer la Vidéo sans(.webm)   \x1b[1;31m: \x1b[38;5;247m")
 print("\033[1;97m║")
 _dmd = raw_input("\033[1;97m╚═\033[1;31m▶ \x1b[38;5;195mNommé le resultat sans(.mp4) \x1b[1;31m: \x1b[38;5;247m")
 anime(); prec()
 os.system(f"ffmpeg -i 01 - {dmd}.webm -crf 23 {_dmd}.mp4")
 os.system(f"mv -f {_dmd}.mp4 {dir}")
 print("\n \x1b[1;91m[\033[1;97m*\033[1;91m]\033[38;5;112m Vidéo convertie avec succès.")
 time.sleep(2)
 add = raw_input("\x1b[1;97m══════════════════════════════════════════════\n \033[1;91m[\033[38;5;90m©\033[1;91m] \x1b[1;97mVeux-tu convertir une autre Vidéo \x1b[1;91m(\x1b[38;5;112mo\x1b[1;91m/\x1b[38;5;111mn\x1b[1;91m) : \x1b[38;5;91m")
 if add == "o" or add == "O":
  WEBMtoMP4()
 else:
  MenuConvert()
  
def WMVtoMP4():
 _cls();print(Dev_faxel)
 print("\033[1;97m║")
 dmd = raw_input("\033[1;97m╚═\033[1;31m▶ \x1b[38;5;199mEntrer la Vidéo sans(.wmv)   \x1b[1;31m: \x1b[38;5;247m")
 print("\033[1;97m║")
 _dmd = raw_input("\033[1;97m╚═\033[1;31m▶ \x1b[38;5;195mNommé le resultat sans(.mp4) \x1b[1;31m: \x1b[38;5;247m")
 anime(); prec()
 os.system(f"ffmpeg -i {dmd}.mov -c:v libx264 -crf 23 {_dmd}.mp4")
 os.system(f"mv -f {_dmd}.mp4 {dir}")
 print("\n \x1b[1;91m[\033[1;97m*\033[1;91m]\033[38;5;112m Vidéo convertie avec succès.")
 time.sleep(2)
 add = raw_input("\x1b[1;97m══════════════════════════════════════════════\n \033[1;91m[\033[38;5;90m©\033[1;91m] \x1b[1;97mVeux-tu convertir une autre Vidéo \x1b[1;91m(\x1b[38;5;112mo\x1b[1;91m/\x1b[38;5;111mn\x1b[1;91m) : \x1b[38;5;91m")
 if add == "o" or add == "O":
  WMVtoMP4()
 else:
  MenuConvert()
  
def PNGtoMP4():
 _cls();print(Dev_faxel)
 print("\033[1;97m║")
 dmd = raw_input("\033[1;97m╚═\033[1;31m▶ \x1b[38;5;199mEntrer la Vidéo sans(.png)   \x1b[1;31m: \x1b[38;5;247m")
 print("\033[1;97m║")
 _dmd = raw_input("\033[1;97m╚═\033[1;31m▶ \x1b[38;5;195mNommé le resultat sans(.mp4) \x1b[1;31m: \x1b[38;5;247m")
 anime(); prec()
 os.system(f"ffmpeg -r 30 -s 1920x1080 -i {dmd}.png -vcodec libx264 -crf 25  -pix_fmt yuv420p {_dmd}.mp4")
 os.system(f"ffmpeg -framerate 5 -i {dmd}.png {_dmd}.mp4")
 os.system(f"mv -f {_dmd}.mp4 {dir}")
 print("\n \x1b[1;91m[\033[1;97m*\033[1;91m]\033[38;5;112m Vidéo convertie avec succès.")
 time.sleep(2)
 add = raw_input("\x1b[1;97m══════════════════════════════════════════════\n \033[1;91m[\033[38;5;90m©\033[1;91m] \x1b[1;97mVeux-tu convertir une autre Vidéo \x1b[1;91m(\x1b[38;5;112mo\x1b[1;91m/\x1b[38;5;111mn\x1b[1;91m) : \x1b[38;5;91m")
 if add == "o" or add == "O":
  PNGtoMP4()
 else:
  MenuConvert()


def MP4toWAV():
 _cls();print(Dev_faxel)
 print("\033[1;97m║")
 dmd = raw_input("\033[1;97m╚═\033[1;31m▶ \x1b[38;5;199mEntrer la Vidéo sans(.mp4)   \x1b[1;31m: \x1b[38;5;247m")
 print("\033[1;97m║")
 _dmd = raw_input("\033[1;97m╚═\033[1;31m▶ \x1b[38;5;195mNommé le resultat sans(.wav) \x1b[1;31m: \x1b[38;5;247m")
 anime(); prec()
 os.system(f"ffmpeg -i {dmd}.mp4 -i {_dmd}.wav -c:v copy -c:a aac ")
 os.system(f"mv -f {_dmd}.wav {dir}")
 print("\n \x1b[1;91m[\033[1;97m*\033[1;91m]\033[38;5;112m Vidéo convertie avec succès.")
 time.sleep(2)
 add = raw_input("\x1b[1;97m══════════════════════════════════════════════\n \033[1;91m[\033[38;5;90m©\033[1;91m] \x1b[1;97mVeux-tu convertir une autre Vidéo \x1b[1;91m(\x1b[38;5;112mo\x1b[1;91m/\x1b[38;5;111mn\x1b[1;91m) : \x1b[38;5;91m")
 if add == "o" or add == "O":
  MP4toWAV()
 else:
  MenuConvert()

def MP4toM4A():
 _cls();print(Dev_faxel)
 print("\033[1;97m║")
 dmd = raw_input("\033[1;97m╚═\033[1;31m▶ \x1b[38;5;199mEntrer la Vidéo sans(.mp4)   \x1b[1;31m: \x1b[38;5;247m")
 print("\033[1;97m║")
 _dmd = raw_input("\033[1;97m╚═\033[1;31m▶ \x1b[38;5;195mNommé le resultat sans(.m4a) \x1b[1;31m: \x1b[38;5;247m")
 anime(); prec()
 os.system(f"ffmpeg -i {dmd}.mp4 -f mp4 -vcodec copy -ac 2 -y {_dmd}.m4a")
 os.system(f"mv -f {_dmd}.m4a {dir}")
 print("\n \x1b[1;91m[\033[1;97m*\033[1;91m]\033[38;5;112m Vidéo convertie avec succès.")
 time.sleep(2)
 add = raw_input("\x1b[1;97m══════════════════════════════════════════════\n \033[1;91m[\033[38;5;90m©\033[1;91m] \x1b[1;97mVeux-tu convertir une autre Vidéo \x1b[1;91m(\x1b[38;5;112mo\x1b[1;91m/\x1b[38;5;111mn\x1b[1;91m) : \x1b[38;5;91m")
 if add == "o" or add == "O":
  MP4toM4A()
 else:
  MenuConvert()

#################################################################################################################
def Update():
  _cls();print(Dev_faxel)
  print("\033[1;97m║     \x1b[38;5;115m Veuillez saisir\x1b[38;5;112m O\x1b[38;5;115m ou\x1b[38;5;198m N\x1b[38;5;115m. \x1b[38;5;113mMerci      \033[1;97m║")
  dmd = raw_input("\033[1;97m╚\033[1;31m▶ \033[1;97mVeux-tu verifié s'il y a une mise a jour? \x1b[1;91m: \x1b[38;5;91m")
  if dmd == "n" or dmd == "N":
    MenuConvert()
  elif dmd == "o" or dmd == "O":
    _cls()
    load("\033[1;97m Veuillez patientez nous vérifions s'il y a une mise à jour\033[1;93m ")
    _cls();print(Dev_faxel)
    os.system('git pull origin master')
    raw_input("\t\t\033[1;91m[\033[38;5;90m!\033[1;91m]\033[1;9;38;5;95m Hit Enter \033[1;0;1;91m[\033[38;5;9m!\033[1;91m]")
    os.system("cd $HOME/Video && python3 setup.py ")
  else:
    print("\n\x1b[1;91m[\x1b[1;97m+\x1b[1;91m]\x1b[1;97m L'option \x1b[3;5;1;38;5;97m" + dmd + "\x1b[3;0;0;1;97m est indisponible. \x1b[1;91m[\x1b[1;97m+\x1b[1;91m]")
    time.sleep(3);Update()
####################################################################################################
if __name__ == "__main__":
    try:
        MenuConvert()
    except Exception as e:
        x = sys.exc_info()
        print("\033[1;97m" + 35 * "═")
        print(f"\x1b[1;91m[\x1b[1;97m+\x1b[1;91m]\x1b[1;97m Erreur \x1b[1;91m:\x1b[38;5;95m {x[0].__name__}\n\x1b[1;91m[\x1b[1;97m+\x1b[1;91m]\x1b[1;97m Texte \x1b[1;91m :\x1b[38;5;92m {e}\n\x1b[1;91m[\x1b[1;97m+\x1b[1;91m]\x1b[1;97m Ligne \x1b[1;91m :\x1b[38;5;95m {x[2].tb_lineno}")
        print("\x1b[38;5;199m Veuillez installé les modules requis puis relancé.")
        print("\033[1;97m" + 35 * "═")
        time.sleep(6)
        MenuConvert()