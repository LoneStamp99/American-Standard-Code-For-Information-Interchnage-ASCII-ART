# Enable execution of system
# If not work type in Powershell terminal "Set-ExecutionPolicy RemoteSigned"
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Set icon
Set-ItemProperty -Path .\ascii-art-launcher.ps1 -Name 'Icon' -Value 'Ms_Kendrah.ico'

# Set Python path
$pythonPath = "C:\Python311\python.exe"

  # Prompt for user input
  $command = Read-Host "ascii-art>"

  # Set script path
  $scriptPath = "src/main.py"
  $scriptPath = "src/command.py"
  $scriptPath = "ascii.py"
  $scriptPath = "color.py"
  $scriptPath = "format_of_picture.py"

  # Print banner
  Clear-Host
  Get-Content banner.txt
  Write-Host ""

  # Print menu
Write-Host "(0) Image file name"
Write-Host "(1) Select ASCII encoding character: [""Standard"", ""Alphabet/Characters"", ""Binary"", ""#"", ""$"", ""*"", ""+"", ""="", ""."", ""-"", ""_"", "","", ""<"", "">"", ""^"", ""%"", ""~"", ""!"", ""?""]"
Write-Host "(2) Colorized/Non-colorized"
Write-Host "(3) Image dimensions ratio: [""1:1"", ""3:2"", ""5:4"", ""16:9"", ""1920:1090"", ""1280:720"", ""1080:1080""]"
Write-Host "(4) Save as: [""jpg"", ""png"", ""tiff"", ""bmp"", ""tga"", ""netpbm"", ""pdf"", ""psd"", ""raw""]"
Write-Host "(5) Background(Optional): [""White: D8D9DA"", ""Pink: FCBAAD"", ""Yellow: F0DE36"", ""Black: 222831"", ""Grey: 393E46"", ""Cyan: 4FC0D0"", ""Red: B70404"", ""Green: CAD315"", ""Oranged: E25822""]"
Write-Host "(6) Select folder or (defualt folder: Output)"
Write-Host "(7)Example: [""ascii-art-launcher.ps1 -Image[Images/sample.jpg] -Colorized[Yes] -Standard -Saveas[png] -Ratio[1:1] -Output[Output/Image.png]""]"
  # ...

  # Run script with arguments
  & $pythonPath $scriptPath $args

  # Get arguments from user
$image = Read-Host "Image path (default folder: Images)"
$colorized = Read-Host "Colorized (Yes/No)"
$encoding = Read-Host "Encoding"
$ratio = Read-Host "Image Dimensions"
$save = Read-Host "Save As"
$background = Read-Host "Background"
$output = Read-Host "Output"

# Validate user input
if ($image -notin @("Image name")) {
  Write-Error "Image not specified. Please enter image file name"
  continue
}
if ($colorized -ne "Yes" -and $colorized -ne "No") {
  Write-Error "Invalid input for Colorized. Please enter Yes or No."
  continue
}

if ($encoding -notin @("Standard", "Alphabet/Characters", "Binary", "#", "$", "*", "@", "+", "=", ".", "-", "_", ",", "<", ">", "^", "%", "~", "!", "?")) {
  Write-Error "Invalid input for Encoding. Please enter Standard, Alphabet, Binary, etc."
  continue
}

if ($ratio -notin @("1:1", "3:2", "5:4", "16:9", "1920:1090", "1280:720", "1080:1080")) {
    Write-Error "Invalid input for Image Dimensions. Please enter 1:1, 3:2..."
    continue
}

if ($save -notin @("jpg", "png", "tiff", "bmp", "tga", "netpbm", "pdf", "psd", "raw")) {
    Write-Error "Invalid input for file Extension. Please enter jpg, png, tiff and so on."
    continue
}

if ($background -notin @("White: D8D9DA", "Pink: FCBAAD", "Yellow: F0DE36", "Black: 222831", "Grey: 393E46", "Cyan: 4FC0D0", "Red: B70404", "Green: CAD315", "Oranged: E25822")) {
    Write-Error "Invalid input for Background. Please enter Yellow: F0DE36 and so on."
    continue
}
if ($output -notin @("Output folder")) {
  Write-Error "Output folder not specified. Please enter output path or (default: Output/Image.png)"
  continue
}

# Handle output from Python
if ($LASTEXITCODE -ne 0) {
  Write-Error "Error executing Python script"
}
else {
  Write-Host "ASCII art generated successfully!"
}

# Print menu and get selection
$selection = Read-Host "Enter menu selection"

# Call Python script based on selection
switch ($selection) {
  1 {
    & $pythonPath $scriptPath -Image $image
  }
  2 {
    $colorized = Read-Host "Colorized (Yes/No)?"
    & $pythonPath $scriptPath -Colorized $colorized
  }
  3 {
    $encoding = Read-Host "Enter encoding"
    & $pythonPath $scriptPath -Encoding $encoding
  }
  4 {
    $ratio = Read-Host "Ratio (1:1, 3:2, 5:4, 16:9, 1920:1090, 1280:720, or 1080:1080)?"
    & $pythonPath $scriptPath -Ratio $ratio
  }
  5 {
    $saveas = Read-Host "Save as (jpg, png, tiff, bmp, tga, netpbm, pdf, psd, or raw)?"
    & $pythonPath $scriptPath -Saveas $saveas
  }
  6 {
    $background = Read-Host "Background color (white, pink, yellow, black, grey, cyan, red, green, or orange)?"
    & $pythonPath $scriptPath -Background $background
  }
  7 {
    $output = Read-Host "Output folder?"
    & $pythonPath $scriptPath -Saveto $output
  }
  # etc for other options
}

# Pass inputs to Python
& $pythonPath command.py -Image $image -Colorized $colorized -Encoding $encoding -Ratio $ratio -Saveas $saveas -Background $background -Output $output


# Handle Python exit code
if ($LASTEXITCODE -ne 0) {
  Write-Error "Error executing Python script"
}
else {
  Write-Host "ASCII art generated successfully!"
}
