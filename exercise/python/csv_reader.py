from csv import reader
import dataset

def get_rows(file_name):
	rdr=reader(open(file_name, 'rb'))
	return [row for row in rdr]

def eliminate_mismatches(head_rows, data_rows):
	all_short_headers=[h[0] for h in head_rows]
	skip_index= []
	final_header_rows=[]
	for header in data_rows[0]:
		if header not in all_short_headers:
			index=data_rows[0].index(header)
			if index not in skip_index:
				skip_index.append(index)

		else:
			for head in head_rows:
				if head[0]==header:
					final_header_rows.append(head)

	return skip_index, final_header_rows


def zip_data(headers, data):
	zipped_data=[]
	for drow in data:
		zipped_data.append(zip(headers, drow))
	return zipped_data