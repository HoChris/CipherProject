import PySimpleGUI as sg
import sys
from SubCipher import SubCipher as cip

#GUI Layout 
layout = [  [sg.Text('Enter Encryption Key')],
			[sg.Input()],
			[sg.Text('Enter a Message to Encrypt')],
			[sg.Multiline(size=(80,5))],
			[sg.Button('Encrypt'), sg.Button('Decrypt')],
			[sg.Text('Encryption', size=(37,1)), sg.Text('Decryption', size=(10,1))],
			[sg.Output(size=(40,7),key='_encrypt_'), sg.Output(size=(40,7),key='_decrypt_')],
			[sg.Exit()]  ]

window = sg.Window('SubCipher').Layout(layout)

# Initiallize class
cipher = cip()

# read and output encrypted message or output decrypted message
while True:
	event, values = window.Read()
	if event is None or event == 'Exit':
		break
	print(event, values)
	window.FindElement(key).Update()