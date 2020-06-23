from note_class import Note
import database_manager

if __name__ == '__main__':
	database_manager.present_database()
	new_note = input("\nNew Note: ")
	new_note = Note(new_note)
	database_manager.save(new_note.packed())
	database_manager.present_database()

