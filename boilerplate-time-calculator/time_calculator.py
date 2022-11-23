def add_time(start, duration, day = None):
#Time start
  time, meridiem = start.split()
  hours, minutes = map(int, time.split(':'))
    
#Duration that need to be add
  durationhours, durationminutes = map(int, duration.split(':'))

#Designing the time-calculator
  totalminutes = minutes + durationminutes
  convertminutes = 0

#Fixing the minutes
  if totalminutes > 60:
    convertminutes = totalminutes // 60
    totalminutes -= 60

  if len(str(totalminutes)) < 2:
    totalminutes = '0' + str(totalminutes)

#Time calculations
  totalhours = hours + durationhours + convertminutes
  days = totalhours // 24

#AM and PM cycles
  if meridiem == 'PM':
    if totalhours >= 12:
      totalhours = totalhours % 12
      meridiem = 'AM'
      days += 1
      
  if meridiem == 'AM':
    if totalhours >= 12:
      totalhours = totalhours  % 12
      meridiem = 'PM'

  if durationhours == 24 or meridiem == 'PM':
    meridiem = 'PM'

  if durationhours == 24 or meridiem == 'AM':
    meridiem = 'AM'

#Fixing the hour format
  if totalhours == 0:
    totalhours = 12

#Process
  new_time = ' '

  if day == None:
    if days == 0:
      new_time = str(totalhours) + ":" + str(totalminutes) + ' ' + meridiem
    elif days == 1:
      new_time = str(totalhours) + ":" + str(totalminutes) + ' ' + meridiem + ' (next day)'
    else :
      new_time = str(totalhours) + ":" + str(totalminutes) + ' ' + meridiem + ' (' + str(days) + ' days later)'
      
  if day :
    week = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
    new_time = str(totalhours) + ":" + str(totalminutes) + ' ' + meridiem + ', ' +str(week[(week.index(day.capitalize()) + days) % 7]) 
    
    if days == 1:
      new_time = str(totalhours) + ":" + str(totalminutes) + ' ' + meridiem + ', ' +str(week[(week.index(day.capitalize()) + days) % 7]) + ' (next day)'
      
    if days > 1 :
      new_time = str(totalhours) + ":" + str(totalminutes) + ' ' + meridiem + ', ' +str(week[(week.index(day.capitalize()) + days) % 7]) + ' (' + str(days) + ' days later)'

  
  return new_time
