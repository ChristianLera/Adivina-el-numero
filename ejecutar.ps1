# Adivina el Número - Modo Calor
# Script de inicio para PowerShell

Write-Host "======================================" -ForegroundColor Yellow
Write-Host "   🔥 ADIVINA EL NÚMERO - MODO CALOR 🔥" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Yellow
Write-Host ""
Write-Host "Iniciando el juego..." -ForegroundColor Green
Write-Host ""

try {
    python AdivinaElNumero.py
    if ($LASTEXITCODE -ne 0) {
        throw "Error al ejecutar el juego"
    }
}
catch {
    Write-Host ""
    Write-Host "ERROR: No se pudo ejecutar el juego." -ForegroundColor Red
    Write-Host "Asegurate de tener Python instalado." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Presiona cualquier tecla para salir..."
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
}
