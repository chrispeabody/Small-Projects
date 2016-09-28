"Stringgen" was a fun little tool I created to randomly generate strings. I used it to come up with names for things, and find interesting word combinations.

--RUNNING THE PROGRAM--

You run the program by typing in a console:
python generate.py [config filepath]

Then you type the number of strings you would like to generate, or type "exit" to close the program. After the strings are generated you will be prompted again, and again. The key to the string generation is in the config file, and the program will generate these based on what the configuration instructs it to do.

--CONFIG FILES--

Config files are made up of two sections. There are LIST sections, and a FORMULAS section. Each list section is started by the line 'LIST'. You may enter as many words as you'd like on the following lines, then leave a blank line. You may create as many LIST sections in a row as you would like.

The FORMULAS section is a list of formulas by which to generate strings. Putting a number will pull a random word from the list associated with it. The first LIST section is associated with 1, the second with 2, etc. Putting a ^ symbol before a list number capitolizes whatever word is generated. Putting anything in (parynthesis) enters the literal contents into the string. Only individual words can be in parynthesis. Putting a dash (-) between two pieces of the formula joins them together to make a compound word.

If multiple formulas are present, a random one will be selected for each string. Two config file examples can be seen in the \type\ folder of this repository. Have fun!

Email me if you have any questions: cgpzbd@mst.edu
