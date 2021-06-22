{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter date in the form of dd/mm/yyyy: 24/10/2020\n",
      "Enter the time in 'hr:mm:ss' 12 hrs format: 06:30:15\n",
      "Enter AM/PM: AM\n",
      "2459146.77101 Julian days\n"
     ]
    }
   ],
   "source": [
    "#to convert the given date to julian days\n",
    "\n",
    "from time import ctime\n",
    "from datetime import date\n",
    "import calendar\n",
    "\n",
    "#jan 1 4713 BC 1200 hrs - julian time starts\n",
    "\n",
    "def getInput():\n",
    "    \n",
    "    date_input = input (\"Enter date in the form of dd/mm/yyyy: \").split('/')\n",
    "    day_input = input(\"Enter the time in 'hr:mm:ss' 12 hrs format: \").split(\":\")\n",
    "    meridiem = input(\"Enter AM/PM: \")\n",
    "    year = int(date_input[2])\n",
    "    month = int(date_input[1])\n",
    "    day = int(date_input[0])\n",
    "    hour=int(day_input[0])\n",
    "    minute=int(day_input[1])\n",
    "    second=int(day_input[2])\n",
    "    \n",
    "    return year, month, day, hour, minute, second, meridiem\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    \n",
    "    years, months, days, hours, minutes, seconds, meridien = getInput()\n",
    "    \n",
    "    #to calculate the days BC\n",
    "    bc_days = 0\n",
    "    for i in range(4714, 1, -1):\n",
    "        if i == 0:\n",
    "            break\n",
    "        elif i%4 == 0: #to check leap year\n",
    "            bc_days = bc_days + 366\n",
    "        else:\n",
    "            bc_days = bc_days+ 365\n",
    "\n",
    "    #print(bc_days)\n",
    "\n",
    "    #to calculate the days AD\n",
    "    julian_days= 0\n",
    "\n",
    "    for i in range (0, years-1):\n",
    "        if i%4 == 0:\n",
    "            julian_days = julian_days + 366\n",
    "        else:\n",
    "            julian_days = julian_days + 365\n",
    "\n",
    "    #print(julian_days)\n",
    "\n",
    "    #to calculate the number of days in the current mentoned year\n",
    "\n",
    "    day = 0\n",
    "    for i in range (0, months-1):\n",
    "        if i == 9 or 4 or 6 or 11: #months having 30 days \n",
    "            day = day + 30 \n",
    "        elif i == 2:\n",
    "            if years%4 == 0: #febraury has 29 days in a leap year\n",
    "                day = day + 29\n",
    "            else:\n",
    "                day = day + 28\n",
    "        else:\n",
    "            day = day + 31\n",
    "\n",
    "    # print(days)\n",
    "    # print(day)\n",
    "\n",
    "    #calculation for mantissa\n",
    "    point=0\n",
    "    if meridien==\"AM\":\n",
    "        point = ((hours*60*60) + (minutes*60) + seconds + 43200) #43200 seconds make up 12 hours - 12:00 to 00:00\n",
    "        day = day - 1 #will be taken into account in seconds from previous day 12 noon\n",
    "    else:\n",
    "        point = ((hours*60*60) + (minutes*60) + seconds)\n",
    "\n",
    "    mantissa = round(point/86400, 5) #86400 is the total number of seconds in 24 hrs i.e., one day \n",
    "\n",
    "    '''subract 10 to account for the change over from julian to gregorian calender\n",
    "    because it did not properly reflect the actual time taken by earth to complete one rotation\n",
    "\n",
    "    transition happened during the year 1582 '''\n",
    "\n",
    "    if years >= 1582: \n",
    "        final = bc_days + julian_days + days + day + mantissa -10\n",
    "    else:\n",
    "        final = bc_days + julian_days + days + day + mantissa\n",
    "\n",
    "    print(str(final) + \" Julian days\")\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda root]",
   "language": "python",
   "name": "conda-root-py"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}