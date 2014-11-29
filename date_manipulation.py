
import dateutil.parser
import datetime
import iso8601


def datestamp(interval, date):
	
	interval = int(interval)

	date = iso8601.parse_date(date)
	interval = datetime.timedelta(0, interval)
	
	final = date + interval

	final = final.isoformat()
	
	format1 = final.split('+')[0]
	format1 += '.000Z'
	return format1 
	
