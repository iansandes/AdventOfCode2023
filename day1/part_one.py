import re

def clear_calibration_document(document_path: str):
    '''Extract numbers of a given string in a line of a file and return 
    the first and the last number concatened and converted to int of 
    each line.

    Parameters:
		document_path (str): The .txt document path

	Returns:
		calibration_values (list): List with extracted numbers of each line
    '''
    calibration_values = []
    calibration_document = open(document_path, "r")

    for line in calibration_document:
        clear_line = re.findall(r'\d', line)
        calibration_values.append(int(clear_line[0] + clear_line[-1]))

    return calibration_values


if __name__ == "__main__":
    calibration_values = clear_calibration_document("calibration_document.txt")
    sum_calibration_values = sum(calibration_values)
    print(f"The sum of all of the calibration values is {sum_calibration_values}")

  
