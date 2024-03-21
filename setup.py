from cx_Freeze import setup, Executable

executables = [Executable("reiscarnota.py", base="Win32GUI", icon="logo_reiscar.ico")]

setup(
    name="ReisCarNotas",
    version="1.0",
    description="ReisCarNotas1.0",
    executables=executables,
    options={
        "build_exe": {
            "include_files": ["banner_reiscar.png", "logo_reiscar.ico", "orderserver.json"]
        }
    }
)
