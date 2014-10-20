from ctypes import cdll 
import sys

lib_name = ''

if sys.platform.startswith('win32'):
    lib_name = 'ShellLib.dll'
else:
    lib_name = 'ShellLib.so'

lib = cdll.LoadLibrary(lib_name)
lib.print_msg()

