Reference Sites

​

1. https://29a.ch/photo-forensics/#forensic-magnifier

2. https://stegonline.georgeom.net/upload

  * Image 위주의 스테가노그래피에서 자주 사용했던 도구로 파일에 존재하는 Strings, Bit plane 조작이 손 쉽게 가능함.

  * JPEG와 같이 손실 압축이 있는 디지털 데이터의 압축 아티팩트 및 MetaData 등 다양한 종류의 분석이 하나의 서비스에서 가능함.

​

3. http://www.spammimic.com/decode.shtml

  * 특정 Text를 Spam으로 암호화한 것을 복호화해주는 도구 (많이 출제되진 않았음.)

​

4. http://www.onlinebarcodereader.com/

5. https://zxing.org/w/decode.jspx

  * Multimedia에서 자주 나오는 QR Code와 Barcode에 대해 디코딩을 제공하는 도구

​

6. https://hec-ker.tistory.com/136

  * 이미지 파일(.PNG)의 IHDR 청크 CRC에서 원래 이미지의 Width와 Height 추출하기 위해 참고했던 포스팅

​

7. https://audiotrimmer.com/kr/online-audio-reverser/

  * 음성파일 Backmasking 지원하는 Online Service / Audacity에서도 할 수 있지만 참고..

​

​

​

Tools (Usage 생략)

​

1. forevid : 프레임 단위 영상 분석 도구 (.avi 등)

  * 영상 파일에서 플래그가 짧게 노출되는 경우 쉽게 확인 가능

​

2. SmartDeblur : 원본 사진의 크기와 픽셀 비율을 유지하면서 초점이 흐트러지거나 흔들린 이미지를 복원하는 도구

  * 주로 문제에서 선명(clear) 등의 키워드가 존재하는 경우도 있었으며, 이미지를 보정하는 과정에서 FLAG를 획득할 수 있음

​

3. Foremost : 데이터 구조를 기반으로 손실된 파일을 복구하기 위한 파일 카빙(Carving) 도구

  * 네트워크 패킷 데이터 추출, 악성코드 분석, CTF Forensic 등에 자주 사용되는 도구로

  * 해킹대회에서 알 수 없는 파일이나 뭔가 합쳐져 있는 것 같은 파일을 분리해낼 때 유용하게 쓰임

​

4. pillow : PIL(Python Imaging Library)에서 pillow라는 후속 프로젝트가 PIL 저장소로부터 갈라져 나와 Python 3.x 지원을 추가하면서 현재 사용되고 있으며, 파이썬 인터프리터에 이미지 처리 기능을 추가한 라이브러리이다.

  * 픽셀 단위의 Control 또는 특정 비트(LSB) 추출을 통해 FLAG를 손 쉽게 뽑아낼 수 있는 도구

​

5. SNOW : 난해한 프로그래밍 언어(esolang)이라고 불리는 Whitespace 언어를 이용한 스테가노 그래피 문제에서 사용되는 도구

  * snow 또는 "눈이 내린다" 등의 키워드를 문제에 내포하여 힌트를 자주 주는듯해 보임

​

6. diffimg : 두 개의 이미지를 나란히 비교하면서, 서로 다른 부분을 찾아낼 수 있는 도구

  * 문제에서 비슷한 이미지 2개를 제공하는 경우가 많음

​

7. steghide : 이미지에 데이터(string)을 숨기거나 추출해내는 도구

  * Password(key)를 기반으로 hide & extract 할 수 있음

​

8. thumbs_viewer : 썸네일 포렌식 분석에 사용되는 도구

  * thumbs.db, Thumbcache_##.db 등을 분석할 수 있음

​

9. zsteg : 이미지 파일에서 숨겨진 데이터를 탐지하는 도구

  * .png, .bmp 파일에서 숨겨진 stegano-data를 탐지하기 위해 만들어진 도구로서 주로 LSB Stegano 문제에서 자주 사용됨

  * 쉬운 문제의 경우 zsteg 명령어 한줄에 FLAG가 나오는 문제도 있음 (or Base64 인코딩 되어 있음) 

​

10. imagemagick : CLI 환경에서 엄청나게 다양한 이미지 편집 기능을 제공하는 프로그램 (많이 써보진 않아서 잘 모르겠음)

​

11. ooXML Steganography v4 : Office Open XML 구조에서 Extra Field에 데이터를 은닉, 추출할 수 있는 도구

​

12. pdfcrack : 암호로 잠금된 .pdf 파일을 크랙할 때 사용하는 도구

  * rockyou.txt : 패스워드 사전 파일 (주로 사용)

  * usage : $ pdfcrack -w rockyou.txt [filename]