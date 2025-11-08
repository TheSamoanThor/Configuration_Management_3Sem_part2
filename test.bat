@echo off
chcp 65001 > nul
echo ===============================================
echo    Тестирование Dependency Visualizer
echo ===============================================

echo.
echo [1] - Проверка флага помощи
python main.py --help

echo.
echo [2] - Запуск без аргументов
python main.py

echo.
echo [3] - Проверка несуществующего файла конфигурации
python main.py not_existing_config.json

echo.
echo [4] - Нормальный запуск с Newtonsoft.Json
python main.py config.json

echo.
echo [5] - Тестирование с Microsoft.EntityFrameworkCore
python main.py config_ef.json

echo.
echo [6] - Тестирование с несуществующим пакетом
python main.py config_nonexistent.json

echo.
echo ===============================================
echo    Тестирование завершено
echo ===============================================
pause
