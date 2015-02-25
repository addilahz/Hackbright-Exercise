cs_partner_info = {}
cs_partner_info ['age'] = 26
cs_partner_info ['eye color'] = 'dark brown'
cs_partner_info ['fave color'] = 'blue'
cs_partner_info ['fave food'] = 'pesto pizza'
cs_partner_info ['current time'] = '5:02pm'
cs_partner_info ['last name'] = 'zakaria'
cs_partner_info ['fave song'] = 'song1: thinking out loud, song2: shake it off, song3: sugar'
cs_partner_info ['fave no'] =  '2, 12, 22, 82'


#print current time
print cs_partner_info ['current time']

# print NOW as current time
cs_partner_info ['current time'] = 'NOW'
print cs_partner_info ['current time']

#print entire dictionary
print cs_partner_info

#delete eye color & print again entire dictionary 
del cs_partner_info ['eye color']
print cs_partner_info

#delete fave color
del cs_partner_info ['fave color']
print cs_partner_info

#check last name in dictionary
'last name' in cs_partner_info
#answer: True becuase last name is in the dictionary

# check age
'age' in cs_partner_info
#answer: True because theres an age in the dictionary


