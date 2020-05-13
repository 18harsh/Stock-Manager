def searchBoxStyle():
	return """
	QGroupBox{
	background-color:#9bc9ff;
	font:15pt Times Bold;
	color:white;
	border:2px solid gray;
	border-radius:15px;

	}
	"""
def listBoxStyle():
	return """
	QGroupBox{
	background-color:#fcc324;
	font:15pt Arial Bold;
	color:white;
	border:2px solid gray;
	border-radius:15px;

	}
	"""	
def searchButtonStyle():
	return """
	QPushButton{
	background-color:#fcc324;
	border-style:outset;
	border-width:2px;
	border-radius:10px;
	border-color:beige;
	font:12px;
	padding:6px;
	min-width:6em;
	}
	"""	
def listButtonStyle():
	return """
	QPushButton{
	background-color:#9bc9ff;
	border-style:outset;
	border-width:2px;
	border-radius:10px;
	border-color:beige;
	font:12px;
	padding:6px;
	min-width:6em;
	}
	"""	

def productbottomFrame():
	return """
	QFormLayout{
	font:15pt Times Bold;
	background-color:#fcc324;
	}
	"""		
def producttopFrame():
	return """
	QVBoxLayout{
	font:20pt Times Bold;
	background-color:white;
	}
	"""			