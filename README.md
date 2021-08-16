# NotesApp
Basic Notes App with cardview and changing size/number cards within resizing
This NotesApp based on design by Amal "A simple and lightweight note app"

![alt text](https://raw.githubusercontent.com/MelonLemon/NotesApp/master/ui/snapshots/snapShot1.PNG)
![alt text](https://raw.githubusercontent.com/MelonLemon/NotesApp/master/ui/snapshots/snapShot2.PNG)

It's simple notes app. 

Display of note are made with QTableView. I made them as a Cardview with Delegate that draw rectangle, color and place text with date of the note.
Display of notes are similar to flatlist. CardViewModel display only limit number of rows at once(I limit it to 5 rows section), than you scroll down/up it changes sections to show and update table. That gives effect of endless list. It also handles changes of columns number - notes in the row. 
Notes are resizing with resizing the window. Width of note grows till you can put another note with minimum width. I limit display to 8 notes in a row(8 columns).

![alt text](https://raw.githubusercontent.com/MelonLemon/NotesApp/master/ui/snapshots/snapShot4.PNG)
![alt text](https://raw.githubusercontent.com/MelonLemon/NotesApp/master/ui/snapshots/snapShot6.PNG)
It has a "search" where it shows notes that has text in search box.  
![alt text](https://raw.githubusercontent.com/MelonLemon/NotesApp/master/ui/snapshots/snapShot5.PNG)

