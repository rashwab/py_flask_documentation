import importlib, traceback, os

def main():
    try:
        mod = importlib.import_module('PyQt6')
        print('PyQt6 package file:', mod.__file__)
        p = os.path.dirname(mod.__file__)
        print('PyQt6 package dir listing:')
        print(os.listdir(p))
        qt6_dir = os.path.join(p, 'Qt6')
        print('Qt6 exists:', os.path.exists(qt6_dir))
        if os.path.exists(qt6_dir):
            print('Qt6/bin exists:', os.path.exists(os.path.join(qt6_dir, 'bin')))
    except Exception:
        print('Error locating PyQt6 package:')
        traceback.print_exc()

    checks = ['PyQt6.QtCore', 'PyQt6.QtGui', 'PyQt6.QtWidgets']
    for name in checks:
        print('\nChecking', name)
        try:
            m = importlib.import_module(name)
            print(name, 'imported successfully')
        except Exception as e:
            print(name, 'import error:', repr(e))
            traceback.print_exc()

    try:
        import ctypes
        mod = importlib.import_module('PyQt6')
        p = os.path.dirname(mod.__file__)
        dll = os.path.join(p, 'Qt6', 'bin')
        print('\nAttempting to list DLLs in', dll)
        if os.path.isdir(dll):
            print(os.listdir(dll)[:20])
        else:
            print('DLL dir not found')
    except Exception:
        traceback.print_exc()

if __name__ == '__main__':
    main()
