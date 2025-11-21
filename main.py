from pyscript import display, document

Club1 = {
'Clubname': 'Science club',
'Meeting Location': 'Science Lab',
'Meeting time': '3-4 pm',
'Description': 'will be doing experiments every week',
'Club moderator': 'Mr. Calpo', 
'Max members': '25'
}

display(Club1, target ='output') 

Club2 = {
'Clubname': 'Math club',
'Meeting Location': 'Room 506',
'Meeting time': '3-4pm',
'Description': 'will be doing Math practices every week',
'Club moderator': 'Mr. Ferma', 
'Max members': '21'
}

display(Club2, target ='output') 

Club3 = {
'Clubname': 'Basketball Varsity Club',
'Meeting Location': 'OBMC Quadrangle',
'meeting time': '3-5 pm',
'description': 'will do doing training and drills every week',
'club moderator': 'Mr. loreto', 
'max members': '30'
}

display(Club3, target ='output') 

Club4 = {
'Clubname': 'Volleyball Varsity Club',
'Meeting Location': 'OBMC Quadrangle',
'Meeting time': '3-5 pm',
'Description': 'will be doing training and drills every week',
'Club moderator': 'Mr. Gervacio', 
'Max members': '22'
}

display(Club4, target ='output') 

Club5 = {
'Clubname': 'Arts Club',
'Meeting Location': 'Music Room',
'Meeting time': '2:30-4:30 pm',
'Description': 'will be doing art activites every week',
'Club moderator': 'Ms. Suarez ', 
'Max members': '20'
}

display(Club5, target ='output') 

def getting_info(e):
    document.getElementById('output').innerHTML = ""

