# Roster
Aloha Spark Competition Recall Roster

Problem:  The 15 MDG Medical Readiness flight and UDMs requested a mobile app that would allow MDG staff to have their unit’s recall
roster, recall alert messages, and Gp AtHoc messages.  After performing a randomized survey on personnel around the 15 MDG, it showed
that only a handful of individuals had the recall roster on person or knew where to find their flight’s recall roster in the work area.
In addition, in-processing new personnel would have their information transcribed incorrectly; thus, when a recall arises, messages
would be delayed getting to them.  The overall solution would be similar to the installation AtHoc system except that it would be
personalized to the Gp-level of utilization.  Since in this day and age almost everyone has their smartphone on them, having a Mobile
Recall and Communication App would make unit communication more effective.  In broader implementation, Gp’s across the Wg could utilize
this app as a “localized” communication tool.  The app would be set up in a tiered system where flight-level staff would have access to
their flight information; Sq-level staff would have access to all specific flight and Sq information; and Gp-level staff would have
access to all Gp-level and below information.  Python 3 is the main programming language utilized for this project since it is
open-sourced and user friendly when updating information.

Currently, the code is pulling 2 flights’ information (PII areas marked out) via asking for user input.  The user will be able to pull
individual records or the whole flight’s records at once.  The code functions via the Command Prompt window.  Two scripts are used for
this application – RecallRoster.py is the main application and RecallRosterData.py is the variable repository for the main application.
App GUI(s) will be implemented later when the bare bones of the program is functional.

To start the code in the Command Prompt window, redirect the current directory to where the file is saved.  Type in "RecallRoster" and
press enter.  Enter names of flight members in the Bioenvironmental Engineering Flight (i.e. Derick or Derick Chandler or Chandler).
Information will population.  You will be able to pull all of the flight information via typing the flight name (i.e. Bioenvironmental
Engineering or Bio or BE).
