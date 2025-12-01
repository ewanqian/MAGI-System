<#
.SYNOPSIS
一键启动MAGI系统脚本

.DESCRIPTION
此脚本用于启动MAGI系统，包括创建虚拟环境、安装依赖、启动后端服务和打开前端页面。

.AUTHOR
钱玉文 (Ewan Qin)
#>

# 设置颜色
$ErrorActionPreference = "Stop"
$Host.UI.RawUI.BackgroundColor = "Black"
$Host.UI.RawUI.ForegroundColor = "Cyan"
Clear-Host

# 脚本目录
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RootDir = Join-Path $ScriptDir ".."
$BackendDir = Join-Path $RootDir "backend"
$FrontendDir = Join-Path $RootDir "frontend"
$VenvDir = Join-Path $BackendDir ".venv"

Write-Host "========================================"
Write-Host "          MAGI SYSTEM LAUNCHER          "
Write-Host "========================================"
Write-Host ""

# 检查Python是否安装
Write-Host "[1/5] 检查Python环境..."
Try {
    $PythonVersion = python --version 2>&1
    Write-Host "✓ Python已安装: $PythonVersion"
} Catch {
    Write-Host "✗ 未找到Python，请先安装Python 3.8+"
    Pause
    Exit 1
}

# 创建虚拟环境
Write-Host "[2/5] 检查虚拟环境..."
If (-Not (Test-Path $VenvDir)) {
    Write-Host "创建虚拟环境..."
    python -m venv $VenvDir
    Write-Host "✓ 虚拟环境创建成功"
} Else {
    Write-Host "✓ 虚拟环境已存在"
}

# 激活虚拟环境并安装依赖
Write-Host "[3/5] 安装依赖..."
$ActivateScript = Join-Path $VenvDir "Scripts\Activate.ps1"
& $ActivateScript

# 升级pip
python -m pip install --upgrade pip > $null 2>&1

# 安装后端依赖
If (Test-Path (Join-Path $BackendDir "requirements.txt")) {
    pip install -r (Join-Path $BackendDir "requirements.txt") > $null 2>&1
    Write-Host "✓ 后端依赖安装完成"
} Else {
    Write-Host "✗ 未找到requirements.txt文件"
    Pause
    Exit 1
}

# 检查Ollama是否安装
Write-Host "[4/5] 检查Ollama..."
Try {
    $OllamaVersion = ollama --version 2>&1
    Write-Host "✓ Ollama已安装: $OllamaVersion"
} Catch {
    Write-Host "⚠ 未找到Ollama，请先安装Ollama并拉取模型"
    Write-Host "   安装地址: https://ollama.com/"
    Write-Host "   拉取模型命令: ollama pull llama3"
    Pause
}

# 启动后端服务
Write-Host "[5/5] 启动MAGI系统..."
Write-Host "启动后端服务..."

# 在新窗口启动后端服务
Start-Process powershell -ArgumentList "-NoExit -Command `"cd '$BackendDir'; & '$ActivateScript'; python app.py`""

# 等待后端服务启动
Write-Host "等待后端服务启动..."
Start-Sleep -Seconds 5

# 打开前端页面
Write-Host "打开前端页面..."
$FrontendUrl = Join-Path $FrontendDir "index.html" -Resolve
Start-Process $FrontendUrl

Write-Host ""
Write-Host "========================================"
Write-Host "          MAGI SYSTEM STARTED           "
Write-Host "========================================"
Write-Host "后端服务地址: http://localhost:5000"
Write-Host "前端页面已在浏览器中打开"
Write-Host ""
Write-Host "按任意键退出脚本..."
$Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") | Out-Null
$Host.UI.RawUI.FlushInputBuffer()

# 恢复原始颜色
$Host.UI.RawUI.Reset()
Clear-Host