# Notys
Basic Notes App with cardview and changing size/number cards within resizing window.
![alt text](https://raw.githubusercontent.com/MelonLemon/NotesApp/master/ui/snapshots/snapShotFull.png)

This app implements basic functionality of CRUD notes + search. Back-end - sqlLite. Front-End - Qt(Python)  
![alt text](https://raw.githubusercontent.com/MelonLemon/NotesApp/master/ui/snapshots/snapShot1.PNG)
![alt text](https://raw.githubusercontent.com/MelonLemon/NotesApp/master/ui/snapshots/snapShot2.PNG)

Display of note are made with QTableView. I made them as a Cardview with Delegate that draw rectangle, color and place text with date of the note.
Display of notes implement similar logic to flatlist(React) or LazyColumn(Jetpack Compose). CardViewModel display only limit number of rows at once(I limit it to 5 rows section), than you scroll down/up it changes sections to show and update table. That gives effect of endless list. It also handles changes of columns number - notes in the row. 
Notes are resizing with resizing the window. Width of note grows till you can put another note with minimum width. I limit display to 8 notes in a row(8 columns).

![alt text](https://raw.githubusercontent.com/MelonLemon/NotesApp/master/ui/snapshots/snapShot4.PNG)
![alt text](https://raw.githubusercontent.com/MelonLemon/NotesApp/master/ui/snapshots/snapShot6.PNG)
It has a "search" where it shows notes that has text in search box.  
![alt text](https://raw.githubusercontent.com/MelonLemon/NotesApp/master/ui/snapshots/snapShot5.PNG)

PS. 
Design Credits: This NotesApp heavily based on design by Amal ["A simple and lightweight note app"](https://dribbble.com/shots/11875872-A-simple-and-lightweight-note-app/attachments/3501130?mode=media)

