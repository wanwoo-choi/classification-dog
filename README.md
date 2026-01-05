# 견종 인식 프로그램 (Dog Species Recognition)

이 프로젝트는 딥러닝(CNN)을 사용하여 강아지 사진의 품종을 인식하는 프로그램입니다.

## 필요 파일
프로그램 실행을 위해 다음 파일들이 **같은 폴더**에 있어야 합니다:
1.  `dog_species_classification.py`: 메인 프로그램 소스 코드
2.  `cnn_for_stanford_dogs.h5`: 학습된 딥러닝 모델 파일
3.  `dog_species_names.txt`: 견종 이름 데이터 파일
4.  `requirements.txt`: 필요 라이브러리 목록
5.  `Images.zip`: 강아지 샘플 이미지 (압축 파일)

## 설치 방법 (Installation)

파이썬이 설치된 환경에서 아래 명령어로 필요한 라이브러리를 설치하세요.

```bash
pip install -r requirements.txt
```

## 실행 방법 (Execution)

터미널이나 명령 프롬프트에서 아래 명령어로 실행합니다.

```bash
python dog_species_classification.py
```

## 참고 사항
- 윈도우 환경에서는 인식 성공 시 알림음이 발생합니다.
- 다른 운영체제(macOS, Linux)에서는 알림음 없이 동작하도록 설정되어 있습니다.
