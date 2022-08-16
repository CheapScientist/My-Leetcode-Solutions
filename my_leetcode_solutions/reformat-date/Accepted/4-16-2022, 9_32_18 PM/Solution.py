// https://leetcode.com/problems/reformat-date

class Solution:
    def reformatDate(self, date: str) -> str:
        a = date.split(' ')
        mon = 1 
        monSet = {"Jan": '1', "Feb": '2', "Mar":'3', "Apr":'4', "May":'5', "Jun":'6', "Jul":'7', "Aug":'8', "Sep":'9', "Oct":'10', "Nov":'11', "Dec":'12'}
        mon = monSet[a[1]]
        if int(mon) < 10:
            monStr = '0' + str(mon)
        else:
            monStr = str(mon)
        day = a[0][:-2]
        if int(day) < 10:
            day = '0'+ day
        ans = a[2] + '-' + monStr + '-' +  day
        return ans
            
            