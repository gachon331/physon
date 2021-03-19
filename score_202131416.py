# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 18:29:41 2021

@author: ng110
"""

score1= int(input("1회차 성적 점수를 입력해주세요: "))
score2= int(input("2회차 성적 점수를 입력해주세요: "))
score3= int(input("3회차 성적 점수를 입력해주세요: "))
score4= int(input("4회차 성적 점수를 입력해주세요: "))
score5= int(input("5회차 성적 점수를 입력해주세요: "))
score6= int(input("6회차 성적 점수를 입력해주세요: "))
score7= int(input("7회차 성적 점수를 입력해주세요: "))
score8= int(input("8회차 성적 점수를 입력해주세요: "))
score9= int(input("9회차 성적 점수를 입력해주세요: "))
score10= int(input("10회차 성적 점수를 입력해주세요: "))
score11= int(input("11회차 성적 점수를 입력해주세요: "))
score12= int(input("12회차 성적 점수를 입력해주세요: "))
score13= int(input("13회차 성적 점수를 입력해주세요: "))
score14= int(input("14회차 성적 점수를 입력해주세요: "))
score15= int(input("15회차 성적 점수를 입력해주세요: "))
test1= int(input("중간고사 성적 점수를 입력해주세요: "))
test2= int(input("기말고사 성적 점수를 입력해주세요: "))


average = (score1+score2+score3+score4+score5+score6+score7+score8+score9+score10+score11+score12+score13+score14+score15)/15

total = (average*0.4)+(test1*0.3)+(test2*0.3)

if  100 >= total > 90:
       grade = "A"
elif 90 >= total > 80:
        grade = "B"
elif 80 >= total > 70:
        grade = "C"
elif 70 >= total > 60:
        grade = "D"
elif total <= 60:
        grade = "F"


print("1~15회차 과제점수는 ", int(average*0.4), "(반영비율 0.4)입니다.")
print("중간고사 점수는 ", int(test1*0.3), "(반영비율 0.3)입니다.")
print("기말고사 점수는 ", int(test2*0.3), "(반영비율 0.3)입니다.")
print("합게는 ", int(total), "입니다.")
print("성적은 ", grade, "입니다.")