import cx_Freeze

executables = [cx_Freeze.Executable('SQL_Main.py')]

cx_Freeze.setup(
    name='SQL by Himanshu Sharma',
    options={"build_exe": {"packages":["sqlite3"], "include_files":["favicon.ico"]}},

    description="SQL by Himanshu Sharma",
    executables = executables
    )
