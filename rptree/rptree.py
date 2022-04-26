# rptree.py

"""This module provides RP Tree main module."""

import os
import pathlib

PIPE = "│"
ELBOW = "\--"
TEE = "+--"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "


class DirectoryTree:
    #self musi być (w sumie to dlaczego?), root_dir to aktualne pwd od którego zaczynamy szukania
    #Nazywa się to      CLASS INITIALIZER
    def __init__(self, root_dir):
        #Podłoga przed nazwą generatora oznacza, że nie będzie używawny poza tym plikiem (modułem) - jest niepubliczny.
        self._generator = _TreeGenerator(root_dir)

    def generate(self):
        tree = self._generator.build_tree()
        for entry in tree:
            print(entry)


            #tutaj lecimy z nową klasą, znowu nieubliczną
class _TreeGenerator:
#Class initializer
    def __init__(self, root_dir):
        #Zabieramy aktualną ścieżkę i zamieniamy ją na instancję klasy TreeGenerator.root_dir
        self._root_dir = pathlib.Path(root_dir)
        #czyste drzewo, jako tablica elementów:
        self._tree = []

    #funkcja budująca drzewo, 
    def build_tree(self):
        #Tutaj robimy nagłówek drzewa, top of the top
        self._tree_head()
        #tutaj definiujemy funkcję, która będzie dokładała kolejne gałązki i liście
        self._tree_body(self._root_dir)
        #wynikiem funkcji jest tablica z całym drzewem, którą trzeba będzie wypluć
        return self._tree


    def _tree_head(self):
        #os sep to po prostu separator, żeby ładnie wyglądało, że jest to directory
        self._tree.append(f"{self._root_dir}{os.sep}")
        #odstępnik w pionie
        self._tree.append(PIPE)
    #Funkcja generująca elementy składowe drzewka
    def _tree_body(self, directory, prefix=""):
        #Tutaj chyba sprawdza current directory, jak wygląda jego struktura
        entries = directory.iterdir() 
        #print(entries)
        #tutaj bierze jegostrukturę i sprawdza co jest plikie, a co nie, jeżeli nie jest plikiem to go omija
        entries = sorted(entries, key=lambda entry: entry.is_file())
        print(entries)
        #sprawdza ile znalazł tych plików by wydrukwoać odpowiednią strukturę drzewa
        entries_count = len(entries)
        #inicjalizacja pętli for 
        for index, entry in enumerate(entries):
            connector = ELBOW if index == entries_count - 1 else TEE
            #print("drukuje sobie zawartosc tego fora")
            #print(index)
            #print(entry)
            #print(entries)
            #jeżeli dany rekord jest dir to dodajemy go do tree
            if entry.is_dir():

                self._add_directory(entry, index, entries_count, prefix, connector)
            #jeżeli nie jest dir to jest file i też dodajemy
            else:
                self._add_file(entry, prefix, connector)
                
    def _add_directory(self, directory, index, entries_count, prefix, connector):

        self._tree.append(f"{prefix}{connector} {directory.name}{os.sep}")

        if index != entries_count - 1:

            prefix += PIPE_PREFIX

        else:

            prefix += SPACE_PREFIX

        self._tree_body(directory=directory, prefix=prefix,)

        self._tree.append(prefix.rstrip())


    def _add_file(self, file, prefix, connector):

        self._tree.append(f"{prefix}{connector} {file.name}")

DirectoryTree(os.getcwd())
tree=DirectoryTree("../hello")
tree.generate()