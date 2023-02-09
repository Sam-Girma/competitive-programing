class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr":"04", "May":"05", "Jun": "06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        day, month, year = date.split()
        dig_day = ""
        for i in day:
            if i.isdigit():
                dig_day+=i
            else:
                break
        if len(dig_day)==1:
            dig_day = "0"+dig_day
        return year+"-"+months[month]+"-"+dig_day
