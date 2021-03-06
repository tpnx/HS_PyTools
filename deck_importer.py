# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import argparse
import os


class DeckImporter(object):
    pos_mouse_search = "966 990"
    pos_mouse_card = "418 468"
    pos_mouse_card_gold = "652 468"

    def __init__(self, filename):
        self.filename = filename

    def run(self):
        print("[+] Importing: %s" % self.filename)
        for item in self.get_file_contents():
            if not item or item.startswith('#'):
                continue
            print("    %s" % item)
            number_of_cards, card_name = item.split(' ', 1)
            self.search(card_name)
            self.choose(number_of_cards)

    def get_file_contents(self):
        with open(self.filename) as f:
            lines = f.readlines()
            lines = [l.strip() for l in lines]
        return lines

    def search(self, card_name):
        os.system("xdotool mousemove " + DeckImporter.pos_mouse_search)
        os.system("xdotool click 1")
        os.system("xdotool type --delay 25 \"" + card_name + "\"")
        os.system("xdotool key \"Return\"")

    def choose(self, number_of_cards):
        if number_of_cards == "2":
            os.system("xdotool mousemove " + DeckImporter.pos_mouse_card_gold)
            os.system("xdotool click --repeat " + number_of_cards + " 1")
        os.system("xdotool mousemove " + DeckImporter.pos_mouse_card)
        os.system("xdotool click --repeat " + number_of_cards + " 1")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str)
    args = parser.parse_args()

    deck_file_name = str(args.file)

    importer = DeckImporter(filename=deck_file_name)
    importer.run()


if __name__ == '__main__':
    main()
