# fetch-images.ps1
# Downloads all original images from the old azqato.com Google Sites pages.
# Run from the project root: .\oldwebsite\fetch-images.ps1

$imgDir = Join-Path $PSScriptRoot "img"
New-Item -ItemType Directory -Force -Path $imgDir | Out-Null

$ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

$baseHeaders = @{
    "User-Agent" = $ua
    "Accept"     = "image/avif,image/webp,image/apng,image/*,*/*;q=0.8"
    "Referer"    = "https://www.azqato.com/"
}

function Save-Image {
    param([string]$Url, [string]$Name, [hashtable]$Headers = $null)
    $dest = Join-Path $imgDir $Name
    try {
        $params = @{
            Uri             = $Url
            OutFile         = $dest
            TimeoutSec      = 20
            UseBasicParsing = $true
            ErrorAction     = "Stop"
        }
        if ($Headers) { $params["Headers"] = $Headers }
        Invoke-WebRequest @params
        $size = (Get-Item $dest).Length
        if ($size -lt 500) {
            Remove-Item $dest -Force
            Write-Host "  SKIP  $Name (response too small - likely blocked)" -ForegroundColor Yellow
        } else {
            $kb = [math]::Round($size / 1KB, 1)
            Write-Host "  OK    $Name ($kb KB)" -ForegroundColor Green
        }
    } catch {
        $msg = $_.Exception.Message
        Write-Host "  FAIL  $Name - $msg" -ForegroundColor Red
    }
}

function Get-PageHtml {
    param([string]$Url)
    $res = Invoke-WebRequest -Uri $Url -UserAgent $ua -UseBasicParsing -TimeoutSec 20 -ErrorAction Stop
    return $res.Content
}

# -- 1. Known images from page analysis (with Referer to satisfy Google CDN) --

Write-Host ""
Write-Host "[1/3] Downloading known images..." -ForegroundColor Cyan

$known = @(
    @{
        Name = "logo-cat-avatar.jpg"
        Url  = "https://lh3.googleusercontent.com/sitesv/AA5AbUC2jaO5t-QP5IhHjrwl1EtJ-4jL4-zlqr4FUJtN7_14CTpe1-ZJX1_qaJkXgXTNcAQrW-D3hmLvu78IgokZXm-1IysgqKLWe1xZBwwH119gy6tg-Zo1pEUVARSi2S13xobbTPgxlcN6h8mkNy2G6Pb-9GMvAWkCXiqj2GH9magjSgxSgHYPUvamVc82uQQ=w16383"
    },
    @{
        Name = "home-hero-profile.jpg"
        Url  = "https://lh3.googleusercontent.com/sitesv/AA5AbUAwmfT1nVQ1qysQ4sCcg-v8E12SylCrnqM16PXBtJ8HxydTc-xrV1CPZFDpZiAh1ZQEUKqrBa_MwYMvbrvhv9PZ1Pxjlpvnu3GUkM9oCvTHadGay2zWU5Vnj9hODozFqEVQFOqRsxWXndoDNKiZKEWEqw-soG4kwjwjtDtYutnNh6Mh7BEqSoUyqxk1dqg=w1280"
    },
    @{
        Name = "about-profile.jpg"
        Url  = "https://lh3.googleusercontent.com/sitesv/AA5AbUBh7pjeWLlGpGCrimun8uitCQxERJBO5p9H3EQekcaKjmICcWVSs1O1riV7lPSBkrf0So8xhApJcaoBvMWDOdiySgU-1NulgK2X6FCkrIvufBe4Cu_Q6wvggQIKSDGfyw2GnpCZeL-CFd_M2vybbk4DEBgoLEuB4kaPFz2qW9cQ5m0yYFXJM7cZAA5oNHU=w1280"
    }
)

foreach ($img in $known) {
    Save-Image -Url $img.Url -Name $img.Name -Headers $baseHeaders
}

# -- 2. Scrape each page for additional Google Sites CDN images ----------------

Write-Host ""
Write-Host "[2/3] Scraping pages for additional images..." -ForegroundColor Cyan

$pages = @(
    @{ Name = "home";     Url = "https://www.azqato.com/home"     },
    @{ Name = "about";    Url = "https://www.azqato.com/about"    },
    @{ Name = "links";    Url = "https://www.azqato.com/links"    },
    @{ Name = "youtube";  Url = "https://www.azqato.com/youtube"  },
    @{ Name = "invests";  Url = "https://www.azqato.com/invests"  },
    @{ Name = "music";    Url = "https://www.azqato.com/music"    },
    @{ Name = "accounts"; Url = "https://www.azqato.com/accounts" }
)

