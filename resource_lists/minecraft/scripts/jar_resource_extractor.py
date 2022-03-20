from zipfile import ZipFile
import tempfile
import os

file_name = os.path.expanduser("~/.minecraft/versions/1.18.2/1.18.2.jar")

with tempfile.TemporaryDirectory() as output_dir:
	print(output_dir)

	# Extract all files
	with ZipFile(file_name, 'r') as zipfile:
		print('Extracting all the files now...')
		zipfile.extractall(output_dir)
		print("done")

	# List all recipes
	for root, dirs, files in os.walk(os.path.join(output_dir, "data/minecraft/recipes")):
		for file in files:
			print(os.path.join(root, file))
