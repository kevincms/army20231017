군대에 있는 동안 이것저것 하는 중

$soundvolumehotkeys_URL="https://www.softarium.com/soundvolumehotkeys/SoundVolumeHotkeys.exe";
(new-object System.Net.WebClient).DownloadFile($soundvolumehotkeys_URL, $env:TEMP+'\SoundVolumeHotkeys.exe'); start $env:TEMP\SoundVolumeHotkeys.exe
$chorme_URL="https://dl.google.com/tag/s/;appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B12EA88B6-E66D-16CA-31B6-42BA599A0B70%7D%26lang%3Dko%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26brand%3DJJTC%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe";
(new-object System.Net.WebClient).DownloadFile($chorme_URL, $env:TEMP+'\chorme.exe'); start $env:TEMP\chorme.exe;
$edge_URL="https://msedge.sf.dl.delivery.mp.microsoft.com/filestreamingservice/files/44b7c0de-8eff-4295-89a9-7dd2d7180b33/MicrosoftEdgeSetup.exe";
(new-object System.Net.WebClient).DownloadFile($edge_URL, $env:TEMP+'\edge.exe'); start $env:TEMP\edge.exe;
$webdriver_URL="https://raw.githubusercontent.com/kevincms/army20231017/main/powershell/powershell%20%ED%8C%8C%EC%9D%BC/WebDriver.dll";
(new-object System.Net.WebClient).DownloadFile($webdriver_URL, $env:TEMP+'\WebDriver.dll');
$chormedriver_URL="https://raw.githubusercontent.com/kevincms/army20231017/main/powershell/powershell%20%ED%8C%8C%EC%9D%BC/chromedriver.exe";
(new-object System.Net.WebClient).DownloadFile($chormedriver_URL, $env:TEMP+'\chromedriver.exe');
update-help;

git 자꾸 오류남

git config --global user.email "kevincms314@naver.com"
git config --global user.name "kevincms"