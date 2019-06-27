import xml.etree.cElementTree as ET
import json 
class Converter:

	def __init__(self):
		pass

	def checkJson(self,data):
		if data != None and  data != {}:
			if data['data'] != None and data['data'] != []:
				for image in data['data']:
					try:
						tmp=image["annotation"]["folder"]
					except:
						print("[ERROR] Attribute Not found annotation.folder .")
						return 0
					try:
						tmp=image["annotation"]["filename"]
					except:
						print("[ERROR] Attribute Not found annotation.filename .")
						return 0
					try:
						tmp=image["annotation"]["path"]
					except:
						print("[ERROR] Attribute Not found annotation.path .")
						return 0
					try:
						tmp=image["annotation"]["source"]["database"]
					except:
						print("[ERROR] Attribute Not found annotation.source.database .")
						return 0
					try:
						tmp=image["annotation"]["size"]["width"]
					except:
						print("[ERROR] Attribute Not found annotation.size.width .")
						return 0
					try:
						tmp=image["annotation"]["size"]["height"]
					except:
						print("[ERROR] Attribute Not found annotation.size.height .")
						return 0
					try:
						tmp=image["annotation"]["size"]["depth"]
					except:
						print("[ERROR] Attribute Not found annotation.size.depth .")
						return 0
					try:
						tmp=image["annotation"]["source"]["database"]
					except:
						print("[ERROR] Attribute Not found annotation.source.database .")
						return 0
					try:
						tmp=image["annotation"]["segmented"]
					except:
						print("[ERROR] Attribute Not found annotation.segmented .")
						return 0


					for obj in  image["annotation"]["object"]:
						try:
							tmp=obj["name"]
						except:
							print("[ERROR] Attribute Not found annotation.object.name .")
							return 0
						try:
							tmp=obj["pose"]
						except:
							print("[ERROR] Attribute Not found annotation.object.pose .")
							return 0
						try:
							tmp=obj["truncated"]
						except:
							print("[ERROR] Attribute Not found annotation.object.truncated .")
							return 0
						try:
							tmp=obj["difficult"]
						except:
							print("[ERROR] Attribute Not found annotation.object.difficult .")
							return 0
						try:
							tmp=obj["bndbox"]["xmin"]
						except:
							print("[ERROR] Attribute Not found annotation.object.bndbox.xmin .")
							return 0
						try:
							tmp=obj["bndbox"]["ymin"]
						except:
							print("[ERROR] Attribute Not found annotation.object.bndbox.ymin .")
							return 0
						try:
							tmp=obj["bndbox"]["xmax"]
						except:
							print("[ERROR] Attribute Not found annotation.object.bndbox.xmax .")
							return 0
						try:
							tmp=obj["bndbox"]["ymax"]
						except:
							print("[ERROR] Attribute Not found annotation.object.bndbox.ymax .")
							return 0
				return 1
						

			else:
				print("[ERROR] Given JSON file data is empty.")
				return 0


		else:
			print("[ERROR] Given JSON file is empty.")
			return 0


	def convertJsonToPascal(self,file_path):
		with open(file_path) as json_file:  
			data = json.load(json_file)
			if self.checkJson(data) == 1:
				for image in data['data']:

					annotation = ET.Element("annotation")

					ET.SubElement(annotation,"folder", name = "folder").text = image["annotation"]["folder"]
					ET.SubElement(annotation,"filename", name = "filename").text = image["annotation"]["filename"]
					ET.SubElement(annotation,"path", name = "path").text = image["annotation"]["path"]

					source = ET.SubElement(annotation,"source")
					ET.SubElement(source,"database", name = "database").text = image["annotation"]["source"]["database"]

					size = ET.SubElement(annotation,"size")
					ET.SubElement(size,"width", name = "width").text = str(image["annotation"]["size"]["width"])
					ET.SubElement(size,"height", name = "height").text = str(image["annotation"]["size"]["height"])
					ET.SubElement(size,"depth", name = "depth").text = str(image["annotation"]["size"]["depth"])

					ET.SubElement(annotation,"segmented", name = "segmented").text = str(image["annotation"]["segmented"])

					for obj in  image["annotation"]["object"]:
						object = ET.SubElement(annotation,"object")
						ET.SubElement(object,"name", name = "name").text = obj["name"]
						ET.SubElement(object,"pose", name = "pose").text = str(obj["pose"])
						ET.SubElement(object,"truncated", name = "truncated").text = str(obj["truncated"])
						ET.SubElement(object,"difficult", name = "difficult").text = str(obj["difficult"])

						bndbox = ET.SubElement(object,"bndbox")
						ET.SubElement(bndbox,"xmin", name = "xmin").text = str(obj["bndbox"]["xmin"])
						ET.SubElement(bndbox,"ymin", name = "ymin").text = str(obj["bndbox"]["ymin"])
						ET.SubElement(bndbox,"xmax", name = "xmax").text = str(obj["bndbox"]["xmax"])
						ET.SubElement(bndbox,"ymax", name = "ymax").text = str(obj["bndbox"]["ymax"])


					tree = ET.ElementTree(annotation)
					tree.write('/'.join(image["annotation"]["path"].split("/")[:-1])+"/"+image["annotation"]["filename"].split(".")[0]+".xml")
			else:
				print("[ERROR] Convert Failed")
				return 0