volatility_2.6_win64_standalone.exe -f .\Target1-1dd8701f.vmss imageinfo 

명령어를 통해서 Profile을 알아냅니다.

Suggested Profile(s) : Win7SP1x86_23418, Win7SP0x86, Win7SP1x86

이제 프로세스 정보 확인 해보겠습니다.

volatility_2.6_win64_standalone.exe -f .\Target1-1dd8701f.vmss --profile=Win7SP1x86_23418 pstree > pstree.txt

여기서 OUTLOOK.EXE가 의심됩니다.

volatility_2.6_win64_standalone.exe -f .\Target1-1dd8701f.vmss --profile=Win7SP1x86_23418 memdump -p 3196 -D ./

메모리덤프를 확인해보겠습니당

strings.exe .\3196.dmp >> 3196.txt

3196.txt 에 @gmail.com 을 검색해보면 
th3wh1t3r0s3@gmail.com < - 이메일을 찾을 수 있습니다 

Flag : th3wh1t3r0s3@gmail.com
