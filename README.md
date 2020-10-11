## Welcome to the Auto-Mail-Sender wiki!

### 1. You must have Python installed.
### 2. You must install yagmail
   (in your command prompt, type : python -m pip install yagmail )

### 3. Setup your gmail account for the program to use 
   1. First, you need to enable 2-Step Verification. Just go to your Google Account > Security > Signing in to Google, and select 2-Step Verification and follow the instruction.
   2. Next, create an app password. Just select ‘App passwords’ under ‘2-Step Verification’. Select ‘Other’ in the ‘Select app’ dropdown.
   3. Enter a name, e.g. Python, and click ‘GENERATE’. Note this name has no link to the Python script and it could be anything.
   4.  Then you will get a new app password. Copy and save the 16-character password without space, e.g. xnwbjmgvjeeevlgc, to use in your Python script.

### 4. Replace values in the code by your own (your open the code with notepad or other programs)
   * user -> your email adress
   * app_password -> the password juste created above
   * to -> the reveiver email adress
   * subject -> Subjet of the email
   * content -> the content of your email (between the """\ and """ )
   * timer -> time between each sending (in seconds)

### 5. Run the program in the background for as long as you want (you have to keep you computer open for the program to work)
