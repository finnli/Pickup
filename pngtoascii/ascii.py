#!/usr/bin/env python
# encoding: utf-8
__author__ = 'liyunfei'
from PIL import Image
import argparse

ascii_char=list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
def get_char(r,g,b,alpha=256):
	if alpha==0:
		return " "
	lenght=len(ascii_char)
	gray=int(0.2126*r+0.7152*g+0.0722*b)
	unit=(256+1)/lenght
	return ascii_char[int(gray/unit)]
if __name__=='__main__':
	width=30
	height=30

	im=Image.open("ascii_dora.png")
	im=im.resize((30,30),Image.NEAREST)
	txt=''
	for i in range(width):
		for j in range(height):
			txt+=get_char(*im.getpixel((j,i)))
		txt+="\n"
	print(txt)
	with open('output.txt','w') as e:
		e.write(txt)
		e.close
