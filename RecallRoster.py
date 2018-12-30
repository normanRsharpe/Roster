# v1.2 24 December 2018
# United States Air Force (USAF)
# Primary POC: DERICK N. CHANDLER, Capt, USAF
# Occupational and Environmental Health Element Chief
# Work Email: derick.n.chandler.mil@mail.mil@mail
# Work Phone: 808-448-6769 (DSN: 315-448-6769)

#!/usr/bin/env python3

# This pulls the recall roster data from
# RecallRosterData.py file.
from RecallRosterData import *
while True:
# Requesting the name command.
	Name = input('Enter Name or Unit  ')
	
# Printing Recall Roster information.

# Printing info for Paul Lane, Maj
	if  'Paul' in Name or 'Lane' in Name \
		or 'Paul Lane' in Name or 'P Lane' \
		in Name or 'Paul L' in Name or 'paul' \
		in Name or 'lane' in Name:
		print(PL)
		
# Printing info for Derick Chandler, Capt.
	elif 'Derick' in Name or 'Chandler' in Name \
		or 'Derick Chandler' in Name or 'D Chandler' \
		in Name or 'Derick C' in Name or 'derick' in \
		Name or 'chandler' in Name:
		print(DC)

# Printing info for Samuel Ortiz, MSgt.
	elif 'Samuel' in Name or 'Ortiz' in Name \
		or 'Samuel Ortiz' in Name or 'S Ortiz' \
		in Name or 'Samuel O' in Name or 'samuel' \
		in Name or 'ortiz' in Name:
		print(SO)
		
# Printing info for Christopher Thornton, TSgt.
	elif 'Christopher' in Name or 'Thornton' in Name \
		or 'Christopher Thornton' in Name or \
		'C Thornton' in Name or 'Christopher T' in Name \
		or 'christopher' in Name or 'thornton' in Name:
		print(CT)
		
# Printing info for Nia Curry, SSgt.
	elif 'Nia' in Name or 'Curry' in Name \
		or 'Nia Curry' in Name or 'N Curry' \
		in Name or 'Nia C' in Name or 'nia' in \
		Name or 'curry' in Name:
		print(NC)
		
# Printing info for Chanel Taylor, SSgt.
	elif 'Chanel' in Name or 'Taylor' in Name \
		or 'Chanel Taylor' in Name or 'C Taylor' \
		in Name or 'Chanel T' in Name or 'chanel' \
		in Name or 'taylor' in Name:
		print(CT2)
		
# Printing info for Raphy Feolino, SSgt.	
	elif 'Raphy' in Name or 'Feolino' in Name \
		or 'Raphy Feolino' in Name or 'R Feolino' \
		in Name or 'Raphy F' in Name or 'raphy' in \
		Name or 'feolino' in Name:
		print(RF)
		
# Printing info for Ryan Clemente, SrA.
	elif 'Ryan' in Name or 'Clemente' in Name \
		or 'Ryan Clemente' in Name or 'R Clemente' \
		in Name or 'Ryan C' in Name or 'ryan' in \
		Name or 'clemente' in Name:
		print(RC)
		
# Printing info for Derrik Felton, SrA.		
	elif 'Derrik' in Name or 'Felton' in Name \
		or 'Derrik Felton' in Name or 'D Felton' \
		in Name or 'Derrik F' in Name or 'derrik' in \
		Name or 'felton' in Name:
		print(DF)
		
# Printing info for Danica Melosi, A1C.
	elif 'Danica' in Name or 'Melosi' in Name \
		or 'Danica Melosi' in Name or 'D Melosi' \
		in Name or 'Danica M' in Name or 'danica' in \
		Name or 'melosi' in Name:
		print(DM)
		
# Printing info for Michael Crain, A1C.	
	elif 'Michael' in Name or 'Crain' in Name \
		or 'Michael Crain' in Name or 'M Crain' \
		in Name or 'Michael C' in Name or 'michael' in \
		Name or 'crain' in Name:
		print(MC)
		
# Printing info for Samantha Campbell, A1C.
	elif 'Samantha' in Name or 'Campbell' in Name \
		or 'Samantha Campbell' in Name or 'S Campbell' \
		in Name or 'Samantha C' in Name or 'samantha' in \
		Name or 'campbell' in Name:
		print(SC)
		
# Printing info for Erica Daniels, A1C.
	elif 'Erica' in Name or 'Daniels' in Name \
		or 'Erica Daniels' in Name or 'E Daniels' \
		in Name or 'Erica D' in Name or 'erica' in \
		Name or 'daniels' in Name:
		print(ED)
		
# Printing info for Bioenvironmental Engineering Flt.
	elif 'Bioenvironmental Engineering' in Name or \
		'BE' in Name or 'Bio' in Name or 'Bioenvironmental' \
		in Name or 'bio' in Name or 'be' in Name or \
		'bioenvironmental engineering' in Name or \
		'bioenvironmental' in Name or '15 AMDS/SGPB' in Name\
		or 'SGPB' in Name or 'sgpb' in Name:
		print(BioFlt)
		
# Asks if you want the whole unit roster.
		Unit_Info = input('Do you want full flight roster?')
# Printing info for Bioenvironmental Engineering Flt if 'Yes'.
		if 'Yes' in Unit_Info or 'yes' in Unit_Info \
		or 'Y' in Unit_Info or 'y' in Unit_Info:
			print(PL, DC, SO, CT, NC, CT2, RF, RC, DF,
			DM, MC,SC, ED)

# Ends inquiry.
		elif 'No' in Unit_Info or 'no' in Unit_Info or \
		'N' in Unit_Info or 'n' in Unit_Info:

		
# Prints phrase when invalid.
	else:
		print('Please enter valid name.')