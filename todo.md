
now

later
* Different styles and sectioning
  * Some people may desire a configuration where there is empty space below a problem and not a line beside it
  * Add sections with section instructions so that each problem doesn't need their own instructions
* Answer key export
  * Must check input list to see if it is a list of just questions or question and answer pairs
* Add multiple choice option and formatting?
  * Could also add some other problem options like writing problems
    * Modifiable writing space
    * Maybe add ability to add images?
  * New line would be added underneath original problem with letter choices
  * Automatically decide how many should be on a row based on what fits
    * Either 4, 2, or 1 option per line
* Add math problem formatting
  * Use $$<math>$$ formatting so that problems can be formatting while text is not
    * Maybe use other typical formatting symbols like single $'s
* Clean up similarly named things in code
* Multilanguage support
  * This seems like it would be difficult
  * All you would have to do would be change the 'Name' p to say name in whatever language the user desires
  * Could easily use python translate, I'm not sure if that would bloat the software if it wasn't really needed though

* Make an add_object method where you can specify type and then make an add_problem, add_instruction, etc. that just point to an object class. That way, you won't have to specify a type in kwargs, you'll just specify it in the method name.
  * Actually the object class should just hold an object based on it's type
  * One object type can be group type where you can make a group of questions
  * I'm thinking of these ideas but don't know when people would actually use them
