import pyautogui
import time

pyautogui.alert("Sou uma IA e vou começar a fazer a automação! Não mexa em nada!")
pyautogui.PAUSE = 0.8
#Abri o chrome no meu computador
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://web.facebook.com/')
pyautogui.press('enter')
time.sleep(1)
#Clico para escrever algo e escrevo
pyautogui.moveTo(450,450)
pyautogui.doubleClick(450,450)
time.sleep(3)
pyautogui.write('Ola pessoal bom fim de semana para todos!')
pyautogui.moveTo(450,570)
pyautogui.doubleClick(450,570)
pyautogui.alert("Parabens Camilo Voce conseguiu meu mestre!")
