# korea-card-bin-api
한국카드에 대응되는 BIN Number 에 기반하여 정보를 알려주는 API 입니다 (21년 05월 기준 업데이트)

해외 bin lookup 툴과의 차이점으로는 
* 카드의 발행사 정보 뿐만 아니라 카드의 세부명 까지 제공 (EX:  BC / 코나카드,  BC / 카카오페이체크)
* 개인카드 및 법인카드 분류 
* ‘체크’, ‘선불’, ‘신용’, ‘기프트카드’ 분류
* 국내 VAN사에서 수집한 자료를 기반으로 하여 정확한 자료 제공
* 매월 업데이트 되는 데이터 제공 (자동 업데이트 기능 개발중)
* 2822개 이상의 데이터를 기반으로 제공 (21년 05월 기준)
* 온라인 API 제공 및 자바스크립트용 라이브러리로 제공

이 있습니다. 

![2B9E763D-B1DC-4CAE-83F9-0A87F6B80031](https://user-images.githubusercontent.com/24792377/118404024-341edc80-b6ac-11eb-91af-f154099da3ca.png)

샘플 데이터는 위와 같고, CARDOWNERTYPE의 경우 0일 경우 개인, 1일 경우 법인카드임을 표시합니다.

![image](https://user-images.githubusercontent.com/24792377/118404198-d212a700-b6ac-11eb-9b6e-91f2ac029129.png)

제공되는 데이터의 발행사 종류와 카드 종류는 위와 같습니다.

API의 경우 cardbin.hanukoon.com?bin=<데이터> 로 POST 요청을 하여 사용할 수 있고, 별다른 API 리밋은 없습니다 (만약 자주 요청을 하는 프로덕션 환경이라면 오프라인 라이브러리를 사용하길 권장합니다!

만약 부정확한 정보가 있다면 해당 레포에 이슈로 남겨주시면 대응할 수 있도록 하겠습니다.

또한, 원본 데이터 파일의 저작권 관련 문의가 있으실 경우 hanu@hanukoon.com 으로 메일 부탁드립니다.
