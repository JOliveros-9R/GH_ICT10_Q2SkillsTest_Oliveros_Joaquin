from pyscript import document

Club1 = {
    'Clubname': 'Science Club',
    'Meeting Location': 'Science Lab',
    'Meeting time': '3-4 pm',
    'Description': 'Will be doing experiments every week',
    'Club moderator': 'Mr. Calpo', 
    'Max members': '25'
}

Club2 = {
    'Clubname': 'Math Club',
    'Meeting Location': 'Room 506',
    'Meeting time': '3-4 pm',
    'Description': 'Will be doing Math practices every week',
    'Club moderator': 'Mr. Ferma', 
    'Max members': '21'
}

Club3 = {
    'Clubname': 'Basketball Varsity Club',
    'Meeting Location': 'OBMC Quadrangle',
    'Meeting time': '3-5 pm',
    'Description': 'Will be doing training and drills every week',
    'Club moderator': 'Mr. Loreto', 
    'Max members': '30'
}

Club4 = {
    'Clubname': 'Volleyball Varsity Club',
    'Meeting Location': 'OBMC Quadrangle',
    'Meeting time': '3-5 pm',
    'Description': 'Will be doing training and drills every week',
    'Club moderator': 'Mr. Gervacio', 
    'Max members': '22'
}

Club5 = {
    'Clubname': 'Arts Club',
    'Meeting Location': 'Music Room',
    'Meeting time': '2:30-4:30 pm',
    'Description': 'Will be doing art activities every week',
    'Club moderator': 'Ms. Suarez', 
    'Max members': '20'
}

CLUBS = {
    'Science': Club1,
    'Math': Club2,
    'Basketball': Club3,
    'Volleyball': Club4,
    'Arts': Club5
}

def show_Club(e):
    sel = document.getElementById("club_select")
    key = sel.value
    club = CLUBS[key]   
    out = document.getElementById("Club")

    html = f"""
    <h5>{club['Clubname']}</h5>
    <p><strong>Description:</strong> {club['Description']}</p>
    <p><strong>Meeting Time:</strong> {club['Meeting time']}</p>
    <p><strong>Location:</strong> {club['Meeting Location']}</p>
    <p><strong>Moderator:</strong> {club['Club moderator']}</p>
    <p><strong>Max Members:</strong> {club['Max members']}</p>
    """
    out.innerHTML = html