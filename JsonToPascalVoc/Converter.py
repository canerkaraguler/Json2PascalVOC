import xml.etree.cElementTree as ET
import json 
class Converter:

	def __init__(self):
		pass


	def convertJsonToPascal(self,file_path):
		with open(file_path) as json_file:  
			data = json.load(json_file)
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