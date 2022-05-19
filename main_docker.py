import webbrowser
import keyboard
import random
import json
import time
import os

os.chdir("~/app/")
data = json.load(open("dictionary.json"))
words = list(data.keys())


def counter():
    with open('counter_timer.txt') as ft:
        counter = int(ft.read())
        with open('counter_timer.txt', 'w') as fh:
            counter += 1
            fh.write(str(counter))
        if counter > 50:
            with open('dictionary.txt', 'w') as fs:
                for line in words:
                    fs.write(line)
                    fs.write("\n")
            with open('counter_timer.txt', 'w') as fh:
                fh.write("0")


def firefox_browser():
    with open('dictionary.txt') as f:
        contents = f.read()
        contents = contents.lower()
        contents = contents.split("\n")
        remove_list = []
        a = 0

        browser = webbrowser.Mozilla("/usr/bin/firefox")
        browser.open("https://bing.com")
        time.sleep(5)
        while a != 30:
            word = random.choice(contents)
            if word not in remove_list:
                remove_list.append(word)
            elif word in remove_list:
                word = random.choice(contents)
            browser.open("https://bing.com/search?q=%s" % word)
            a += 1
            time.sleep(random.randint(1, 2))
        remove_words(contents, remove_list)


def chrome_browser():
    with open('dictionary.txt') as f:
        contents = f.read()
        contents = contents.lower()
        contents = contents.split("\n")
        remove_list = []
        b = 0

        browser = webbrowser.Chrome("/usr/bin/chrome")
        browser.open("https://bing.com")
        time.sleep(5)
        while b != 20:
            word = random.choice(contents)
            if word not in remove_list:
                remove_list.append(word)
            elif word in remove_list:
                word = random.choice(contents)
            browser.open("https://bing.com/search?q=%s" % word)
            b += 1
            time.sleep(random.randint(2, 3))
        remove_words(contents, remove_list)


def edge_browser():
    with open('dictionary.txt') as f:
        contents = f.read()
        contents = contents.lower()
        contents = contents.split("\n")
        remove_list = []
        b = 0

        # os.system("start msedge.exe")
        time.sleep(30)
        while b != 12:
            word = random.choice(contents)
            if word not in remove_list:
                remove_list.append(word)
            elif word in remove_list:
                word = random.choice(contents)
            webbrowser.open_new_tab("https://bing.com/search?q=%s" % word)
            b += 1
            time.sleep(random.randint(1, 2))
            keyboard.press_and_release('ctrl+w')
        remove_words(contents, remove_list)
        keyboard.press_and_release('ctrl+w')


def remove_words(contents, remove_list):
    keep_list = list(set(contents) - set(remove_list))
    with open('dictionary.txt', 'w') as fa:
        for line in keep_list:
            fa.write(line)
            fa.write("\n")


def main():
    counter()
    edge_browser()
    firefox_browser()

    time.sleep(2)
    os.system("taskkill /im firefox.exe /f")

    chrome_browser()
    time.sleep(2)

    os.system("taskkill /im chrome.exe /f")
    webbrowser.open("https://account.microsoft.com/rewards/")
    os.system("taskkill /im cmd.exe /f")


main()
