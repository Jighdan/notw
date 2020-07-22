## Configuration
You can configure the database directory, filename and table name in the `notw/__init__.py` file.

## Installation
Requires Python>=3.8

### Using Pip
```bash
	$ cd notw
	$ sh install.sh
```

### Manual
```bash
	$ git clone https://github.com/Jighdan/notw
	$ cd notw
	$ pip install -e . || pip3 install -e .
```

## Usage

```bash
	$ notw
	
	# adds a new note
	$ notw -n "YOUR NOTE HERE"
	
	# (X Represents the note index)
	# deletes a note
	$ notw -d X
	# updates a note content
	$ notw -u X "NEW CONTENT HERE"
```
