#!/data/bin/env python3

import re
import os
import sys
import time
import shutil
import requests
from getpass import getpass
from data import Main,login,banner,start


def menu():
    os.system("clear")
    banner.banner()
    banner.menu()
    print()

    zet = input("Masukkan Pilihan : ")
    if zet == '':
        menu()
    elif zet == '1':
# TOOL KE PERTAMA
        os.system("clear")
        print("""
    +------------------------------------------+
    |        Welcome To Script Dunia IT        |
    | Github   : https://github.com/duniait    |
    | Youtube  : Dunia IT                      |
    | Facebook : Dunia IT                      |
    +------------------------------------------+
            """)

        fr = run.parser.get("/me").find_all("a",string="Teman")
        for x in fr:
            if "friends/center" in x["href"]:
                continue
            else:
                users = run.friendlist(x["href"])
                print()
                start.sorting(users)
    elif zet == "2":
# TOOL KE KEDUA
        os.system("clear")
        print("""
    +------------------------------------------+
    |        Welcome To Script Dunia IT        |
    | Github   : https://github.com/duniait    |
    | Youtube  : Dunia IT                      |
    | Facebook : Dunia IT                      |
    +------------------------------------------+
            """)

        url = input("# url post: ")
        if "https://www.facebook.com" in url:
            url = url.replace("https://www.facebook.com",'')
        elif "https://m.facebook.com" in url:
            url = url.replace("https://m.facebook.com",'')
        elif "https://mbasic.facebook.com" in url:
            url = url.replace("https://mbasic.facebook.com",'')
        else:
            exit("# url invalid")
        like = run.parser.get(url)
        try:
            react = re.findall('href="(/ufi.*?)"',str(like))[0]
        except IndexError:
            exit("# invalid")
        users = run.likes(react)
        print()
        start.sorting(users)
    elif zet =="3":
# TOOL KE KETIGA
        os.system("clear")
        print("""
    +------------------------------------------+
    |        Welcome To Script Dunia IT        |
    | Github   : https://github.com/duniait    |
    | Youtube  : Dunia IT                      |
    | Facebook : Dunia IT                      |
    +------------------------------------------+
            """)

        username = run.bysearch("/search/people/?q=" + input("# query : "))
        print()
        start.sorting(username)
# TOOL KE EMPAT
    elif zet == '4':
        os.system("clear")
        print("""
    +------------------------------------------+
    |        Welcome To Script Dunia IT        |
    | Github   : https://github.com/duniait    |
    | Youtube  : Dunia IT                      |
    | Facebook : Dunia IT                      |
    +------------------------------------------+
            """)

        print("Tutorial Cara Ambil Id Grub")
        print("link youtube : ")
        grub = input("# Masukkan Id Grub : ")
        users = run.fromGrub("/browse/group/members/?id=" + grub)
        print()
        if len(users) == 0:
            exit("# Id Salah")
        start.sorting(users)
# TOOL KE LIMA
    elif zet == '5': 
        os.system("clear")
        print("""
    +------------------------------------------+
    |        Welcome To Script Dunia IT        |
    | Github   : https://github.com/duniait    |
    | Youtube  : Dunia IT                      |
    | Facebook : Dunia IT                      |
    +------------------------------------------+
            """)
        print("Tutorial Cara Mendapatkan Id Target")
        print("link youtube : ")
        zet = input("# Masukkan Id target : ")
        if zet.isdigit():
            user = "/profile.php?id=" + zet
        else:
            user = "/" + zet
        try:
            user = run.parser.get(user).find('a',string="Teman")["href"]
            username = run.friendlist(user)
            start.sorting(username)
        except TypeError:
            exit("# User Tidak Ditemukan ")
# TOOL KE 6
    elif zet == '6': 
        os.system("clear")
        print("""
    +------------------------------------------+
    |        Welcome To Script Dunia IT        |
    | Github   : https://github.com/duniait    |
    | Youtube  : Dunia IT                      |
    | Facebook : Dunia IT                      |
    +------------------------------------------+
            """)
        print("BELUM TERSEDIA TOOL 6")
        exit("# belum jadi ")
# TOOL KE 7
    elif zet == '7': 
        os.system("clear")
        print("""
    +------------------------------------------+
    |        Welcome To Script Dunia IT        |
    | Github   : https://github.com/duniait    |
    | Youtube  : Dunia IT                      |
    | Facebook : Dunia IT                      |
    +------------------------------------------+
            """)
        print("BELUM TERSEDIA TOOL 7")
        exit("# belum jadi ")
# TOOL KE 8
    elif zet == '8': 
        os.system("clear")
        print("""
    +------------------------------------------+
    |        Welcome To Script Dunia IT        |
    | Github   : https://github.com/duniait    |
    | Youtube  : Dunia IT                      |
    | Facebook : Dunia IT                      |
    +------------------------------------------+
            """)
        print("BELUM TERSEDIA TOOL 8")
        exit("# belum jadi ")
# TOOL KE 9
    elif zet == '9': 
        os.system("clear")
        print("""
    +------------------------------------------+
    |        Welcome To Script Dunia IT        |
    | Github   : https://github.com/duniait    |
    | Youtube  : Dunia IT                      |
    | Facebook : Dunia IT                      |
    +------------------------------------------+
            """)
        print("BELUM TERSEDIA TOOL 9")
        exit("# belum jadi ")
# TOOL KE 10
    elif zet == '10': 
        os.system("clear")
        print("""
    +------------------------------------------+
    |        Welcome To Script Dunia IT        |
    | Github   : https://github.com/duniait    |
    | Youtube  : Dunia IT                      |
    | Facebook : Dunia IT                      |
    +------------------------------------------+
            """)
        print("BELUM TERSEDIA TOOL 10")
    else:
        exit(" => Masukkan Pilihan Yang Benar ")
def cek():
    os.system('clear')
    banner.banner()
    print(" => Untuk Menggunakan Tools Ini Silakan Masukkan Cookie")
    print(" => Tutorial Cara Ambil Cookie Silakan Cek Disini")
    print(" => link youtube : ")
    print()
    cookie = input(" => Masukkan Cookie : ")
    if login.val(host, cookie):
        with open("data/cookies","w") as f:
            f.write(cookie)
        return cookie
    else:
        getpass("# Cookie Tidak Valid | Silakan Tonton Video Tutorial ")
        cek()
def main():
    try:
        cookies = open("data/cookies").read()
        if login.val(host, cookies):
            return cookies
        else:
            os.remove("data/cookies")
            exit("# session die")
    except FileNotFoundError:
        return cek()
if "__main__" == __name__:
    try:
        os.system('clear')
        banner.banner()
        try:
            shutil.rmtree("data/__pycache__")
            shutil.rmtree("./__pycache__")
        except FileNotFoundError:
            pass
        if len(sys.argv) == 2:
            if sys.argv[1] == 'free':
                host = "https://free.facebook.com{}"
            else:
                print("# Usage")
                exit("# Use <python3 mbf.py free> for free data")
        else:
            os.system("git pull")
            host = "https://mbasic.facebook.com{}"
        kuki = main()
        run = Main(kuki)
        menu()
    except requests.exceptions.ConnectionError:
        exit("# bad connection")
    except (KeyboardInterrupt,EOFError):
        exit("# Exit")