$seen = [System.Collections.Generic.HashSet[string]]::new()
foreach ($img in $known) { $seen.Add($img.Url) | Out-Null }

$scraped = [System.Collections.Generic.List[hashtable]]::new()

foreach ($page in $pages) {
    Write-Host "  Scanning /$($page.Name)..."
    try {
        $html = Get-PageHtml -Url $page.Url

        $patterns = @(
            'src="(https://lh3\.googleusercontent\.com/sitesv/[^"]+)"',
            "src='(https://lh3\.googleusercontent\.com/sitesv/[^']+)'",
            'url\("(https://lh3\.googleusercontent\.com/sitesv/[^"]+)"\)'
        )

        foreach ($pattern in $patterns) {
            $rxMatches = [regex]::Matches($html, $pattern)
            foreach ($m in $rxMatches) {
                $url = $m.Groups[1].Value
                if ($seen.Add($url)) {
                    $scraped.Add(@{ Url = $url; Page = $page.Name })
                }
            }
        }
        $count = ($scraped | Where-Object { $_.Page -eq $page.Name }).Count
        Write-Host "    Found $count new image(s)"
    } catch {
        $msg = $_.Exception.Message
        Write-Host "    Could not fetch - $msg" -ForegroundColor Yellow
    }
}

$idx = 1
foreach ($img in $scraped) {
    $name = "scraped-$($img.Page)-$idx.jpg"
    Save-Image -Url $img.Url -Name $name -Headers $baseHeaders
    $idx++
}

if ($scraped.Count -eq 0) {
    Write-Host "  No additional images found (pages may be JS-rendered)." -ForegroundColor Yellow
}

# -- 3. YouTube channel avatars via og:image ----------------------------------

Write-Host ""
Write-Host "[3/3] Fetching YouTube channel avatars..." -ForegroundColor Cyan

$channels = @(
    @{ Name = "yt-channel-azqato.jpg";  Url = "https://www.youtube.com/@Azqato" },
    @{ Name = "yt-channel-streams.jpg"; Url = "https://www.youtube.com/channel/UCar9s_yiJUFWnM-20fLU5dw" },
    @{ Name = "yt-channel-mixes.jpg";   Url = "https://www.youtube.com/channel/UCV2X1axZ19iubEzgkouPSCQ" },
    @{ Name = "yt-channel-chills.jpg";  Url = "https://www.youtube.com/channel/UC1ytKNtxdBWCiiSQ6DGsxHA" }
)

foreach ($ch in $channels) {
    try {
        $html = Get-PageHtml -Url $ch.Url

        # Extract og:image from channel page
        $m = [regex]::Match($html, '<meta property="og:image" content="([^"]+)"')
        if (-not $m.Success) {
            $m = [regex]::Match($html, '"thumbnail"\s*:\s*\{"thumbnails"\s*:\s*\[.*?"url"\s*:\s*"([^"]+)"', [System.Text.RegularExpressions.RegexOptions]::Singleline)
        }

        if ($m.Success) {
            $thumbUrl = $m.Groups[1].Value -replace '\\u0026', '&'
            Save-Image -Url $thumbUrl -Name $ch.Name
        } else {
            Write-Host "  SKIP  $($ch.Name) - could not extract avatar URL" -ForegroundColor Yellow
        }
    } catch {
        $msg = $_.Exception.Message
        Write-Host "  FAIL  $($ch.Name) - $msg" -ForegroundColor Red
    }
}

# -- Summary ------------------------------------------------------------------

Write-Host ""
$saved = Get-ChildItem $imgDir -File -ErrorAction SilentlyContinue
if ($saved) {
    Write-Host "Done. $($saved.Count) file(s) saved to oldwebsite\img\" -ForegroundColor Cyan
    foreach ($f in $saved) {
        $kb = [math]::Round($f.Length / 1KB, 1)
        Write-Host "  $($f.Name) ($kb KB)"
    }
} else {
    Write-Host "Done. No files saved." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "The Google Sites CDN URLs require a valid browser session." -ForegroundColor Yellow
    Write-Host "To save the images manually:" -ForegroundColor Yellow
    Write-Host "  1. Open each azqato.com page in your browser" -ForegroundColor Yellow
    Write-Host "  2. Right-click each image -> Save image as -> oldwebsite\img\" -ForegroundColor Yellow
    Write-Host "  3. Use the names: logo-cat-avatar, home-hero-profile, about-profile" -ForegroundColor Yellow
}
