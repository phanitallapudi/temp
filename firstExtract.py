import xml.etree.ElementTree as sol
import pandas as pan

#above two modules are needed to perform the action

from tkinter import Tk     
from tkinter.filedialog import askopenfilename
import time

#above three modules semi-automates the process for ease of use

cols = ["id","fullname","classfc","Cmmdty","NtnlCcy"]
rows = []
print("\n************************************************\n")
print("Select the XML file to convert it to CSV")
print("\n************************************************\n")
time.sleep(1)
Tk().withdraw()
filename = askopenfilename() 

#Tkinter module is used to get the file destination address and used to parse the file for the next process
try:
	if filename[-3:] == 'xml':				#if the file selected ends with an extension xml, then only it will continue the process
		xmlparse = sol.parse(filename)
		root = xmlparse.getroot()
		for zeroX in root:
			theid = zeroX.find("Id").text
			fname = zeroX.find("FullNm").text
			fcclass = zeroX.find("ClssfctnTp").text
			Cmdty = zeroX.find("CmmdtyDerivInd").text
			NtnlC = zeroX.find("NtnlCcy").text

			rows.append({"id": theid,
						"fullname": fname,
						"classfc": fcclass,
						"Cmmdty": Cmdty,
						"NtnlCcy": NtnlC 
						})

		df = pan.DataFrame(rows, columns=cols)

		# Writing dataframe to csv
		df.to_csv('extracteddata.csv')
		
		print("\n************************************************\n")
		print("CSV file created and saved under the User folder.")

	else:
		print("It should be an XML file, not {} file".format(filename[-3:]))

except AttributeError:
	print("\nSomething went wrong please try again..")
except IndexError:
	print("\nSomething went wrong please try again..")
except KeyboardInterrupt:
	print("\nSomething went wrong please try again..")
