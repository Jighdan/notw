## Configuration
You can configure the database directory, filename and table name in the `notew/__init__.py` file.

## Installation
Requires Python>=3.8

### Using Pip
```bash
	$ cd notew
	$ sh install.sh
```

### Manual
```bash
	$ git clone https://github.com/Jighdan/notew-cli
	$ cd notew-cli
	$ pip install -e . || pip3 install -e .
```

## Usage

```bash
	$ notew
	
	# adds a new note
	$ notew -n "YOUR NOTE HERE"
	
	# (X Represents the note index)
	# deletes a note
	$ notew -d X
	# updates a note content
	$ notew -u X "NEW CONTENT HERE"
```
