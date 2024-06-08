from cx_Freeze import setup, Executable


include_files = [
    ('imgs/background_image.png', 'imgs/background_image.png'),
    ('imgs/icon.ico', 'imgs/icon.ico'),
    ('users/', 'users/'),  # Uključivanje celog users foldera
    ('auth.db', 'auth.db'),
    ('config.json', 'config.json'),
]


options = {
    'build_exe': {
        'include_files': include_files,
        'packages': ['tkinter', 'sqlite3', 'cryptography', 'json'],
    },
}

executable = Executable("finance_manager.py", icon="imgs/icon.ico", base='Win32GUI')

setup(
    name="FinanceManager",
    version="1.1",
    description="Finance Manager Application",
    options=options,
    executables=[executable]
)
