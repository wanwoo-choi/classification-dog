import cv2 as cv 
import numpy as np
import tensorflow as tf
try:
    import winsound
except ImportError:
    winsound = None
import pickle
import sys
from PyQt5.QtWidgets import *

# 모델과 데이터 로드 (파일 경로가 정확해야 합니다)
cnn = tf.keras.models.load_model('cnn_for_stanford_dogs.h5')
dog_species = pickle.load(open('dog_species_names.txt', 'rb'))

class DogSpeciesRecognition(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.setWindowTitle('견종 인식')
        self.setGeometry(200, 200, 700, 100)
       
        # '품종 인식' 버튼 제거함
        fileButton = QPushButton('강아지 사진 열기', self) 
        quitButton = QPushButton('나가기', self) 
        
        # 버튼 위치 조정
        fileButton.setGeometry(10, 10, 100, 30)
        quitButton.setGeometry(510, 10, 100, 30)
        
        # 버튼 연결
        fileButton.clicked.connect(self.pictureOpenFunction)
        quitButton.clicked.connect(self.quitFunction)
        
    def pictureOpenFunction(self):
        # 파일 열기 대화상자
        fname = QFileDialog.getOpenFileName(self, '강아지 사진 읽기', './')
        
        # [수정] 취소 버튼을 눌렀을 때 오류가 나지 않고 그냥 함수를 종료하도록 변경
        if not fname[0]:
            return 

        # 이미지 읽기
        self.img = cv.imread(fname[0])
        
        # [수정] 이미지가 없으면 프로그램 종료(sys.exit) 대신 경고 메시지 출력 후 리턴
        if self.img is None: 
            print("이미지를 읽을 수 없습니다.")
            return
        
        # 이미지가 정상적으로 열리면 바로 인식 기능 실행
        self.runRecognition()

    # 기존 recognitionFunction을 내부에서 호출하기 좋게 이름 변경 및 수정
    def runRecognition(self):
        # 원본 비율 유지를 위해 보여줄 때는 원본(self.img)을 쓰고, 예측할 때만 리사이즈
        x = np.reshape(cv.resize(self.img, (224, 224)), (1, 224, 224, 3))
        res = cnn.predict(x)[0]       # 예측
        
        top5 = np.argsort(-res)[:5]
        top5_dog_species_names = [dog_species[i] for i in top5]
        
        for i in range(5):
            prob = '(' + str(round(res[top5[i]] * 100, 2)) + '%)' # 확률을 보기 좋게 %로 변경 (선택사항)
            name = str(top5_dog_species_names[i]).split('-')[1]
            
            # 텍스트 그리기 (색상: 파란색)
            cv.putText(self.img, prob + name, (10, 100 + i * 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
        
        # 결과 이미지 띄우기
        cv.imshow('Dog image', self.img)   
        if winsound:
            winsound.Beep(1000, 500)
                
    def quitFunction(self):
        cv.destroyAllWindows()        
        self.close()
              
app = QApplication(sys.argv) 
win = DogSpeciesRecognition() 
win.show()
app.exec_()