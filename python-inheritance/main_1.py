#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('8-rectangle').Rectangle

print(issubclass(Rectangle, BaseGeometry))
