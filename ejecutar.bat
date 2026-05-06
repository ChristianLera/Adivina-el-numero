@echo off
title Adivina el Número - Modo Calor
echo ======================================
echo    🔥 ADIVINA EL NÚMERO - MODO CALOR 🔥
echo ======================================
echo.
echo Iniciando el juego...
echo.
python AdivinaElNumero.py
if errorlevel 1 (
    echo.
    echo ERROR: No se pudo ejecutar el juego.
    echo Asegurate de tener Python instalado.
    echo.
    pause
)
