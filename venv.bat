@echo off

REM 1. Create virtual environment
if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
    call .venv\Scripts\activate
    pip install -r requirements.txt
REM    call .venv\Scripts\deactivate
)

REM 2. Activate virtual environment
call .venv\Scripts\activate

@REM REM 3. Deactivate virtual environment
@REM REM call .venv\Scripts\deactivate


@REM # 1. 执行虚拟环境设置脚本
@REM .\venv.bat