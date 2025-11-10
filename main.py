# -*- coding: utf-8 -*-
import sys
from antlr4 import *
from MyLangLexer import MyLangLexer
from MyLangParser import MyLangParser
from MyLangRunner import MyLangRunner
from ExecutorVisitor import Executor

def main():
    input_stream = FileStream("input.txt", encoding='utf-8')
    lexer = MyLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyLangParser(stream)
    tree = parser.program()

    runner = MyLangRunner()
    runner.visit(tree)

if __name__ == "__main__":
    main()